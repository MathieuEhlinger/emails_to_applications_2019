# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:32:35 2019

@author: Mathieu

 1. Extracts imap url, destination folder name for application mails,
 destination folder 2 for other emails and output_directory for the pdf files
 2. Attempts a first connection to server to test login data
 3. Loop of doom
     3.1. 

"""
import os 
import sys
import time
import imaplib
from emails_to_df import analyze_mail
from run_time import time_until_next_run
from df_to_tex import write_tex

from getmail import read_cfg
from getmail import get_mail
from getmail import create_pdf
from getmail import try_connection
import pandas as pd

# The dummy parameter allows to track some data and to limit the number of
# fetched & analyzed mails during debugging
dummy=True

# Gather configuration from ./main.cfg
imap_url, desti_folder_name, desti_folder_name2, output_directory = read_cfg()

# Initialize and test login data
user, password = try_connection(imap_url)


'''
One execution per day at midnight
1. Creates output folders if missing
2. Tries to establish a connection
    -> In case of connection failure : retry in 30 minutes
3. Gathers the UID list of the inbox
4. Iterates through the mail 1 by 1 ( fetch, process, copy, delete )
'''

while True:    
    # Check if output folders exist. If not, create them.
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    if not os.path.exists(output_directory+'tex/'):
        os.makedirs(output_directory+'tex/')

    connection=None    
    while connection==None :
        try : 
            connection = imaplib.IMAP4_SSL(imap_url)
            connection.login(user, password)
            connection.create(desti_folder_name)
            connection.create(desti_folder_name2)
            connection.select()
        except UnboundLocalError :
            print('Connection failed. Will try again in 30 minutes.')
            time.sleep(1800)
            pass
    #Gather UID list of messages in the inbox
    result,data = connection.uid('SEARCH', None, 'ALL')
    
    if dummy: i=0
    if dummy: all_mail_dict = list()
    
    if result == 'OK' :
        # Iteration through the UID's
        for num in data[0].split():
            if dummy :i+=1
            #Collects the mail in form of a dictionnary
            mail_dict = get_mail(num, connection)
            
            #Converts the content from byte to a DataFrame of python strings
            # If no 'Name' or 'Vorname' argument could be found, returns None
            parsed_content = analyze_mail(mail_dict['Content'])
            
            # If the message is an Antrag
            if type(parsed_content)==pd.DataFrame :
                tex_file_name, pdf_file_name = write_tex(parsed_content, \
                                                         output_directory)

                create_pdf(tex_file_name, pdf_file_name)
                
                # Only after the pdf was created, the email is copied to an 
                # other folder
                apply_lbl_msg = connection.uid('COPY', num, desti_folder_name)
                if apply_lbl_msg[0] == 'OK':
                    #If the copy was successful, deletes the email 
                    mov, data = connection.uid('STORE', \
                                               num , '+FLAGS', '(\Deleted)')
                    connection.expunge()
                
            #If the Email doesn't seem to be an Antrag...
            elif type(parsed_content)==type(None):
                # Copy. In case of success, deletes message in inbox.
                apply_lbl_msg = connection.uid('COPY', num, desti_folder_name2)
                if apply_lbl_msg[0] == 'OK':
                    mov, data = connection.uid('STORE', num \
                                               , '+FLAGS', '(\Deleted)')
                    connection.expunge()
                    
            #Other types wouldn't make sense. Raise.
            else :
                raise TypeError
                
            if dummy : all_mail_dict.append(mail_dict)
            if dummy and i==10 : 
                break 
            
    #Returns the number of second until next midnight
    wait_time = time_until_next_run()
    print('Job\'s done for today')
    #Disconnect from the mailbox
    connection.close()
    connection.logout()
    if dummy: break
    #And go to sleep until next day
    time.sleep(wait_time)

