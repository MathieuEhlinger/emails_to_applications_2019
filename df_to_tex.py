# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 20:32:45 2019

@author: Mathieu
"""

import os  
import datetime

def write_tex(mail, output_directory):
    
    '''
    Input : pd.DataFrame
    Concats the LaTeX code and the data, outputs a TeX data
    
    Competing in the Most Disgusting Function of the Known Universe contest
    '''
    
    #Checks if the int for amout of number is between 3 and 18. If not, deleted.
    if int(mail['stuz'].iloc[0])>=18 or int(mail['stuz'].iloc[0])<=2 :
        mail['stuz'].iloc[0]=''      

    
          
    lat_file = '\
        \\documentclass[a4paper, 9pt]{extletter} \n\
        \\usepackage{nopageno}\n\
        \\usepackage{phonenumbers}\n\
        \\usepackage{tabularx}\n\
        \\usepackage{tabularx,array, lipsum}\n\
        \\usepackage{cellspace}\n\
        \\usepackage{hyperref}\n\
        \\usepackage{xcolor}\n\
        \\usepackage{setspace}\n\
        \\usepackage{enumitem}\n\n\
        \\newenvironment{myTextfield}\n\n\n\
        \\setlength\\cellspacetoplimit{6pt}\n\
        \\setlength\\cellspacebottomlimit{6pt}\n\
        \\addparagraphcolumntypes{X}\n\
        \\usepackage[ddmmyyyy]{datetime}\n\
        \\renewcommand{\\dateseparator}{.}\n\
        \\usepackage[paper=a4paper, left=15mm, right=20mm, top=20mm, bottom=15mm]{geometry}\n\n\
        \\newcolumntype{R}{>{\\raggedright\\arraybackslash}X}%\n\n\n\\begin{document} \n\
        \\begin{Form}\n\n\
        \\begin{flushright}\n\
        \tDüsseldorf, den \\today\\\\\n\
        \t(Ilhan) \\phonenumber[area-code-sep=brackets]{0211 - 81 - 12615} \\\\\n\
        % \t(Häser) \\phonenumber[area-code-sep=brackets]{0211 - 81 - 15841} \\\\\n\
        \\end{flushright}\nZentrum/Institut/Klinik\n\\begin{enumerate}\n\
       \\item Über die Vorsitzenden der Komission zur Verteilung der Stunden für stud. und wiss. Hilfskräfte\\footnote{siehe Seite 2 \\--Anschrift\\--}\n\
       \\item Über die Dekanin/den Dekan der Medizinischen Fakultät \\\\ (\\textbf{Ziffer 1. und 2. entfällt bei Finanzierung über Drittmittel})\n\
       \\item An die Personalabteilung des Universitätsklinikums Düsseldorf \n\
       \\end{enumerate}\n\n\\underline{Betrifft:}\n\n\n\n\
       \\begin{center}\t\n\
       \t\\begingroup\n\
       \t\\setlength{\\tabcolsep}{1em} \n\
       \t\\begin{tabular}{l c c c }\t  \n\
       \t  Antrag auf  & \t  \n\
       \t\t\\ChoiceMenu[combo,name=typeEmp1,height=0.1cm,default={'+str(mail['einst'].iloc[0]) +'},width=2.5cm,borderwidth=0,backgroundcolor={0.95 0.95 0.95}]{}{Einstellung,Weiterbeschäftigung,Wiedereinstellung}\n\
       \t  & \n\t  \teiner \n\t  &\t  \n\t  \t\\ChoiceMenu[combo,name=typeEmp2,default={'+str(mail['rolle'].iloc[0]) +'},width=2.5cm,borderwidth=0,backgroundcolor={0.95 0.95 0.95}]{}{stud. Hilfskraft,wiss. Hilfskraft} \\\\\n\
       \t\\end{tabular} \n\t \n\t \n\
       \t\\begin{tabular}{l c c c }\t\n\
       \t  \tfür die Zeit vom \n \t&\n\
       \t\t\\TextField[name=timeFrom,align=1,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}  \n\
       \t&\n\
       \t  \tbis \n\
       \t&\n\
       \t\t\\TextField[name=timeTo,align=1,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}  \n\
       \t\\end{tabular}\n\t \n\t\\endgroup\t \n\
       \\end{center}\n\n\n\nmit einer durchschnittlichen wöchentlichen Arbeitszeit von \\textbf{'+str(mail['stuz'].iloc[0]) +'} Stunden (max. 17 Std. / min 3 Std.)\n\
       Gesamtstundenanzahl: \\textbf{'+str(int(mail['stuz'].iloc[0])*4) +'} Stunden. \n\n\n\n\n\
       \\begin{center}\n\\begin{tabularx}{\\columnwidth}{|X|R|}\n\
       \\hline\n  \\textsf{Name:} \\hspace{3.5mm} \\TextField[name=vname,width=6.5cm,value={'+str(mail['vorname'].iloc[0]) +'},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\n\
       &\n  \\textsf{Nachname:} \\TextField[name=nname,width=5cm,value={'+str(mail['name'].iloc[0]) +'},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} \\\\\n\
       \\hline\n\\end{tabularx}\n\\begin{tabularx}{\\columnwidth}{|X|R|}\n\
       \\textsf{Anschrift:} \\TextField[name=adresse,width=6.5cm,value={'+str(mail['adresse'].iloc[0]) +'},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\n  &\n\
       \\textsf{Telefon:} \\hspace{3.1mm} \\TextField[name=telefon,width=4cm,value={'+str(mail['tel'].iloc[0]) +'},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} \\\\\n\
       \\hline\n\\end{tabularx}\n\\end{center}\n\n\nfür die Lehrveranstaltung: \\hspace{2.4mm} \\ChoiceMenu[combo,name=kursName,borderwidth=0,width=8.5cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}{(Ilhan) \\textbf{Makroskopisch Anatomischer Kurs},(Häser) \\textbf{Mikroskopisch Anatomischer Kurs}}\n\n\
       \\begin{myTextfield}\n\t\\renewcommand*{\\LayoutTextField}[2]{\\makebox[0.6em][l]{#1}\\raisebox{\\baselineskip}{\\raisebox{-\\height}{#2}}}\n\
       \tfür Dienstleistungsaufgaben: \\TextField[multiline,name=aBeschr,bordercolor=,width=0.5\\textwidth,height=1cm,value={},backgroundcolor={0.95 0.95 0.95}]{}\n\
       \\end{myTextfield}\n\\hspace{5.2cm} (kurze Angaben zur zu verrichtenden Tätigkeit)\n\n\
       \\textbf{Die stud./wiss. Hilfskraft wird:}\n\n\
       \\begin{enumerate}\n  \\renewcommand{\\arraystretch}{0.5}\n\
       \\item umgang mit Stoffen nach der Gefahrstoffverordnung haben \\hfill \\CheckBox[name=j1,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n1,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\item Röntgen-/Strahlenschutzbereich eingesetzt \\hfill \\CheckBox[name=j2,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n2,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\item Infektiösem- oder Infektionsverdächtigem zu tun haben \\hfill \\CheckBox[name=j3,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n3,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\item im Laborbereich eingesetzt \\hfill \\CheckBox[name=j4,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n4,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\item in Sektionsräumen tätig sein \\hfill \\CheckBox[name=j5,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n5,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\item in der stationären-/ambulanten Krankenversorgung eingesetzt \\hfill \\CheckBox[name=j6,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Ja} \\CheckBox[name=n6,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{Nein}\n\
       \\end{enumerate}\n\n\n\n\
       \\CheckBox[name=weekdays,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} Beschäftigung erfolgt an folgenden Wochentagen:\n\n\
       \\begin{tabular}{llll}\n\
       \tMontag: & \\TextField[name=mmVon,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{von } & \\TextField[name=moBis,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{bis } & Uhr \\\\\n\
       \tDienstag: & \\TextField[name=dVon,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{von } & \\TextField[name=diBis,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{bis } & Uhr \\\\\n\
       \tMittwoch: & \\TextField[name=miVon,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{von } & \\TextField[name=miBis,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{bis } & Uhr \\\\\n\
       \tDonnerstag: & \\TextField[name=doVon,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{von } & \\TextField[name=doBis,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{bis } & Uhr \\\\\n\
       \tFreitag: & \\TextField[name=frVon,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{von } & \\TextField[name=frBis,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{bis } & Uhr \\\\\n\
       \\end{tabular}\n\t\n\\CheckBox[name=tutor,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} mit Tutorentätigkeit im Umfang von \\TextField[name=aBesch,align=1,width=1cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} \\hspace{1mm} Stunden wöchentlich. \n\t\n\t\n\
       % \\begin{tabularx}{\\textwidth}{lX}\n% \tFür: \n\
       %  \t&\n% \t\\TextField[name=forTut,width=14cm,value={},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\n\
       %  \t\\\\\n% \t\n% \t&\n% \t(Art des Tutoriums s. Â§1 Abs. 3 Buchst. a-g der Dienstverträge für szud./wiss. Hilfskräfte)\n\
       % \\end{tabularx}\n\n\
       Für: \\TextField[name=forTut,width=14cm,value={},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{} \\\\ \n\
       \\phantom{Für:} \\hspace{1ex}(Art des Tutoriums s. Â§1 Abs. 3 Buchst. a-g der Dienstverträge für szud./wiss. Hilfskräfte)\n\t\n\t\n\
       Falls nicht aus Hilfskraftstunden-Kontingent der Med. Fakultät, Finanzierung durch:\t\t\t\n\t\n\
       \\begin{tabular}{clrl}\n\n\\CheckBox[name=drittMittel,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\\hspace{0.2cm}Drittmittel:\n&\n\
       \\TextField[name=projectName,width=5cm,value={},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\n&\n\\CheckBox[name=freiWiss,width=0.4cm,height=0.4cm,bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\\hspace{0.2cm}freie wiss. Stelle:\n&\n\
       \\TextField[name=stellBeschr,width=5cm,value={},bordercolor=,backgroundcolor={0.95 0.95 0.95}]{}\n\n\\\\\n\n&\n\\hspace{1cm}(Projektbezeichnung)\n&\n\n&\n\
       \\hspace{1cm}(Stellenbezeichnung)\n\
       \\end{tabular}\n\n\t\n\t\n\\end{Form}\n\\end{document}\
    '
    lat_file = lat_file.encode('utf-8')
    tex_file_name = output_directory+'tex/'+str(mail.iloc[0]['name'])+'_'\
        +str(mail.iloc[0]['vorname'])+'_'+str(datetime.date.today())+'.tex'
    
    if os.path.isfile(tex_file_name):
        tex_file_name = tex_file_name[:-4]+'(1)'+'.tex'
    i=2
    while os.path.isfile(tex_file_name):
        tex_file_name = tex_file_name[:-7]+'('+str(i)+')'+'.tex'
        i+=1

    pdf_file_name = tex_file_name[:-4]
    start = pdf_file_name.find('/tex')
    pdf_file_name = pdf_file_name[:start]+pdf_file_name[(start+4):]
    
    with open(tex_file_name,\
              "wb+") as text_file:
        text_file.write(lat_file)
        
    return tex_file_name, pdf_file_name
    