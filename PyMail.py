import smtplib, random, string, time, json
from tkinter import *

class EmailClient:
    def __init__(self, user_address, user_password):
        self.user_address = user_address
        self.user_password = user_password

        self.s = smtplib.SMTP('smtp.gmail.com', 587) 
        self.s.starttls() 
        
    def send(self, receiver, message):
        self.s.login(self.user_address, self.user_password)
        self.s.sendmail(self.user_address, receiver, message) 
    
class EmailWin:
    def __init__(self):
        self.configFile = json.loads(open('config.json').read())
    
        self.win = Tk()
        self.win.title = 'PyMail'
        self.win.geometry("550x350")

        self.sendBtn = Button(self.win, text = 'Send', command = lambda: EmailWin.sendEmail(self))
        self.sendBtn.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 0.2)

        self.receiverEditor = Text(self.win)
        self.receiverEditor.place(relx = 0.2, rely = 0, relwidth = 0.7, relheight = 0.1)
        self.receiverEditor.configure(font = ("Helvetica", 17))

        self.sendCountEditor = Text(self.win)
        self.sendCountEditor.place(relx = 0.9, rely = 0, relwidth = 0.1, relheight = 0.1)
        self.sendCountEditor.configure(font = ("Helvetica", 17))
        self.sendCountEditor.insert(INSERT, '1')

        self.messageEditor = Text(self.win)
        self.messageEditor.place(relx = 0, rely = 0.09, relwidth = 1, relheight = 0.9)
        self.messageEditor.configure(font = ("Helvetica", 12))

        self.win.mainloop()
 
    def sendEmail(self):
        myClient = EmailClient(self.configFile["user_address"], self.configFile["user_password"])
        for _ in range( int( self.sendCountEditor.get('1.0', END) ) ):
            myClient.send(self.receiverEditor.get('1.0', END), self.messageEditor.get('1.0', END))

if __name__ == '__main__':
    myEmail = EmailWin()
