import os
"""
NOT WORKING!
"""

command = "ls"
os.system("gnome-terminal -- 'ls'")
os.system("gnome-terminal -- 'bash -c \""+command+";bash\"'")