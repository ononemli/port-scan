# author: ononemli

from pyfiglet import Figlet
import socket
import ipaddress

portscanner = Figlet(font='standard')
print(portscanner.renderText('Port Scanner'))

ononemli = Figlet(font='doom')
print(ononemli.renderText('ononemli'))

scancomplete = Figlet(font='digital')

destinationip = input("Destination IP Address: ")
X = input("Starting Port Number: ")
X = int(X)
Y = input("End Port Number: ")
Y = int(Y)
portvalues = range(X, Y+1)
timeout = input("Timeout Period -milliseconds-: ")
timeout = float(timeout)

try:
    ipnetwork = ipaddress.ip_network(destinationip, strict=False)
except:
    print("Invalid IP Address")
    input('\n''Press enter to exit')
    if input: exit()

for ip in ipnetwork:
    print(X, "to", Y, "/", "Scanning ports at destination address", "/", ip)
    for port in portvalues:
        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockt.settimeout(timeout)
        code = sockt.connect_ex((str(ip), port))
        sockt.close()
        if code == 0:
            print("PORT", port, "----- OPEN -----")
        else:
            print("Port", port, "closed")

print(scancomplete.renderText('Scan Complete'))

input('\n''Press enter to exit')
if input: exit()