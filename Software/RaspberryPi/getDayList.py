#!/usr/bin/env python3
import csv
import config
from datetime import date
from datetime import datetime
from math import ceil
import pandas as pd
import os
import glob


path = os.getcwd()
roomNumber = config.room['roomNumber']
colT = 8
colE = 8
table_path = '/daylist/dayList.csv'
exam_path = '/daylist/examList.csv'

match date.today().weekday():
    # 3 = MO , 4 = Di , 5 = Mi, 6 = DO, 7 = FR
    case 0:
        colE = 3
    case 1:
        colE = 4
    case 2:
        colE = 5
    case 3:
        colE = 6
    case 4:
        colE = 7

match date.today().weekday():
    # 2 = MO , 3 = Di , 4 = Mi, 5 = DO, 6 = FR
    case 0:
        colT = 2
    case 1:
        colT = 3
    case 2:
        colT = 4
    case 3:
        colT = 5
    case 4:
        colT = 6



def tablesForTheDay():
    hlist = []
    if colT > 6:
        print(colT)
        print("Kein Vorlesungstag")
        print(date.today().weekday())
    else:
        table_files = glob.glob(os.path.join(path, "*.csv"))
        for f in table_files:
            df = pd.read_csv(f)
            with open(f.split(path + '/')[-1], newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if roomNumber in row[colT]:
                        hlist.append(row[1])
        return list(set(hlist))

def week_of_month(dt):
    """ credits to: https://stackoverflow.com/users/174709/josh
        https://stackoverflow.com/questions/3806473/week-number-of-the-month
    Returns the week of the month for the specified date.
    """

    first_day = dt.replace(day=1)

    dom = dt.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom/7.0))

def checkExamWeek():
    now = date.today()
    week = week_of_month(now)
    match now.month:
        case 1:
            if 4 <= week:
                return '1'
            elif week == 5:
                return '2'
        case 2:
            if week == 1:
                return '2'
            elif week == 2:
                return '3'


def examTablesForTheDay(week):
    exam_files = glob.glob(os.path.join(path + '/examTables/week???'+ week +'Exam.csv'))
    elist = []
    for t in exam_files:
        df = pd.read_csv(t)
        with open(t.split(path + '/')[-1], newline='') as t:
            reader = csv.reader(t)
            for row in reader:
                if roomNumber in row[colE]:
                    elist.append(row[1])
        return list(set(elist))

def dayExamListToCSV(week):
    csv = examTablesForTheDay(week)
    df = pd.DataFrame(csv)
    df.to_csv(path + exam_path)

def dayListToCSV():
    csv = tablesForTheDay()
    df = pd.DataFrame(csv)
    df.to_csv(path + table_path)

def whichDayListTable():
    week = checkExamWeek()

    if week == None:
        dayListToCSV()
    else:
        dayExamListToCSV(week)

whichDayListTable()