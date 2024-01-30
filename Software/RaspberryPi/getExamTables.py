#!/usr/bin/env python3
import requests
import pandas as pd
import pdfplumber
import os 
import glob 


path = os.getcwd() + '/examTables/'


def getExamIB():
    url = 'https://services.informatik.hs-mannheim.de/pruefungsplan?stdg%5B%5D=B&sem%5B%5D=%25&prof%5B%5D=%25&aufsicht%5B%5D=%25&zeige_raum=1&zeige_endezeit=1&zeige_woche1=1&zeige_woche2=2&zeige_woche3=3&p=1&q=%24q&landscape=PDF-Version+im+Querformat'
    field = 'IB.pdf'
    getExamTable(url, field)
    getExamCSV(field)
    

def getExamCSB():
    url = 'https://services.informatik.hs-mannheim.de/pruefungsplan?stdg%5B%5D=C&sem%5B%5D=%25&prof%5B%5D=%25&aufsicht%5B%5D=%25&zeige_raum=1&zeige_endezeit=1&zeige_woche1=1&zeige_woche2=2&zeige_woche3=3&p=1&q=%24q&landscape=PDF-Version+im+Querformat'
    field = 'CSB.pdf'
    getExamTable(url, field)
    getExamCSV(field)
    

def getExamIMB():
    url = 'https://services.informatik.hs-mannheim.de/pruefungsplan?stdg%5B%5D=e&sem%5B%5D=%25&prof%5B%5D=%25&aufsicht%5B%5D=%25&zeige_raum=1&zeige_endezeit=1&zeige_woche1=1&zeige_woche2=2&zeige_woche3=3&p=1&q=%24q&landscape=PDF-Version+im+Querformat'
    field = 'IMB.pdf'
    getExamTable(url, field)
    getExamCSV(field)
    

def getExamUIB():
    url = 'https://services.informatik.hs-mannheim.de/pruefungsplan?stdg%5B%5D=U&sem%5B%5D=%25&prof%5B%5D=%25&aufsicht%5B%5D=%25&zeige_raum=1&zeige_endezeit=1&zeige_woche1=1&zeige_woche2=2&zeige_woche3=3&p=1&q=%24q&landscape=PDF-Version+im+Querformat'
    field = 'UIB.pdf'
    getExamTable(url, field)
    getExamCSV(field)
    

def getExamIMaster():
    url = 'https://services.informatik.hs-mannheim.de/pruefungsplan?stdg%5B%5D=M&sem%5B%5D=%25&prof%5B%5D=%25&aufsicht%5B%5D=%25&zeige_raum=1&zeige_endezeit=1&zeige_woche1=1&zeige_woche2=2&zeige_woche3=3&p=1&q=%24q&landscape=PDF-Version+im+Querformat'
    field = 'IMa.pdf'
    getExamTable(url, field)
    getExamCSV(field)
    

def getExamTable(url, field):
    r = requests.get(url)
    with open('examTables/' + field, "wb") as f:
        f.write(r.content)


def getExamCSV(field):
    pdf = pdfplumber.open(path + field)

    for i in range(3):
        table = pdf.pages[i].extract_table()
        df = pd.DataFrame(table[1::], columns=table[0])
        df.to_csv(path + '/week' + field[:-4]+ str(i+1) +'Exam.csv')

getExamCSB()
getExamIB()
getExamIMaster()
getExamIMB()
getExamUIB()



