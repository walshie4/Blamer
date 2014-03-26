Blamer
======

Automagically find out what Symbolicate blames for the recent crashes on your jailbroken iDevice

##Pre-req's
* Symbolicate
    * To install it open Cydia, and go to the Manage tab. Tap the settings button in the top right corner,
    and select user type 'Developer'. After that all you should have to do is search for the Symbolicate package
    and install it. Once installed you can change your user type back to whatever you had it set as before.

* Python
    * To install Python on your jailbroken iDevice simply open MobileTerminal or ssh into your iDevice and run
    `apt-get install python` and answer y to any prompts about installing new packages.

##How to use
* To use this script simply run `python blamer.py` on your jailbroken iDevice. A blame.txt file will be generated with
the summary of symbolicate's blame of all found .plist files in your /var/mobile/Library/Logs/CrashReporter dir.

##Note
* Everytime you sync your iDevice all the crash logs will be deleted

* The blame provided by Symbolicate is only a guess of which package caused the crash, and is not a definite
cause.
