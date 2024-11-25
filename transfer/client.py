#CLIENT SIDE

import socket
import os

def send_file(file_path,host='127.0.0.1',port=5001,buffer_size=4096):
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host,port))

    print("CLIENT STARTED")

    with open(file_path,'rb') as f:
        while True:
            bytes_read=f.read(buffer_size)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)

    client_socket.close()
    print("CLIENT STOPPED")

if __name__=="__main__":
    file_send="file.txt"
    send_file(file_send)


