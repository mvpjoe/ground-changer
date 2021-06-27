import ctypes
import requests
import shutil
import platform
import subprocess
import os

# Command for changing background on mac
cmd = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

# Get image from Github Pages json page
r = requests.get('https://mvpjoe.github.io/ground-changer/json_data.json').json()
url = r['urls']['background']
print(url)


# Download the image
r = requests.get(url, stream=True)
r.raw.decode_content = True

# Open a local file with wb ( write binary ) permission.
with open('image.png','wb') as f:
	shutil.copyfileobj(r.raw, f)


# Set image as desktop background
if platform.system() == 'Darwin':
	subprocess.Popen(cmd%"image.png", shell=True)
	subprocess.call(["killall Dock"], shell=True)
if platform.system() == 'Windows':
	path = os.getcwd()+'\\image.png'
	ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
