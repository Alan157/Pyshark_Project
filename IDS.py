import sys
sys.path.append('/home/kali/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/')  # allows terminal execution
import pyshark


"""
This program uses Pyshark to monitor the traffic on a specified network interface
and writes the output to a text file for logging.
"""
print("Welcome to the live network traffic feed:")
while True:  # A loop to capture and validate the input of the interface variable
    network_interface = input("\nPlease type the network interface you wish to use:")
    if network_interface == "":
        print("\nMust enter a network interface!")
    else:
        break


filters = input("\nPlease type with filters you would like to use(leave empty for all traffic):")  # An input for the filters variable(bpf filter)

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

print("\n------------Starting packet sniff, display and logging------------")
capture = pyshark.LiveCapture(interface=network_interface, only_summaries=summaries, bpf_filter=filters)  # starting the capture

output = open(path, "w")  # Opens a file for writing logs

for packet in capture.sniff_continuously():  # A loop for printing and writing the packets
    print(packet)  # Printing the packet
    output.write(str(packet))  # writing the packet to the file for logging
    output.write("\n")

output.close()


