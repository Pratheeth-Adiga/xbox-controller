import time
import ctypes 
from ctypes import wintypes
import psutil

# Code.exe, explorer.exe, brave.exe, EpicGamesLauncher.exe, steam.exe, vlc.exe
# Acrobat.exe, Discord.exe, ApplicationFrameHost.exe
time.sleep(5)
user32 = ctypes.windll.user32
h_wnd = user32.GetForegroundWindow()
pid = wintypes.DWORD()
user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
print(psutil.Process(pid.value).name())

