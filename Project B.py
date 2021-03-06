#Project B By Malcolm  01/17/2021
#Host IP address 169.254.22.7 / 10.0.0.1
#Scan beginning at:  01/21/2021 15:06:40
#Scan completed at:  01/21/2021 15:07:21
#Total scan time:  40.92 seconds.
#Discovered Port "Port 53 is open"
#Import required modules
import socket
import subprocess
from datetime import datetime, time
import time

#
def portscan(host,port_num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port_num)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False
    finally:
        s.close()

File = open("ScanResults", "w")

host = input("Enter host IP address: ")
MinRange = int(input('Enter starting port number: '))
MaxRange = int(input('Enter ending port number: '))
PortCheckRange = range(MinRange, MaxRange+1, 1)

now = datetime.now()

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
start = time.time()

status=subprocess.getstatusoutput("ping -n 1 " + host)
result=str(status)

if (result.startswith("(0")):
    print("Host is responding. Begin with port scan.")
    print("Scan beginning at: ", dt_string)
    print("Im on it Coach")

    RespTup = [host, "trying to respond. Starting scan at", dt_string, "\n"]
    RespOut = ' '.join(RespTup)
    File.write(RespOut)
else:
    print("Host is not responding. Terminating scan")
    RespTup = [host, "is not responding. Scan Terminated at", dt_string,"\n"]

    RespOut = ' '.join(RespTup)
    File.write(RespOut)
    File.close()
    exit()

for x in PortCheckRange:
    if portscan(host,x):
       print("Port ", x, " is Open")
       CheckTup = ["Port", str(x), "is open.", "\n"]
       RespOut = ' '.join(CheckTup)
       File.write(RespOut)

    else:
       print('port ', x, 'is closed')
       CheckTup = ["Port", str(x), "is closed.", '\n']
       RespOut = ' '.join(CheckTup)
       File.write(RespOut)

end= time.time()
print("Task completed. Port range", MinRange, " - ", MaxRange, " has been scanned.")
elasped = end - start
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Scan completed at: ", dt_string)
print("Total scan time: ", "%.2f" % elasped, "seconds.")
FinTup = ["Scan completed at", str(dt_string), "\n"]
FinOut = ' '.join(FinTup)
File.write(FinOut)
FinTup = ["Total scan time:","%.2f" % elasped, "seconds.", "\n"]
FinOut = ' '.join(FinTup)
File.write(FinOut)
File.close()