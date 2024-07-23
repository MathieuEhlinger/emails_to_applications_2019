# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:57:12 2019

@author: Mathieu
"""

import re
import pandas as pd

def get_mails():
    example = " \
    Name : NANANANANANNA             \n     \
    Age : 2137219321       \n    \
    Wish : 8h       \n"
    bad_example = "Name : 1 Age"
    return [example, example, bad_example, bad_example]

def str_purge(string,punct='''!()-[]{};:'"<>/?@#$%^&*_~'''):
    no_punct = ""
    for char in string:
       if char not in punct:
           no_punct = no_punct + char
    return no_punct

def analyze_mail(mail):
    parsed_mail=dict()
    #Attempts to extract name. Failure returns None
    #Name    Tomy\r\nVorname
    
    name_string = re.compile(r'Name[\W,\w]*?\n').search(mail)
    if name_string :
        name_string=name_string.group().split()
        name_string.pop(0)
#        name_string.pop(-1)
        parsed_mail['name']=' '.join(name_string)
    else :
        return None
    
    vorname_string = re.compile(r'Vorname[\W,\w]*?\n').search(mail)
    if vorname_string :
        vorname_string=vorname_string.group().split()
        vorname_string.pop(0)
#        vorname_string.pop(-1)
        parsed_mail['vorname']=' '.join(vorname_string)
    else :
        return None
    
    gdatum_string = re.compile(r'Geburtsdatum[\W,\w]*?\n').search(mail)
    if gdatum_string :
        parsed_mail['gdatum']=gdatum_string.group().split()[1]
    else :
        parsed_mail['gdatum']=''
    
    gort_string = re.compile(r'Geburtsort[\W,\w]*?\n').search(mail)
    if gort_string :
        parsed_mail['gort']=gort_string.group().split()[1]
    else :
        parsed_mail['gort']=''
    
    adresse_string = re.compile(r'Adresse[\W,\w]*?\n').search(mail)
    if adresse_string :
        adresse=adresse_string.group().split()
        adresse.pop(0)
#        adresse.pop(-1)
        parsed_mail['adresse']=' '.join(adresse)
    else :
        parsed_mail['adresse']=' '
    
    email_string = re.compile(r'eMail[\W,\w]*?\n').search(mail)
    if email_string :
        parsed_mail['email']=email_string.group().split()[1]
    else :
        parsed_mail['email']=''
    
    matr_string = re.compile(r'Matrikelnummer[\W,\w]*?\n').search(mail)
    if matr_string :
        parsed_mail['matr']=matr_string.group().split()[1]
    else :
        parsed_mail['matr']=''
    
    fs_string = re.compile(r'Bewerbungssemester[\W,\w]*?\n').search(mail)
    if fs_string :
        parsed_mail['fs']=fs_string.group().split()[1]
    else :
        parsed_mail['fs']=''
    
    stuz_string = re.compile(r'Stundenanzahl[\W,\w]*?\n').search(mail)
    if stuz_string :
        parsed_mail['stuz']=stuz_string.group().split()[1]
    else :
        parsed_mail['stuz']=''
    
    einst_string = re.compile(r'Neu-/Wiedereinstellung[\W,\w]*?\n').search(mail)
    if einst_string :
#        einst_string.pop(0)
#        einst_string.pop(-1)
        parsed_mail['einst']=einst_string.group().split()[1]
    else :
        parsed_mail['einst']=''
    
    rolle_string = re.compile(r'Bewerbung als[\W,\w]*?\n').\
        search(mail)
    if rolle_string :
#         parsed_mail['rolle']=rolle_string.group().split()[2]        
        rolle_string=rolle_string.group().split()
        rolle_string.pop(0)
        rolle_string.pop(0)
#        rolle_string.pop(-1)
        parsed_mail['rolle']=' '.join(rolle_string)
    else :
        parsed_mail['rolle']=''
    
    
    #Attempts to extract age. Failure returns None
    tel_string = re.compile(r'Telefon[\W,\w]*?\n').search(mail)
    if tel_string :
        tel_string=tel_string.group().split()
        tel_string.pop(0)
#        tel_string.pop(-1)
        parsed_mail['tel']=' '.join(tel_string)
    else :
        parsed_mail['tel']=''
    
    return pd.DataFrame(parsed_mail, index=[0])
