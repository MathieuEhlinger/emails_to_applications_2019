# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:36:30 2019

@author: Mathieu
"""


import email
import re
import chardet
import getpass
import imaplib
import os


def read_cfg(file_name='config.cfg'):
    with open('config.cfg', 'r', encoding='utf-8') as infile:
        content=str(infile.read())
        content = content.replace('\n', '=')
        imap_url = re.compile(r'imap_url=[\W,\w]*output_directory').search(content).group().split('=')[1]
        desti_folder_name=re.compile(r'desti_folder_name=[\W,\w]*desti_folder_name2').search(content).group().split('=')[1]
        desti_folder_name2=re.compile(r'desti_folder_name2=[\W,\w]*').search(content).group().split('=')[1]
        output_directory = re.compile(r'output_directory=[\W,\w]*desti_folder_name').search(content).group().split('=')[1]
        infile.close()  
    return imap_url, desti_folder_name, desti_folder_name2, output_directory

    

def try_connection(imap_url):
    for i in range(3):
        user =input('Email adress :')
        password = getpass.getpass('Password :')
        
        try :
            connection = imaplib.IMAP4_SSL(imap_url)
        except : 
            print ('Connection error or invalid imap adress - change it in main.cfg')
            
        try:
            connection.login(user, password)
            print('Connected')
            connection.logout()
            break
        
        except :
            print('Invalid Login/Password combination or connection to server failed')
            continue
        
        print(connection.error)
        if i==3: raise
    return user, password

def get_mail(num, connection):
    result, data = connection.uid('fetch', num, '(RFC822)')
    if result == 'OK':
        email_message = email.message_from_bytes(data[0][1])
        mail_dict=dict()
        mail_dict['UID']= email_message['UID']
        mail_dict['From']= email_message['From']
        mail_dict['To']= email_message['To']
        mail_dict['Date']= email_message['Date']
        mail_dict['Subject'] = email_message['Subject']
        content = email_message.get_payload()
        
        if type (content)==list:
            content_list = list()
            for subpart in content :
                encoding_type=chardet.detect(subpart.as_bytes())
                
                content_list.append(subpart.as_bytes()\
                                    .decode(encoding_type['encoding']))
                
            concat = ''.join(content_list)
            mail_dict['Content'] =concat
    
        else :
            content = email_message.get_payload(None, True)
            encoding_type=chardet.detect(content)
            mail_dict['Content'] = content.decode\
                (encoding_type['encoding'])

    return mail_dict


def create_pdf(input_filename, output_filename):
    print('In : ',print(os.getcwd()))
    print(input_filename,' to ',output_filename )
    print('----------')
    print('pdflatex',  
        '-output-format=pdf',
        str('-job-name=' + output_filename), ' ',
        input_filename)
    os.system(str("pdflatex -interaction=nonstopmode -output-format=pdf \
                  -job-name="+output_filename+' '+\
        input_filename))
#    process = subprocess.Popen([
#        'pdflatex',   # Or maybe 'C:\\Program Files\\MikTex\\miktex\\bin\\latex.exe
#        '-output-format=pdf',
#        str('-job-name=' + output_filename),
#        input_filename])
##    pdflatex -output-format=pdf -job-name=./output/Clark_Kent_2019-01-23.pdf  ./output/tex/Clark_Kent_2019-01-23.tex
#    process.wait()