#!/usr/local/bin/python3

from sys import stdin
import nltk
import string
import re

def finding_date(line):
### Catch pure number
    number = re.compile(r'\b[on\s+]*\d{1,2}\/\d{1,2}\/\d{2,4}',re.IGNORECASE)
    result_n = number.findall(line)
    for i in range(len(result_n)):
        print(result_n[i])
### Catch day and mdy
    #how to do this?  Friday, September 26, 2008 without repetition.
### Catch Weekend and Weekday
    #day and dates
    dd = re.compile(r"((?:\bMonday[s]*\b|\bTuesday[s]*\b|\bWednesday[s]*\b|\bThursday[s]*\b|\bFriday[s]*\b|\bSaturday[s]*\b|\bSunday[s]*\b)(?:\s+the\s+(?:\b\d{1,2}\D{2}\b|\b\w+\b))?)")
    result_dd = dd.findall(line)
    for i in range(len(result_dd)):
        print(result_dd[i])
### Catch Months
    # on month day (year) have bug deal with british format
    mdy = re.compile(r"((?:(?:\bJan(?:uary)?|\bFeb(?:ruary)?|\bMar(?:ch)?|\bApr(?i:il)?|\bMay|\bJun(?:e)?|\bJul(?:y)?|\bAug(?:ust)?|\bSep(?:tember)?|\bOct(?:ober)?|\bNov(?:ember)?|\bDec(?:ember)?)\.?\s+(?:\d{1,2}\w{0,2}|\w+\b\s+\w+))(?:\,+\s+\d{2,4})?)")
    result_mdy = mdy.findall(line)
    for i in range(len(result_mdy)):
        print(result_mdy[i])
    #the xx of Month
    dm = re.compile(r"\bthe\b\s+(?:d{1,2}|\w+)\s+\bof\s+(?:\bJan(?:uary)?|\bFeb(?:ruary)?|\bMar(?:ch)?|\bApr(?i:il)?|\bMay|\bJun(?:e)?|\bJul(?:y)?|\bAug(?:ust)?|\bSep(?:tember)?|\bOct(?:ober)?|\bNov(?:ember)?|\bDec(?:ember)?)")
    result_dm = dm.findall(line)
    for i in range(len(result_dm)):
        print(result_dm[i])

### Catch Holidays
    holidays = re.compile(r"((?:\bChristmas\b|\bThanksgiving\b|\bMother\'s\b|\bEaster\b|\bIndependence\b|\bFather\'s\b|\bHalloween\b|\bValentine\'s\b|\bSaint\s+\bPatrick\'s\b|\bNew\s+\bYear\'s\b|\bLabor\b)(?:\s+(?:\bDay|\bEve\b))?)")    
    result_holi = holidays.findall(line)
    for i in range(len(result_holi)):
        print(result_holi[i])    

### Test Section
    test = re.compile(r"\*\*\*\*[0-9]\*\*\*\*")
    result = test.findall(line)
    for i in range(len(result)):
        print(result)
         
if __name__ == "__main__":
    for input_line in stdin:
        if input_line != "":
        #print(word)
    #test="Design and write a program that recognizes simple date expressions like: January 15, 2014, the 21st of December, 01/15/2014 (only the American notation), Monday, Monday the 23rd, Christmas, Labor Day" 
            finding_date(input_line)
    #print("There are 7 answers")
