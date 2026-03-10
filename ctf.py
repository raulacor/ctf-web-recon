import os
#pip install pynput
from pynput.keyboard import Key, Controller 
#https://pynput.readthedocs.io/en/latest/

keyboard = Controller()

os.system("pwd=$(pwd)") #needed for eyewitness

target = input("Input target: ")

print("Creating folders. . .")
os.system("mkdir thirdlevels")
os.system("mkdir scans")
os.system("mkdir eyewitness")

print("Running sublist3r. . .")
os.system(f"sublist3r -d {target} -o final.txt")
os.system(f"echo {target} >> final.txt")

print("Compiling third-level domains. . .")
os.system("cat final.txt | grep -Po '(\w+\.\)w+\.\w+)$' | sort -u >> third-level.txt")
##https://regex101.com

print("Gathering full third-level domains. . .")
os.system("subfinder -dL third-level.txt -o thirdlevels/domain.txt")
os.system("cat thirdlevels/domain.txt | sort -u >> final.txt")

print("Searching for alive subdomains. . .")
os.system("cat final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' > probed.txt") 
#by limiting the port we get to only find the subdomains that actually resolve on the wifi router.

print("Scanning for open ports. . .")
os.system("namp -iL probed.txt -T5 -oA scans/scanned.txt")

print("Running eyewitness. . .")
os.system(f"eyewitness -f $pwd/probed.txt -d {target} --all-protocols")
os.system(f"mv /usr/share/eyewitness/{target} eyewitness/{target}")