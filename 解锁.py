import os
import sys

user = os.environ.get('USERNAME') 
startup_path = fr'C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
os.remove(startup_path + '\尝试.exe')
