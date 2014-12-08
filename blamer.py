#!/usr/bin/env python
#Written by: Adam Walsh
#Written on 3/25/14

#A simple script to help jailbroken iDevice users find out what
#Symbolicate finds as the blame for recent crashes
import os
location = "/var/mobile/Library/Logs/CrashReporter/"
if os.path.isfile(location + "blame.txt"):
    os.system("echo '' > " + location + "blame.txt") #empty the blame.txt file of old results
os.system("touch " + location + "blame.txt")
os.system("touch " + location + "temp.txt")
path = "/var/mobile/Library/Logs/CrashReporter/"
crashes = dict() #dictionary to hold all found crashes
for file in os.listdir(path):
    if file.endswith(".ips"):
        print("now reading: " + file)
        command = "symbolicate --print-blame " + path + file + " > " + location + "temp.txt"
        os.system(command)
        recording = False #true when writing to output file, false otherwise
        output = open(location + "temp.txt")
        for line in output:
            if line.startswith("/"):#is a path
                parts = line.split("/")
                word = parts[len(parts)-1]#cut out name
                if word in crashes: #already been found
                    crashes[word] += 1 #increment its count
                else:
                    crashes[word] = 1 #add to dict
for element in sorted(crashes, key=crashes.get, reverse=True):
    open(location + "blame.txt","a").write(element + " - " + str(crashes[element]) + "\n")
os.system("rm " + location + "temp.txt")

