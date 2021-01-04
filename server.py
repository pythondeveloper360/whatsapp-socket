import threading
import socket
from tkinter import Tk


host = "127.0.0.1"
port = 54321

def socket_connetion():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((host,port))
        s.listen()
        while True:
            conn,addr = s.accept()
            with conn:
                print("connected by:",addr)


threading.Thread(target = socket_connetion).start()
