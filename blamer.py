#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os, time
os.system("touch blame.txt")
os.system("touch prelim.txt")
path = "/var/mobile/Library/Logs/CrashReporter/"
for file in os.listdir(path):
    if file.endswith(".plist"):
        print("now reading: " + file)
        command = "symbolicate " + path + file + " > temp.txt"
        os.system(command)
        recording = False #true when writing to output file, false otherwise
        output = open("temp.txt")
        for line in output:
            line = "".join(line.rstrip().split())
            if recording:
                open("prelim.txt","a").write(line + "\n")
            if line == "<key>blame</key>": #starting of what we're looking for
                print("recording")
                recording = True
            if line == "<key>symbolicated</key>":
                print("stopping")
                recording = False
contents = open("prelim.txt")
for line in contents:
    for word in line.split(' '):
        if word.startswith("<array><string>"):
            open("blame.txt","a").write(word[15:])
os.system("rm temp.txt")
os.system("rm prelim.txt")
