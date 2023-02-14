from tkinter import *
from tkinter import ttk

def start():
    print("ABC")

def stop():
    print("STOP")


root_window = Tk()
root_window.title('StudyHacks')
root_window.geometry("370x230")
root_window.resizable(False, False)

header_frm = Frame(root_window, relief="solid", border=1)
id = Label(header_frm, text="성균 ID", padx=3, height=2, justify="center")
id_input = Entry(header_frm, bd=1, width=40)
pw = Label(header_frm, text="성균 PW", padx=3, height=2, justify="center")
pw_input = Entry(header_frm, bd=1, show="*", width=40)
key = Label(header_frm, text="KEY", padx=3, height=2, justify="center")
key_input = Entry(header_frm, bd=1, show="*", width=40)
id.grid(row=0, column=0, padx=3, pady=3)
id_input.grid(row=0, column=1, padx=3, pady=3)
pw.grid(row=1, column=0, padx=3, pady=3)
pw_input.grid(row=1, column=1, padx=3, pady=3)
key.grid(row=2, column=0, padx=3, pady=3)
key_input.grid(row=2, column=1, padx=3, pady=3)
header_frm.pack(side="top", padx=5, pady=5)

bottom_frm = Frame(root_window, relief="solid", border=1)
find = Button(bottom_frm, text="KEY 찾기", width=20, height=3, command=start)
login = Button(bottom_frm, text="로그인", width=20, height=3, command=stop)
find.grid(row=0, column=0, padx=3, pady=3)
login.grid(row=0, column=1, padx=3, pady=3)
bottom_frm.pack(side="bottom", padx=5, pady=5)

root_window.mainloop()