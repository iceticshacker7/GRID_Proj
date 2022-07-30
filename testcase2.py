import webbrowser
from os import walk
import zipfile
import time
import os

link = input("Pease enter Your Link:")     #https://github.com/iceticshacker7/PythonCodes
webbrowser.open(f'{link}/archive/refs/heads/main.zip') 
webbrowser.open(f'{link}/archive/refs/heads/master.zip') 
time.sleep(14)
with zipfile.ZipFile("C:\\Users\\hp\Downloads\PythonCodes-main.zip", 'r') as zip_ref:
    zip_ref.extractall("C:\\Users\\hp\Downloads")
# folder path
dir_path = r'C:\\Users\\hp\Downloads\\PythonCodes-master/'
dir_path = r'C:\\Users\\hp\Downloads\\PythonCodes-main/'

# list to store files name
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
substring = ".java"
substring2 = ".py"
substring3 = ".class"
java = []
pyth = []
source = []
other = []


def comp(t):
   
    if substring in t:
        java.append(t)
        print(t) 
    elif substring2 in t:
        pyth.append(t)
        print(t)
        os.system(f"cmd /c python3 -m pyt C:\\Users\\hp\Downloads\PythonCodes-main\\{t}")
    elif substring3 in t:
        source.append(t)
        print(t)
    else:
         other.append(t)
         print(t)




for i in range(0, len(res)):
    fullstring = res[i]
    comp(res[i])
   
str = ('``` \n'
       '\n\nTypes of Files present in Repo: \n\n'
       # this line is the part I need help with: list comprehension for the 2 lists to output the values as shown below
       '```')
print(str)
res = "\n".join("{}\t\t{}".format(x, y) for x, y in zip(java, source, pyth))
print(res)
