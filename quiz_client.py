import socket
from threading import Thread
from tkinter import *

# nickname = input("Enter Nickname >> ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port= 8001

client.connect((ip_address, port))

print("Connected to server ...")

class GUI():
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=400)

        self.pls = Label(
            self.login, 
            text = "Please Log In to Continue",
            justify=CENTER,
            font = "Helevica 14 bold"
        )
        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.labelName = Label(self.login, text="Name: ", font="Helevica 12")
        self.labelName.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)

        self.entryName = Entry(self.login, font="Helvetica 14")
        self.entryName.place(
            relwidth= 0.4,
            relheight= 0.12,
            relx = 0.35,
            rely = 0.2                
        )
        self.entryName.focus()

        self.go = Button(
            self.login, 
            text="CONTINUE", 
            font="Helevica 14 bold", 
            command = lambda: self.goAhead(self.entryName.get())
        )
        self.go.place(relx = 0.4, rely= 0.55)

        self.window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target = self.recieve)
        rcv.start()

    def recieve(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')

                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured ...")
                client.close()
                break

g = GUI()
# def recieve():


# def write():
#     while True:
#         message = '{}:{}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# recieve_thread = Thread(target=recieve)
# recieve_thread.start()

# write_thread = Thread(target=write)
# write_thread.start()


