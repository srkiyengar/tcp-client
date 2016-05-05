import socket
import time


class my_socket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host,port))

    def end_socket(self):
        #self.sock.shutdown(self.sock)
        self.sock.close()

    def send_data(self, msg):

        message_len = len(msg)
        total = 0
        while total < message_len:
            sent = self.sock.send(msg[total:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total = total + sent


ndi_socket = my_socket()
ndi_socket.connect('192.168.10.2', 5000)


#read command is 7a


for i in range(0,10,1):
    num = 200050 +i
    num_str = str(num)
    length = str(len(num_str))
    send_str = "7" + length + num_str
    print send_str
    ndi_socket.send_data(send_str)
    x = raw_input("Type when ready")


    num_str = str(num)
    length = str(len(num_str))
    send_str = "5" + length + num_str
    print send_str
    ndi_socket.send_data(send_str)
    x = raw_input("Type when ready")

ndi_socket.end_socket()
#time.sleep(1)

