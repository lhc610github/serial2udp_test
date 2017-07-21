import socket,select,serial
import time

UDP_PORT_IN = 14550 # UDP server port
UDP_PORT_OUT = 14560
MAX_UDP_PACKET=512 # max size of incoming packet to avoid sending too much data to the micro
SERIAL_PORT='/dev/ttyAMA0'
BROADCAST_MODE=False #set to True if you want a broadcast replay instead of unicast


udp_client_address=('192.168.1.100',UDP_PORT_OUT) #where to forward packets coming from serial port
udp_server_address = ('192.168.1.151',UDP_PORT_IN) #udp server
udp_broadcast=('<broadcast>',UDP_PORT_OUT) #broadcast address

serial_t=serial.Serial(SERIAL_PORT,115200) #open the file corrisponding to YUN serial port

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_socket.bind(udp_server_address)
if BROADCAST_MODE: 
        udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while True:
                serial_data = serial_t.read(100)
		print serial_data
