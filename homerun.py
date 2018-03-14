#/usr/bin/env python
import subprocess, time, os, argparse, schedule
from os.path import abspath, dirname, join

if 'x86_64' in os.uname():
    BROWSER = 'google-chrome'
    BROWSER_KILL = 'chrome'
else:
    print("Running on RPi")
    BROWSER = 'chromium-browser'  # RPi        
    BROWSER_KILL = 'chromium'

def start_chrome(debug):
    print("Starting chrome")
    html_path = abspath(join(dirname(__file__), './html/test.html'))
    cmd = [BROWSER, html_path, '--noerrdialogs', '--incognito', '--disable-translate'] # '--ignore-certificate-errors'
    if not debug:
        cmd.append('--kiosk')
    subprocess.Popen(cmd)

def turn_off_chrome():
    print("Turns of chrome")
    cmd = ['pkill', BROWSER_KILL]
    subprocess.call(cmd)
    print("Done")
	
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--debugOff', action="store_false")
    args = parser.parse_args()
    
    if args.debugOff:
        print("Starting in debug mode")
    start_chrome(args.debugOff)
    time.sleep(25)
    turn_off_chrome()
	

#* Create a script to replace the standard desktop environment.
#```
## ~/fullscreen.sh
#unclutter &
#matchbox-window-manager &

#sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium-browser Default/Preferences
