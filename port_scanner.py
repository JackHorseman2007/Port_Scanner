import socket #Imports the socket library for network connections
import sys #Imports the sys library for command line arguments
from datetime import datetime #Imports the datetime library for time tracking

print("Welcome to the Port Scanner!") #Outputs a welcome message

if len(sys.argv) == 2: #Checks if the user has provided exactly one argument
    target = socket.gethostbyname(sys.argv[1]) #Converts the target domain to an IP address by looking up it's DNS
else:
    print("Invalid amount of arguments") #Error message for incorrect number of arguments

print("Scanning target: " + str(target)) #Outputs the target being scanned
print("Time scan started:" + str(datetime.now())) #Outputs the current time when the scan started

try:
    for port in range(1,65535): #Scans through all ports between 1 to 65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates a new TCP socket
        socket.setdefaulttimeout(1) #Sets a default timeout of 1 second for the socket connection

        result = sock.connect_ex((target, port)) #Attempts to connect to the target on the specified port
        if result == 0: #If the connection was successful
            print("Port {}: Open".format(port)) #Outputs that the port is open
        sock.close() #Closes the socket connection

except KeyboardInterrupt: #Detects if the user interrupts the scan with Ctrl+C
    print("\nExited.") #Outputs a message indicating the scan was exited
    sys.exit() #Exits the program
except socket.gaierror: #Detects if the hostname could not be resolved
    print("\n Hostname could not be resolved.") #Outputs an error message if the hostname could not be resolved
    sys.exit() #Exits the program
except socket.error: #Detects if there was a socket error
    print("\nCould not connect to the server.") #Outputs an error message if the connection failed
    sys.exit() #Exits the program