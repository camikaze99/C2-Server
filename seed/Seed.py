import subprocess
import sys

#help("modules")

#Install the required packages to run the rest of the script.
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "platform"])

#help("modules")
#import requests

#url = "https://google.com/"
#r =requests.get(url)
#print(r)


#Read system information.
import platform
print(platform.uname())
print("")
print(platform.machine())
print(platform.version())
print(platform.platform())
print(platform.system())
print(platform.processor())
