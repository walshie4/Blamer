#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os
os.system("touch blame.txt")
for file in os.listdir("/var/mobile/Library/Logs/CrashReporter"):
    if file.endswith(".plist"):
        output = os.popen("symbolicate " + file).read()
        recording = False #true when writing to output file, false otherwise
        for line in output:
            line = "".join(line.rstrip.split)
            if recording:
                open("blame.txt","a").write(line)
            if line == "<key>blame</key>": #starting of what we're looking for
                print("recording")
                recording = True
            if line == "<key>symbolicated</key>":
                print("stopping")
                recording = False
