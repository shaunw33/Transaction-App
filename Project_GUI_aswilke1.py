#Shaun Wilkerson, Final Project, CIS 345 12pm
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import aswilke1_logger

orders = []
logger = []
total = []

win = tk.Tk()
win.title('Carhartt Online Shopping')
win.geometry('600x700')
win.columnconfigure(0, weight=1)
win.config(bg='white')

def check_out():
    labels = []
    check_window = Toplevel(win)
    check_window.title("Shopping Cart")
    check_window.geometry("300x400")
    Label(check_window,text="Your final order consisted of:\n",font=("Canela", 22)).pack()
    for i in range(len(orders)):
        labels.append(Label(check_window,text = orders[i],font=("Canela", 12)))
        labels[i].pack()
    aswilke1_logger.log_transactions(logger)
    totalPrice = 0
    for i in range(len(total)):
        totalPrice += total[i]
    formatPrice = round(totalPrice,2)
    Label(check_window,text="\n\n\n\nTotal Cost:",font=("Canela", 22)).pack()
    Label(check_window,text=formatPrice,font=("Canela", 22)).pack()
    Button(check_window, command=check_window.destroy, font=("Canela", 16), text='Exit').pack()

def addToCartBtn(item):
    final_name = item.name
    final_price = item.price
    final_quantity = item.stock
    total.append(final_price)
    orders.append(final_name + ' ' + 'for' + ' ' + str(final_price) + ' at' + ' ' + str(final_quantity))
    logger.append([f'{final_name}', f'{final_price}',f'{time.ctime()}',f'{final_quantity}'])

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


logo = Image.open('Logo.jpeg')
jacket = Image.open('jacket.jpeg')
beanie = Image.open('beanie.jpeg')
flannel = Image.open('flannel.jpeg')
resize_jacket = jacket.resize((130,130))
resize_beanie = beanie.resize((130,130))
resize_flannel = flannel.resize((130,130))
logo = ImageTk.PhotoImage(logo)
jacket = ImageTk.PhotoImage(resize_jacket)
beanie = ImageTk.PhotoImage(resize_beanie)
flannel = ImageTk.PhotoImage(resize_flannel)

title_label = tk.Label(win, text = "Winter '22 Collection",bg="white") #Title
title_label.config(font=('Canela bold',40))
title_label.grid(row=0,column=0)

logo_pic = tk.Label(win,image = logo)
logo_pic.grid(row=0,column=1)

jacketObject = Item("Layered Active Jacket",79.99," 1 Quantity" )
jacket_photo = tk.Label(win, image = jacket, borderwidth=0,relief="solid")
jacket_photo.grid(row=1, column=0,padx=10,pady=10,sticky=W)
jacket_price = tk.Label(win, text = "Layered Active Jacket\n$79.99",font=("Canela", 16))
jacket_price.grid(row=1, column=0,padx=10,pady=10,sticky=E)
jacket_button = Button(win, text="Add To Cart",cursor="hand2", command=lambda i=jacketObject: addToCartBtn(i) )
jacket_button.grid(row=1, column=1, ipady=10)

beanieObject = Item("Knit Cuffed Beanie",9.99,"1 Quantity")
beanie_photo = tk.Label(win, image = beanie, borderwidth=0,relief="solid")
beanie_photo.grid(row=2, column=0,padx=10,pady=10,sticky=W)
beanie_price = tk.Label(win, text = "Knit Cuffed Beanie\n$9.99",font=("Canela", 16))
beanie_price.grid(row=2, column=0,padx=10,pady=10,sticky=E)
beanie_button = Button(win, text="Add To Cart",cursor="hand2", command=lambda i=beanieObject: addToCartBtn(i) )
beanie_button.grid(row=2, column=1, ipady=10)

flannelObject = Item("Relaxed Fit Flannel",19.99,"1 Quantity")
flannel_photo = tk.Label(win, image = flannel, borderwidth=0,relief="solid")
flannel_photo.grid(row=3, column=0,padx=10,pady=10,sticky=W)
flannel_price = tk.Label(win, text = "Relaxed Fit Flannel\n$19.99",font=("Canela", 16))
flannel_price.grid(row=3, column=0,padx=10,pady=10,sticky=E)
flannel_button = Button(win, text="Add To Cart",cursor="hand2", command=lambda i=flannelObject: addToCartBtn(i) )
flannel_button.grid(row=3, column=1, ipady=10)


exit_button = Button(win, command=win.destroy,font=("Canela", 16), text='Exit', width=15)
exit_button.grid(column=0, row=10, pady=20, padx=(35, 0), sticky=W)
checkout_button = Button(win, command=check_out,font=("Canela", 16), text='Check Out', width=15)
checkout_button.grid(column=1, row=10, pady=20, padx=(0, 35), sticky=W)

win.mainloop()