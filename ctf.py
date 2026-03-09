import os
#pip install pynput
from pynput.keyboard import Key, Controller 
#https://pynput.readthedocs.io/en/latest/

keyboard = Controller()

target = input("Input target: ")

os.system("mkdir thirdlevels")

print("Running sublist3r. . .")
os.system(f"sublist3r -d {target} -o final.txt")
os.system(f"echo {target} >> final.txt")

print("Compiling third-level domains. . .")
os.system("cat final.txt | grep -Po '(\w+\.\)w+\.\w+)$' | sort -u >> third-level.txt")

print("Gathering full third-level domains. . .")
os.system("subfinder -dL third-level.txt -o thirdlevels/domain.txt")
os.system("cat thirdlevels/domain.txt | sort -u >> final.txt")
