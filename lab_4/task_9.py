import os
import platform
import distro

print("Home dir: ", os.environ.get('HOME'))
print("Platform: ", platform.platform())
print("OS: ", platform.system())
print("Processor: ", platform.processor())
print("Distro:\n\tID: ", distro.id())
print("\tName: ", distro.name())
print("\tVersion: ", distro.version())

