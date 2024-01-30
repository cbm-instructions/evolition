#!/usr/bin/env python3
import board
import neopixel
import time
import config
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#GPIO 12, 5 von rechts außen (D in)
#GND 3 außen
#5V 2 außen

maxAnzahl = config.room['maxSeats']

pixel_pin1 = board.D12 #Ändern nach GPIO Pin
num_pixels1 = 15 #Anzahl LEDs
pixel_pin2 = board.D21
num_pixels2 = 15

pixelsz = neopixel.NeoPixel(pixel_pin1, num_pixels1, brightness = 0.05, auto_write = False)
pixelse = neopixel.NeoPixel(pixel_pin2, num_pixels2, brightness = 0.05, auto_write = False)

def alleZahlenAus():
    pixelsz.fill((0, 0, 0))
    pixelse.fill((0, 0, 0))
    pixelsz.show()
    pixelse.show()

def alleZahlenAn(color):
    alleZahlenAusz()
    alleZahlenAuse()
    pixelsz.fill(color)
    pixelse.fill(color)
    pixelsz.show()
    pixelse.show()


#---------------------------------------------------------------Ziffern Zehner--------------------------------------------------------
def alleZahlenAusz():
    pixelsz.fill((0, 0, 0))
    pixelsz.show()

def alleZahlenAnz(color):
    alleZahlenAusz()
    pixelsz.fill(color)
    pixelsz.show()


def zahl0z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[3] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()


def zahl1z(color):
    alleZahlenAusz()
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl2z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[2] = color
    pixelsz[3] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl3z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[2] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl4z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[7] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl5z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl6z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[3] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl7z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl8z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[3] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

def zahl9z(color):
    alleZahlenAusz()
    pixelsz[0] = color
    pixelsz[1] = color
    pixelsz[2] = color
    pixelsz[4] = color
    pixelsz[5] = color
    pixelsz[7] = color
    pixelsz[9] = color
    pixelsz[10] = color
    pixelsz[11] = color
    pixelsz[12] = color
    pixelsz[13] = color
    pixelsz[14] = color
    pixelsz.show()

#---------------------------------------------------------------Ziffern Einer--------------------------------------------------------

def alleZahlenAuse():
    pixelse.fill((0, 0, 0))
    pixelse.show()

def alleZahlenAne(color):
    alleZahlenAuse()
    pixelse.fill(color)
    pixelse.show()


def zahl0e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[3] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()


def zahl1e(color):
    alleZahlenAuse()
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl2e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[2] = color
    pixelse[3] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[14] = color
    pixelse.show()

def zahl3e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[2] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl4e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[7] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl5e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl6e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[3] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl7e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl8e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[3] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()

def zahl9e(color):
    alleZahlenAuse()
    pixelse[0] = color
    pixelse[1] = color
    pixelse[2] = color
    pixelse[4] = color
    pixelse[5] = color
    pixelse[7] = color
    pixelse[9] = color
    pixelse[10] = color
    pixelse[11] = color
    pixelse[12] = color
    pixelse[13] = color
    pixelse[14] = color
    pixelse.show()


#-------------------------------------------------------------Logik-------------------------------------------------
farbe = (0, 0, 0)
def eingabe(zahl):
    #Farben
    weiß = (255, 255, 255)
    grün = (0, 255, 0)
    gelb = (255, 255, 0)
    rot = (255, 0, 0)


    #Abfangen: Fehlermeldung in roten Nullen
    if zahl >= 100 or zahl < 0:
        farbe = rot
        zahl0z(farbe)
        zahl0e(farbe)
        exit(-1)

    #Farbänderung
    if zahl < (maxAnzahl // 3):
        farbe = grün
    elif zahl < (2 * (maxAnzahl // 3)):
        farbe = gelb
    elif zahl >= (2 * (maxAnzahl // 3)):
        farbe = rot

    #Aufrufe der Zahlen

    #Zehner
    zehner = zahl // 10
    if zehner == 0:
        zahl0z(farbe)
    if zehner == 1:
        zahl1z(farbe)
    if zehner == 2:
        zahl2z(farbe)
    if zehner == 3:
        zahl3z(farbe)
    if zehner == 4:
        zahl4z(farbe)
    if zehner == 5:
        zahl5z(farbe)
    if zehner == 6:
        zahl6z(farbe)
    if zehner == 7:
        zahl7z(farbe)
    if zehner == 8:
        zahl8z(farbe)
    if zehner == 9:
        zahl9z(farbe)

    #Einer
    einer = zahl % 10
    if einer == 0:
        zahl0e(farbe)
    if einer == 1:
        zahl1e(farbe)
    if einer == 2:
        zahl2e(farbe)
    if einer == 3:
        zahl3e(farbe)
    if einer == 4:
        zahl4e(farbe)
    if einer == 5:
        zahl5e(farbe)
    if einer == 6:
        zahl6e(farbe)
    if einer == 7:
        zahl7e(farbe)
    if einer == 8:
        zahl8e(farbe)
    if einer == 9:
        zahl9e(farbe)

def bekommeFarbe():
    return farbe

def bekommeAnzahl():
    #Gezählte Personenanzahl wird dynamisch auf der Webseite des Sensors angezeigt
    #Selenium wird verwendet, um den Wert aus dem verändert werdenden DOM parsen zu können
    
    options = webdriver.FirefoxOptions()
    options.headless = True  # Anpassung der Driveroptionen damit Firefox ohne GUI gestartet wird.
    
    driver = webdriver.Firefox()
    driver.get(config.sensor('url'))
    soup = BeautifulSoup(driver.page_source)
    
    anzahlSensor = ""
    for tag in soup.find_all("h1", id="count"):
            anzahlSensor = tag.text
    return anzahlSensor
#---------------------------------------------------------Methodenaufrufe-------------------------------------------------
if __name__ == '__main__':
    while true:
        try:
            # eingabe(bekommeAnzahl) bekommeAnzahl muss troubleshooted werden 
            eingabe(9) #Zu vorführen das die Anzeige der Zahlen funktioniert
            # time.sleep(2) # Damit das Skript alle 2 Sekunden weiterläuft
        except KeyboardInterrupt:
            alleZahlenAusz() #schaltet alle LEDs aus, wenn das Skript beendet wird
            alleZahlenAuse()