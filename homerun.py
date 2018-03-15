#/usr/bin/env python
import subprocess, time, os, sys, argparse, schedule
from os.path import abspath, dirname, join

from threading import Thread

if sys.version_info >= (3, 0): # python 3
    import tkinter as Tkinter
    from tkinter import messagebox
else:
    import Tkinter
    import tkMessageBox as messagebox

if 'x86_64' in os.uname():
    BROWSER = 'google-chrome'
    BROWSER_KILL = 'chrome'
else:
    print("Running on RPi")
    BROWSER = 'chromium-browser'  # RPi        
    BROWSER_KILL = 'chromium'

def start_chrome(html_path, debug):
    print("Starting chrome")
    cmd = [BROWSER, html_path, '--noerrdialogs', '--incognito', '--disable-translate'] # '--ignore-certificate-errors'
    if not debug:
        cmd.append('--kiosk')
    subprocess.Popen(cmd)

def turn_off_chrome():
    cmd = ['pkill', BROWSER_KILL]
    subprocess.call(cmd)
    print("Turned of chrome")

def job(html, debug):
    start_chrome(html, debug)
    time.sleep(10)
    turn_off_chrome()

def halt_startup(exit_app):
    root = Tkinter.Tk()
    root.withdraw()
    exit_app[0] = messagebox.askyesno(__file__,"The application is about to start, would you like to stop it?")
    root.destroy()

def start_up_delay():
    exit_app = [False]*1 # Use list to "return by reference"
    tread = Thread(target=halt_startup, args=(exit_app,))
    tread.start()
    start = time.time()
    timeout = False
    while not exit_app[0] and tread.isAlive() and not timeout:
        timeout = (time.time() - start) > 5
        time.sleep(1)
        print(time.time())

    if exit_app[0]:
        exit("Application halted by user..")
    elif timeout:
        exit_app[0] = True
        print("Time out")
    tread.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debugOff', action="store_false")
    args = parser.parse_args()

    start_up_delay()

    if args.debugOff:
        print("Starting in debug mode")
    
    html = abspath(join(dirname(__file__), './html/train_yr.html'))
    schedule.every(30).seconds.do(job, html, args.debugOff)

    while True:
        schedule.run_pending()
        time.sleep(1)
	

#* Create a script to replace the standard desktop environment.
#```
## ~/fullscreen.sh
#unclutter &
#matchbox-window-manager &

#sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium-browser Default/Preferences
