#!/usr/bin/env python3
import csv
import os
import time
import pandas as pd
import datetime
from datetime import datetime
import serial
import LightsaberNumber as led

current_time = datetime.now()
cTime = current_time.strftime("%H")
dayClass = 'daylist/dayList.csv'
dayExam = 'daylist/examList.csv'

shouldBoxShowClass = False
shouldBoxShowExam = False
shouldBoxShowDefault = False
justChanged = False


def classCheck():
    with open(dayClass, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if cTime in row[1]:
                shouldBoxShowClass = True
                justChanged = True
        shouldBoxChangeBack()
        justChanged = False

def examCheck():
    with open(dayExam, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if cTime in row[0]:
                shouldBoxShowExam = True
                justChanged = True
            shouldBoxChangeBack()
            justChanged = False


def whichOtherCheck():
    if os.path.exists(os.getcwd() + dayExam):
        examCheck()
    elif os.path.exists(os.getcwd() + dayClass) and os.path.getsize(os.getcwd() + dayClass) > 0:
        classCheck()

def shouldBoxChangeBack():
    if(shouldBoxShowClass == True and justChanged == False):
        shouldBoxShowClass == False
    if(shouldBoxShowExam == True and justChanged == False):
        shouldBoxShowClass == False


def connectWithArduino(whichPicture):
    with serial.Serial('/dev/ttyACM0', 9600) as ser:
        isPictureThere = False
        time.sleep(0.3) # Warten da pyserial anscheinend vom Port aufmachen returned bevor der Port bereit ist 
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        while isPictureThere == False:
            ser.write(str(whichPicture + "\n").encode("ascii"))
            line = ser.readline().decode('utf-8').rstrip()
            if"Bin da" in line:
                isPictureThere = True
            else:
                ser.reset_input_buffer()
                ser.reset_output_buffer()



def sendToBox():
    if __name__ == '__main__':
        whichOtherCheck()
        whichPicture = 4
        if shouldBoxShowExam:
            whichPicture = 2
        elif shouldBoxShowClass:
            whichPicture = 3
        else:
            whichPicture = 4
        
        whichColor = led.bekommeFarbe()
        print(whichColor)

        if whichColor == (255, 0, 0):
            whichPicture = 1

        #connectWithArduino(whichPicture) bisher keine Reaktion von ArduinoUno
        
sendToBox()