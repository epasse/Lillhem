#/usr/bin/env python
import subprocess, time
from os.path import abspath, dirname, join

def start_chrome():
	print("Starting chrome")
	html_path = abspath(join(dirname(__file__), './html/test.html'))
	cmd = ['chromium-browser', html_path]
	subprocess.Popen(cmd)

def turn_off_chrome():
	print("Turns of chrome")
	cmd = ['pkill', 'chromium']
	subprocess.call(cmd)
	print("Done")
	
if __name__ == "__main__":
	print("Starting")
	start_chrome()
	time.sleep(25)
	turn_off_chrome()
	


