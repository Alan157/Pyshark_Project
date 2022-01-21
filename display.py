import sys
sys.path.append('/home/kali/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/')  # allows terminal exec
import pyshark


def capture_live_packets(network_interface):
    capture = pyshark.LiveCapture(interface=network_interface)
    for raw_packet in capture.sniff_continuously():
        print(raw_packet)


"""
----Main program that will call the other scripts----
1)* ###DONE### Monitors the network and capture relevant packets form unknown IPs (i.e excluding SOC IPs)
  * ###DONE### Writes the relevant packets to a file (a simple txt file)
  * ###DONE### Gives the option between capturing full packets and summaries (only_summaries = True/False)
2)Backs up local machine logs every 2 or so minutes (/var/log directory)

TO CHECK:
*How to run a python script in a new CLI
* ###DONE### Why running .py script didnt work through CLI (import error)
*Close a CLI/running script
*

"""
print("Welcome to the live network traffic feed:")
network_interface = input("\nPlease type the network interface you wish to use:")  # Create a try for the network adapter
filters = input("\nPlease type with filters you would like to use(leave empty for all traffic):")
while True:
    summaries = input("\nDisplay packets as summaries?(y/n):")
    if summaries == "y" or summaries == "n":
        if summaries == "y":
            summaries = True
        else:
            summaries = False
        break

file_name = input("\nPlease type the file name to which the logs will be saved:")

print("Starting packet sniff and display")
capture = pyshark.LiveCapture(interface=network_interface, only_summaries=summaries, bpf_filter=filters)

output = open("/home/kali/Desktop/" + file_name + ".txt", "w")

for packet in capture.sniff_continuously():
    print(packet)
    output.write(str(packet))
    output.write("\n")

output.close()


