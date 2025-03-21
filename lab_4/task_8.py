import os
import platform

print("Username:", os.environ.get('USERNAME'))
print("Profile:", os.environ.get('LOGNAME'))
print("Home dir: ", os.environ.get('HOME'))
print("OS: ", platform.system())
print("System language: ", os.environ.get('LANG'))