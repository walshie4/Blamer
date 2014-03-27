#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent springboard crashes
import os, time
os.system("touch blame.txt")
os.system("touch temp.txt")
path = "/var/mobile/Library/Logs/CrashReporter/"
crashes = dict() #dictionary to hold all found crashes
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
    open("blame.txt","a").write(element + " - " + str(crashes[element]) + "\n")
os.system("rm temp.txt")
