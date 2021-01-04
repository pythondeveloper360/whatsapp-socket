from tkinter import Tk,Label,Frame
import threading
import socket as s
host = '127.0.0.1'
port = 54321

socket = s.socket(s.AF_INET,s.SOCK_STREAM)
socket.connect((host,port))
    



root = Tk()
chatLabel = Frame(root,width = 100,height = 100,bg = "Black")
chatLabel.pack(side = "left",fill = "x")
messageLable = Frame(width = 100,height = 100,bg = "blue")
messageLable.pack(side = "right")
root.mainloop()