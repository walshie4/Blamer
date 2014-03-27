Blamer
======

Automagically find out what Symbolicate blames for the recent crashes on your jailbroken iDevice

**Download the source [here](https://github.com/walshie4/Blamer/archive/master.zip)**

##Pre-req's
* Symbolicate
    * To install it open Cydia, and go to the Manage tab. Tap the settings button in the top right corner,
    and select user type 'Developer'. After that all you should have to do is search for the Symbolicate package
    and install it. Once installed you can change your user type back to whatever you had it set as before.

* Python
    * To install Python on your jailbroken iDevice simply open MobileTerminal or ssh into your iDevice and run
    `apt-get install python` and answer y to any prompts about installing new packages.

##How to use
* First download the source of this project from one of the links on the project page to your iDevice, then extract the source to
any directory

* To use this script simply run `python blamer.py`. A blame.txt file will be generated with
the summary of symbolicate's blame of all found .plist files in your `/var/mobile/Library/Logs/CrashReporter` dir.

**OR**

* You can install through Cydia, just search for `python`

For a video walkthough go [here](http://youtu.be/IoeE5im7Lfo).

###How to use with Activate Command and Activate Link
Thanks to Reddit user [qazaqazaqazaq](http://www.reddit.com/user/qazaqazaqazaq) for helping fix the issues for setup with
Activate Command.

For a video walkthrough on how to set this up, and a recap on installing directly to your iDevice look 
[here](http://youtu.be/Vtavb3LbHvY).

* First download the latest source, and install Activate Command (and Activate Link if you would
like to automate opening the blame.txt file) from Cydia.

* Next place the downloaded script somewhere mobile user has read/write access. For simplicity in finding it I would
suggest making a directory inside your `/usr/bin/` dir called Blamer.

* After that open settings and go to the Activate Command panel. For the command enter 
`python [path-to-blamer-source]/blamer.py` so if you used `/usr/bin/` as suggested above your command would be
`python /usr/bin/Blamer/blamer.py`

* If you would like to automate the opening of the `blame.txt` file install Cydia package `Activate Link` and use the URL
`ifile:///var/mobile/Library/Logs/CrashReporter/blame.txt`

##Note
* Everytime you sync your iDevice all the crash logs will be deleted

* The blame provided by Symbolicate is only a guess of which package caused the crash, and is not a definite
cause.
