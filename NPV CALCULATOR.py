# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:37:41 2020

@author: Louis
"""

import tkinter as tk
import pandas as pd

pd.options.mode.chained_assignment = None
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 1350, height = 1350, bg='black')
canvas1.pack()
######################################################
entry1 = tk.Entry (root)
canvas1.create_window(675, 50, window=entry1)
button1 = tk.Button (root, text='Discount Rate r', bg='purple', fg='white')
canvas1.create_window(675, 20, window=button1)
#####################################################
Y0CI=0
entry2 = tk.Entry (root)
canvas1.create_window(150, 130, window=entry2)
button1 = tk.Button (root, text='YEAR 0 CASH INF', bg='green', fg='white')
canvas1.create_window(150, 100, window=button1)
####################################################
Y0CO=0
entry3 = tk.Entry (root)
canvas1.create_window(150, 200, window=entry3)
button1 = tk.Button (root, text='YEAR 0 CASH OUT', bg='red', fg='white')
canvas1.create_window(150, 170, window=button1)
####################################################
Y1CI=0
entry4 = tk.Entry (root)
canvas1.create_window(150, 370, window=entry4)
button1 = tk.Button (root, text='YEAR 1 CASH INF', bg='green', fg='white')
canvas1.create_window(150, 340, window=button1)
####################################################
Y1CO=0
entry5 = tk.Entry (root)
canvas1.create_window(150, 440, window=entry5)
button1 = tk.Button (root, text='YEAR 1 CASH OUT', bg='red', fg='white')
canvas1.create_window(150, 410, window=button1)
####################################################
Y2CI=0
entry6 = tk.Entry (root)
canvas1.create_window(150, 610, window=entry6)
button1 = tk.Button (root, text='YEAR 2 CASH INF', bg='green', fg='white')
canvas1.create_window(150, 580, window=button1)
####################################################
Y2CO=0
entry7 = tk.Entry (root)
canvas1.create_window(150, 680, window=entry7)
button1 = tk.Button (root, text='YEAR 2 CASH OUT', bg='red', fg='white')
canvas1.create_window(150, 650, window=button1)
####################################################
Y3CI=0
entry8 = tk.Entry (root)
canvas1.create_window(675, 130, window=entry8)
button1 = tk.Button (root, text='YEAR 3 CASH INF', bg='green', fg='white')
canvas1.create_window(675, 100, window=button1)
####################################################
Y3CO=0
entry9 = tk.Entry (root)
canvas1.create_window(675, 200, window=entry9)
button1 = tk.Button (root, text='YEAR 3 CASH OUT', bg='red', fg='white')
canvas1.create_window(675, 170, window=button1)
####################################################
Y4CI=0
entry10 = tk.Entry (root)
canvas1.create_window(675, 370, window=entry10)
button1 = tk.Button (root, text='YEAR 4 CASH INF', bg='green', fg='white')
canvas1.create_window(675, 340, window=button1)
####################################################
Y4CO=0
entry11 = tk.Entry (root)
canvas1.create_window(675, 440, window=entry11)
button1 = tk.Button (root, text='YEAR 4 CASH OUT', bg='red', fg='white')
canvas1.create_window(675, 410, window=button1)
####################################################
Y5CI=0
entry12 = tk.Entry (root)
canvas1.create_window(675, 610, window=entry12)
button1 = tk.Button (root, text='YEAR 5 CASH INF', bg='green', fg='white')
canvas1.create_window(675, 580, window=button1)
####################################################
Y5CO=0
entry13 = tk.Entry (root)
canvas1.create_window(675, 680, window=entry13)
button1 = tk.Button (root, text='YEAR 5 CASH OUT', bg='red', fg='white')
canvas1.create_window(675, 650, window=button1)
####################################################
Y6CI=0
entry14 = tk.Entry (root)
canvas1.create_window(1200, 130, window=entry14)
button1 = tk.Button (root, text='YEAR 6 CASH INF', bg='green', fg='white')
canvas1.create_window(1200, 100, window=button1)
####################################################
Y6CO=0
entry15 = tk.Entry (root)
canvas1.create_window(1200, 200, window=entry15)
button1 = tk.Button (root, text='YEAR 6 CASH OUT', bg='red', fg='white')
canvas1.create_window(1200, 170, window=button1)
####################################################
Y7CI=0
entry16 = tk.Entry (root)
canvas1.create_window(1200, 370, window=entry16)
button1 = tk.Button (root, text='YEAR 7 CASH INF', bg='green', fg='white')
canvas1.create_window(1200, 340, window=button1)
####################################################
Y7CO=0
entry17 = tk.Entry (root)
canvas1.create_window(1200, 440, window=entry17)
button1 = tk.Button (root, text='YEAR 7 CASH OUT', bg='red', fg='white')
canvas1.create_window(1200, 410, window=button1)
####################################################
Y8CI=0
entry18 = tk.Entry (root)
canvas1.create_window(1200, 610, window=entry18)
button1 = tk.Button (root, text='YEAR 8 CASH INF', bg='green', fg='white')
canvas1.create_window(1200, 580, window=button1)
####################################################
Y8CO=0
entry19 = tk.Entry (root)
canvas1.create_window(1200, 680, window=entry19)
button1 = tk.Button (root, text='YEAR 8 CASH OUT', bg='red', fg='white')
canvas1.create_window(1200, 650, window=button1)
####################################################
#####################################################
def insert_number():
    global r
    r = str(entry1.get())
    if r==(''):
        r=0
    else:
        r = str(entry1.get())
    global Y0CI
    Y0CI = str(entry2.get())
    if Y0CI==(''):
        Y0CI=0
    else:
        Y0CI = str(entry2.get())
    global Y0CO
    Y0CO = str(entry3.get())
    if Y0CO==(''):
        Y0CO=0
    else:
        Y0CO = str(entry3.get())
    global Y1CI
    Y1CI = str(entry4.get())
    if Y1CI==(''):
        Y1CI=0
    else:
        Y1CI = str(entry4.get())
    global Y1CO
    Y1CO = str(entry5.get())
    if Y1CO==(''):
        Y1CO=0
    else:
        Y1CO = str(entry5.get())
    global Y2CI
    Y2CI = str(entry6.get())
    if Y2CI==(''):
        Y2CI=0
    else:
        Y2CI = str(entry6.get())
    global Y2CO
    Y2CO = str(entry7.get())
    if Y2CO==(''):
        Y2CO=0
    else:
        Y2CO = str(entry7.get())
    global Y3CI
    Y3CI = str(entry8.get())
    if Y3CI==(''):
        Y3CI=0
    else:
        Y3CI = str(entry8.get())
    global Y3CO
    Y3CO = str(entry9.get())
    if Y3CO==(''):
        Y3CO=0
    else:
        Y3CO = str(entry9.get())
    global Y4CI
    Y4CI = str(entry10.get())
    if Y4CI==(''):
        Y4CI=0
    else:
        Y4CI = str(entry10.get())
    global Y4CO
    Y4CO = str(entry11.get())
    if Y4CO==(''):
        Y4CO=0
    else:
        Y4CO = str(entry11.get())
    global Y5CI
    Y5CI = str(entry12.get())
    if Y5CI==(''):
        Y5CI=0
    else:
        Y5CI = str(entry12.get())
    global Y5CO
    Y5CO = str(entry13.get())
    if Y5CO==(''):
        Y5CO=0
    else:
        Y5CO = str(entry13.get())
    global Y6CI
    Y6CI = str(entry14.get())
    if Y6CI==(''):
        Y6CI=0
    else:
        Y6CI = str(entry14.get())
    global Y6CO
    Y6CO = str(entry15.get())
    if Y6CO==(''):
        Y6CO=0
    else:
        Y6CO = str(entry15.get())
    global Y7CI
    Y7CI = str(entry16.get())
    if Y7CI==(''):
        Y7CI=0
    else:
        Y7CI = str(entry16.get())
    global Y7CO
    Y7CO = str(entry17.get())
    if Y7CO==(''):
        Y7CO=0
    else:
        Y7CO = str(entry17.get())
    global Y8CI
    Y8CI = str(entry18.get())
    if Y8CI==(''):
        Y8CI=0
    else:
        
        Y8CI = str(entry18.get())
    global Y8CO
    Y8CO = str(entry19.get())
    if Y8CO==(''):
        Y8CO=0
    else:
        Y8CO = str(entry19.get())

def window_close():
    insert_number()
    root.destroy()

button1 = tk.Button (root, text='CALCULATE',command=insert_number, bg='orange', fg='white')
canvas1.create_window(675, 750, window=button1)


root.mainloop()
PV1=(float(Y0CI)-float(Y0CO))/((1+(float(r)))**0)
PV2=(float(Y1CI)-float(Y1CO))/((1+(float(r)))**1)
PV3=(float(Y2CI)-float(Y2CO))/((1+(float(r)))**2)
PV4=(float(Y3CI)-float(Y3CO))/((1+(float(r)))**3)
PV5=(float(Y4CI)-float(Y4CO))/((1+(float(r)))**4)
PV6=(float(Y5CI)-float(Y5CO))/((1+(float(r)))**5)
PV7=(float(Y6CI)-float(Y6CO))/((1+(float(r)))**6)
PV8=(float(Y7CI)-float(Y7CO))/((1+(float(r)))**7)
PV9=(float(Y8CI)-float(Y8CO))/((1+(float(r)))**8)
NPV=PV1+PV2+PV3+PV4+PV5+PV6+PV7+PV8
print ('Net Present Value is', NPV)
