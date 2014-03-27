#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os
location = "/var/mobile/Library/Logs/CrashReporter/"
os.system("touch " + location + "blame.txt")
os.system("touch " + location + "temp.txt")
path = "/var/mobile/Library/Logs/CrashReporter/"
crashes = dict() #dictionary to hold all found crashes
for file in os.listdir(path):
    if file.endswith(".plist"):
        print("now reading: " + file)
        command = "symbolicate " + path + file + " > " + location + "temp.txt"
        os.system(command)
        recording = False #true when writing to output file, false otherwise
        output = open(location + "temp.txt")
        for line in output:
            line = "".join(line.rstrip().split())
            if recording:
                for word in line.split(' '):
                    if word.startswith("<array><string>"):
                        word = word[15:] #cut off XML tags at beginning
                        word = word.split('<')[0] #grab only the path
                        if word in crashes: #already been found
                            crashes[word] += 1 #increment its count
                        else:
                            crashes[word] = 1 #add to dict
            if line == "<key>blame</key>": #starting of what we're looking for
                print("recording")
                recording = True
            if line == "<key>symbolicated</key>":
                print("stopping")
                recording = False
for element in sorted(crashes, key=crashes.get, reverse=True):
    open(location + "blame.txt","a").write(element + " - " + str(crashes[element]) + "\n")
os.system("rm " + location + "temp.txt")
