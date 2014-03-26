#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os, time
os.system("touch blame.txt")
path = "/var/mobile/Library/Logs/CrashReporter/"
for file in os.listdir():
    if file.endswith(".plist"):
        #time.sleep(5)
        print("now reading: " + file)
        command = "symbolicate " + path + file + " > temp.txt"
        os.system(command)
        recording = False #true when writing to output file, false otherwise
        output = open("temp.txt")
        for line in output:
            print(line)
            line = "".join(line.rstrip.split)
            if recording:
                open("blame.txt","a").write(line)
            if line == "<key>blame</key>": #starting of what we're looking for
                print("recording")
                recording = True
            if line == "<key>symbolicated</key>":
                print("stopping")
                recording = False
os.system("rm temp.txt")
