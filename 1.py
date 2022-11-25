from requests import Session
from tkinter import Tk, Label, Button, Entry, StringVar
from tkinter.messagebox import showinfo, showerror
session = Session()


def uah_to_usd(amount):
    amount = float(amount)
    return round(float(session.get(
        "https://minfin.com.ua/currency/converter/uah-usd/"
    ).text.split('1 UAH = ')[1].split(' USD')[0])*amount, 2)


def usd_to_uah(amount):
    amount = float(amount)
    return round(float(session.get(
        "https://minfin.com.ua/currency/converter/uah-usd/"
    ).text.split('1 USD = ')[1].split(' UAH')[0])*amount, 2)


def packer(objects_to_pack):
    for object_to_pack in objects_to_pack:
        object_to_pack.pack()


def uah_to_usd_command():
    try:
        amount = float(amount_var.get())
        showinfo(title="Currency Exchange", message=f"{amount} UAH = {uah_to_usd(amount)} USD")
    except ValueError:
        showerror(title="Currency Exchange", message="Enter a number!")
    amount_var.set("")
    global objects
    for object_to_destroy in objects:
        object_to_destroy.destroy()
    objects = [Label(text="Welcome to Currency Exchange"),
               Button(text="UAH to USD", command=uah_to_usd_gui), Button(text="USD to UAH", command=usd_to_uah_gui)]
    packer(objects)


def usd_to_uah_gui():
    global objects
    for object_to_destroy in objects:
        object_to_destroy.destroy()
    objects = [Label(text="Enter the amount of USD that you have"), Entry(textvariable=amount_var),
               Button(text="Exchange", command=usd_to_uah_command)]
    packer(objects)


def usd_to_uah_command():
    try:
        amount = float(amount_var.get())
        showinfo(title="Currency Exchange", message=f"{amount} USD = {usd_to_uah(amount)} UAH")
    except ValueError:
        showerror(title="Currency Exchange", message="Enter a number!")
    amount_var.set("")
    global objects
    for object_to_destroy in objects:
        object_to_destroy.destroy()
    objects = [Label(text="Welcome to Currency Exchange"),
               Button(text="UAH to USD", command=uah_to_usd_gui), Button(text="USD to UAH", command=usd_to_uah_gui)]
    packer(objects)


def uah_to_usd_gui():
    global objects
    for object_to_destroy in objects:
        object_to_destroy.destroy()
    objects = [Label(text="Enter the amount of UAH that you have"), Entry(textvariable=amount_var),
               Button(text="Exchange", command=uah_to_usd_command)]
    packer(objects)


root = Tk()
amount_var = StringVar()
root.resizable(False, False)
root.title("Currency Exchange")
objects = [Label(text="Welcome to Currency Exchange"),
           Button(text="UAH to USD", command=uah_to_usd_gui), Button(text="USD to UAH", command=usd_to_uah_gui)]
packer(objects)
root.mainloop()
