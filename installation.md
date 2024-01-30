# Installation

## ArduinoUno
Installieren Sie die Arduino IDE auf einem Rechner Ihrer Wahl und verbinden Sie diesen mit dem ArdunioUno über USB.
Sollte Ihr Betriebssystem nicht automatisch die notwendigen Treiber installieren, sobald Sie das Board anschließen, können Sie unter Windows folgende Schritte befolgen:

- Öffnen Sie den Gerätemanager.

- Unter Anschlüsse (COM, LPT) sollte ein Anschluss namens "Arduino UNO (COMxx)" zu sehen sein. Falls nicht, suchen Sie unter "Andere Geräte" nach "Unbekanntes Gerät"

- Machen Sie auf "Arduino UNO (COMxx)" oder "Unbekanntes Gerät" einen Doppelklick und wählen Sie die Registerkarte Treiben. Klicken Sie auf Treiber aktualisieren und dann auf Durchsuchen.

- Navigieren Sie zu dem Ordner Arduino Software download und wählen Sie die Datei "arduino.inf" aus.

Als Nächstes öffnen Sie die Datei count.ino, die Sie unter evolition/Software/ArduinoUno finden werden, in der Arduino IDE und klicken dann auf Hochladen.

## Tof-Sensor

Der Tof-Sensor benötigt ebenfalls die Arduino IDE. Haben Sie bereits das Wemos D1 mini Board verfügbar, können Sie mit dem nächsten Schritt weitermachen. Ansonsten befolgen Sie diese Schritt-Anleitung:

- Öffnen Sie die Arduino IDE. Gehen Sie auf "File" und anschließend auf "Preferences".

- Geben Sie unter "Additional Boards Manager URLs" folgende URL ein: http://arduino.esp8266.com/stable/package_esp8266com_index.json

- Klicken Sie auf OK.

- Öffnen Sie "Tools" -> "Board" -> "Boards Manager"

- Suchen Sie nach "esp8266" und installieren Sie das ESP8266 Community Package.

Sollten Sie anschließend noch nicht auf das Board zugreifen können, installieren Sie den entsprechend den Treiber wie in [ArduinoUno](#arduinouno).


In evolition/WeimosD1Mini finden Sie den Ordner PeopleCounterFirmware, welchen Sie mit allen seinen Datein herunterlanden sollten, da dieser Ordner für die weiteren Schritte in der Arduino IDE notwendig ist

Öffnen sie nun die PeopleCounterFirmware.ino, die sich in dem PeopleCounterFirmware Ordner befindet. Hierbei sollten sich auch alle anderen Dateien in der Arduino IDE öffnen. Ist dies nicht der Fall, öffnen Sie händisch die `Config.h`. Hier müssen Sie "name" und "password" mit Ihren Internetzugangsdaten ersetzen.

Zusätzlich können Sie `DEFAULT_PEOPLE_LIMIT` verändern. Diese beschreibt die maximale Raumkapazität und liegt aktuell bei 50.

Wenn Sie bemerken, dass der Sensor in die falsche Richtung zählt, kommentieren Sie den Befehl `#define MOUNTED_INSIDE` aus.

## RaspberryPi
Zuerst sollte sichergestellt werden, dass Python3 auf dem Raspberry Pi installiert ist, da die Skripte, die die Siebensegmentanzeige und die Bildanzeige, steuern, in Python geschrieben sind.

Für das Raspbian OS können folgende Befehle genutzt werden:
```
sudo apt update
sudo apt upgrade
sudo apt install python3
```
Für andere Betriebssysteme sollten Sie am besten die [offizielle Webseite](https://www.python.org/downloads) konsultieren.

Die nächsten Schritte sind wie folgt:
- Das Repository klonen: `git clone https://github.com/cbm-instructions/evolition.git`
- In den Ordner für den Raspberry Pi navigieren: `cd Software/RaspberryPi`
- Die Abhängigkeiten installieren: `sudo -H pip install -r requirements.txt`
- Sicherstellen, dass für die Skripte die Ausführungsrechte vorhanden sind: `chmod a+x ` mit allen Python Skripten benutzen 
- Die Skripte automatisieren:
    (Wir empfehlen vorher einmal die Skripte getAllTables.py, getExamTables.py und getDayList.py ausgeführt zu haben, damit, wenn Sie die Anzeige mitten im Semester installieren möchten, die Anzeige mit den aktuellen Plänen arbeitet)
    `crontab -e`
    
    Wählen Sie den Command-Line Editor aus, der Ihnen am besten gefällt, und schreiben Sie in der Datei die folgenden Zeilen:
        
        
        # Minute, Stunde, Tag, Monat, Wochentag, Interpreter, Pfad
        # Überprüfung zu jedem Blockanfang (Vorlesungen & Klausuren) ob sich das Bild verändern soll
        * 8 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        15 8 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        45 9 * * * /usr/bin/python3pfad zu evolition/Software/RaspberryPi/roomcheck.py
        45 10 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        * 12 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        15 13 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        40 13 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        20 15 * * * /usr/bin/python3pfad zu evolition/Software/RaspberryPi/roomcheck.py
        45 15 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py
        * 17 * * * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomcheck.py

        # Überprüfung der Stundenpläne jeden Dienstag im ersten Semestermonat
        * * * 9 2 /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/getAllTables.py
        * * * 3 2 /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/getAllTables.py

        # Überpüfung der Prüfungspläne im vorletzten Semestermonat
        * * 1 1 * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/getExamTables.py
        * * 10 1 * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/getExamTables.py
        * * 1 7 * /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/getExamTables.py
        * * 10 7 * /usr/bin/python3 Pfad zu evolition/Software/RaspberryPi/getExamTables.py

        @reboot /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomCheck.py
        

    Da die Skripte LightsaberNumber.py sudo Rechte benötigt und das Skript roomCheck.py LightsaberNumber.py importiert, öffnen Sie als Nächstes das crontab von root: `sudo crontab -e`
    
    ```
    @reboot /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/roomCheck.py
    @reboot /usr/bin/python3 pfad zu evolition/Software/RaspberryPi/LightsaberNumber.py
    ```

Um die Anzeige nutzen zu können, müssen Sie sicherstellen, dass sich der Raspberry Pi und der Weimos D1 Mini im selben Netz befinden. Je nach Netz kann sich die URL des Weimos D1 Mini ändern, weshalb Sie diese gegebenenfalls in der config.py Datei anpassen müssen.

Sollten Sie außerdem die Anzeige für einen anderen Raum verwenden wollen, müssen Sie die Raumnummer und die entsprechende maximale Sitzplatzanzahl ebenso in der config.py Datei verändern. Nach einer solchen Raumänderung empfiehlt es sich, die Anzeige neu zu starten, damit sich die Tagesliste direkt anpasst