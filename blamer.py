#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os
os.system("/var/mobile/Library/Logs/CrashReporter/blame.txt")
for file in os.listdir("/var/mobile/Library/Logs/CrashReporter"):
    if file.endswith(".plist"):
        command = subprocess.Popen("symbolicate " + file, stdout=subprocess.PIPE)
        output = command.stdout.read()
        contents = open(ouput)
        recording = False #true when writing to output file, false otherwise
        for line in contents:
            if recording:
                os.system("echo " + line + " >> blame.txt") #write to output file
            if line == "<key>blame</key>": #starting of what we're looking for
                recording = True
            if line == "<key>symbolicated</key>":
                recording = False
