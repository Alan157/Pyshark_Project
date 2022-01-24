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
while True:  # A loop to capture and validate the input of the interface variable
    network_interface = input("\nPlease type the network interface you wish to use:")
    if network_interface == "":
        print("\nMust enter a network interface!")
    else:
        break


filters = input("\nPlease type with filters you would like to use(leave empty for all traffic):")  # An input for the filters variable

while True:  # A loop to capture and validate the input of the summaries variable
    summaries = input("\nDisplay packets as summaries?(y/n):")
    if summaries == "y" or summaries == "n":
        if summaries == "y":
            summaries = True
        else:
            summaries = False
        break
    print("\nMust enter a valid option!")

while True:  # A loop to capture and validate the input of the path variable

    path = input("\nPlease type the path to which the logs will be saved:")
    if path == "":
        "\nMust enter a valid path!"
    else:
        break

print("Starting packet sniff and display")
capture = pyshark.LiveCapture(interface=network_interface, only_summaries=summaries, bpf_filter=filters)  # starting the capture

output = open(path, "w")  # Opens a file for writing logs

for packet in capture.sniff_continuously():  # A loop for printing and writing the packets
    print(packet)  # Printing the packet
    output.write(str(packet))  # writing the packet to the file for logging
    output.write("\n")

output.close()


