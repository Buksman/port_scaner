import threading
import socket
import time
from datetime import datetime

start_time = datetime.now()

# ports = []
# for i in range(65535):
# ports.append(i)

with open("hosts") as file:
host_list = [row.strip() for row in file]


def scan_ip(host, port):


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)

try:
s.connect((host, port))
print("IP: " + host + " Open port: " + str(port))
s.close
except:
pass

count = 0
for ip in host_list:
count = count + 1

# print('=' * 50)
# print("Сканирую: ", ip)
# print('-' * 50)

# for port in ports:
time.sleep(0.05)
t = threading.Thread(target=scan_ip, args=(ip, 22))
t.daemon = True
t.start()

# if count == 3:
# print("\nTIME OUT")
# count = 0
# time.sleep(10)

#print('=' * 50, "\n")

t.join()

end_time = datetime.now()
print('Прошло: {}'.format(end_time - start_time))
input("happy end : ")
