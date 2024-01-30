#!/usr/bin/env python3
import datetime
from datetime import date
import requests
import pandas as pd
from furl import furl

url = furl('https://services.informatik.hs-mannheim.de/stundenplan/?xsem=')
current_date = datetime.date.today()
classTablePath = 'classTables/'


def checkIfLeapYear(year):
    if year%4 == 0:
        if year%100 != 0:
            return True
        elif year%100 == 0:
            if year%400 == 0:
                return True
    return False


def checkYear(whichDate):
    if current_date.month <= 3:
        if(whichDate == False):
            return current_date.year -1
        else:
            return current_date.year
    elif 9 <= current_date.month <= 12:
        if(whichDate == False):
            return current_date.year
        else:
            return current_date.year + 1

def wSemesterEndDate(year):
    if checkIfLeapYear(year):
        return date(year = year, month = 2, day = 29)
    else:
        return date(year = year, month = 2, day = 28)


def wSemester():
    whichDate = False
    wStart = date(year = checkYear(whichDate), month = 9, day = 1)
    whichDate = True
    wEnd = wSemesterEndDate(checkYear(whichDate))

    if wStart <= current_date <= wEnd:
        return True
    else:
        return False
        
def sSemester():
    if 3 <= current_date.month <= 8:
        return True
    else:
        return False


def checkSemester():
    if sSemester():
        return False
    if wSemester():
        return True

def getTable(semester, course):
    html = requests.get(url).content
    df_list = pd.read_html(html)
    return df_list[-1]

def saveTable(semester, course):
    df = getTable(semester, course)
    df.to_csv(classTablePath + semester + course + '.csv')

def setUrl(semester, course):
    url.set({'xsem': str(semester) + course})

def getIBAndMasterTables():
    course = 'IB'
    for semester in range(1, 8):
        if(semester > 0):
            if(semester < 3):
                getMasterTables(semester)
            setUrl(str(semester), course)
            saveTable(str(semester), course)

def getMasterTables(semester):
    course = 'IM_MDS'
    setUrl(str(semester), course)
    saveTable(str(semester),course)

    course = 'IM_SE'
    setUrl(str(semester), course)
    saveTable(str(semester), course)

def getOtherTables():
    courses = ['CSB', 'UIB', 'IMB']
    if checkSemester():
        semester = 1

        for course in courses:
            setUrl(str(semester),course)
            saveTable(str(semester),course)
        
        semester = 3

        for course in courses:
            setUrl(str(semester),course)
            saveTable(str(semester),course)

    elif checkSemester() == False:
        semester = 2

        for course in courses:
            setUrl(str(semester),course)
            saveTable(str(semester),course)
        
        semester = 4
        for course in courses:
            setUrl(str(semester),course)
            saveTable(str(semester),course)

    for semester in range(6,8):
        for course in courses:
            setUrl(str(semester),course)
            saveTable(str(semester),course)


getIBAndMasterTables()
getOtherTables()
