#/usr/bin/env python
import subprocess, time, os
from os.path import abspath, dirname, join

DEBUG = True

if 'x86_64' in os.uname():
    BROWSER = 'google-chrome'
    BROWSER_KILL = 'chrome'
else: 
    BROWSER = 'chromium-browser'  # RPi        
    BROWSER_KILL = 'chromium'

def start_chrome():
    print("Starting chrome")
    html_path = abspath(join(dirname(__file__), './html/test.html'))
    cmd = [BROWSER, html_path, '--noerrdialogs', '--incognito', '--disable-translate'] # '--ignore-certificate-errors'
    if not DEBUG:
        cmd.append('--kiosk')
    subprocess.Popen(cmd)

def turn_off_chrome():
    print("Turns of chrome")
    cmd = ['pkill', BROWSER_KILL]
    subprocess.call(cmd)
    print("Done")
	
if __name__ == "__main__":
    print("Starting")
    start_chrome()
    time.sleep(25)
    turn_off_chrome()
	

#* Create a script to replace the standard desktop environment.
#```
## ~/fullscreen.sh
#unclutter &
#matchbox-window-manager &

#sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium-browser Default/Preferences
