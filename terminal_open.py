import os
import subprocess

"""
-----
"""

#subprocess.call(['gnome-terminal -- "ls"'], shell=True)

subprocess.Popen('')
subprocess.call(["ls"], shell=True)

#os.system("ls")
#os.system("gnome-terminal -- 'bash -c \""+command+";bash\"'")