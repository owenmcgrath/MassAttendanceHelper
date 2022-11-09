# MassAttendanceHelper
Compiled code for a QR code mass attendance tool for parish religious ed students to meet their mass attendance requirements

## BatchQrCodeGenerator
Imports a csv file of students by grade number and name and generates a special formatted qr code for each student

Row 1 expected format

| | A | B | C |
|---|---|---|---|
|1| Last Name: | First Name: | Grade: |
|2| Aquinas | Thomas | 9 |
|3| Avila | Teresa | 10 |
|4| Lisieux | Therese | 11 |

It will perform text cleanup on each of the rows, optionally spit out a new file with the cleaned up names, and also generate QR codes corresponding to each entry

### Setup
```
pip install pyqrcode
pip install pypng
pip install easygui
```

### Run 
```
python BatchQrCodeGenerator.py
```
Select "ExampleInput.xlsx" to run an example

## QR Code Scanning Instructions

1. Install the app from the link above
2. Before you first scan:
   1. Tap on the three horizontal lines in the top left corner of the screen
   2. Tap on "History"
   3. Tap on the three dots on the top right corner of the screen 
   4. Tap the trash icon.
   5. The app will prompt "Are you sure you want to clear history?" Tap yes
3. Tap on the three horizontal lines in the top left corner of the screen
4. Tap "Scan"
5. Scan each student, return to the scan view after each scan
6. After you have scanned all the students
   1. Tap on the three horizontal lines in the top left corner of the screen
   2. Tap on "History"
   3. Tap on the three dots on the top right corner of the screen
   4.  Tap on the "CSV Down Arrow" option
   5.  Tap on the share icon (3 dots connected by two lines)
   6.  Tap on the email option (or share the file by whatever preferred means)

## Attendence Tracker
- Attendence Sheet: Enter a row for each attending. Can be copy and pasted from QR scanned CSV's and minor post processing from above. 
- Tally Sheet: Automatically keeps tally of each entry from the attendence sheet
