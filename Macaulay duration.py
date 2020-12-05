# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:37:59 2020

@author: Louis
"""

import re
import tkinter as tk
import pandas as pd
pd.options.mode.chained_assignment = None
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 350, height = 350, bg='black')
canvas1.pack()
entry1 = tk.Entry (root) # create the entry box
canvas1.create_window(150, 50, window=entry1)
def insert_text(): # add a function/command to be called by the button (i.e., button1 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed
    x1 = str(entry1.get()) # store the data input by the user as a variable x1 

button1 = tk.Button (root, text='Insert question ',command=insert_text, bg='blue', fg='white') # button to call the 'inserter' command above 
canvas1.create_window(150, 80, window=button1)
root.mainloop()
#We have coupon bond with a 5% coupon rate, a 2-year semi-annual  face value of $100, and a yield of 8%. What is the price of this coupon?
float1 = x1
list1 = (re.findall('\d*\.?\d+', float1))
list2 = ['yield', 'YTM', 'coupon', 'year', 'face value']
list3 = ['YTM', 'coupon', 'year', 'face value']
list4 = ['yield', 'coupon', 'year', 'face value']

filter1 = sorted(list2, key=x1.find)

if filter1[0]== 'YTM':
    new_list = sorted(list4, key=x1.find)
    Y1='yield'
else:
    new_list = sorted(list3, key=x1.find)
    Y1='YTM'

#################################### yield
if new_list[0]==(Y1):
    ytm=float(list1[0])/100
if new_list[1]==(Y1):
    ytm=float(list1[1])/100
if new_list[2]==(Y1):
    ytm=float(list1[2])/100
if new_list[3]==(Y1):
    ytm=float(list1[3])/100
#################################### coupon
if new_list[0]=='coupon':
    c=float(list1[0])/100
if new_list[1]=='coupon':
    c=float(list1[1])/100
if new_list[2]=='coupon':
    c=float(list1[2])/100
if new_list[3]=='coupon':
    c=float(list1[3])/100
#################################### year
if new_list[0]=='year':
    t=float(list1[0])
if new_list[1]=='year':
    t=float(list1[1])
if new_list[2]=='year':
    t=float(list1[2])
if new_list[3]=='year':
    t=float(list1[3])
#################################### face value
if new_list[0]=='face value':
    fv=float(list1[0])
if new_list[1]=='face value':
    fv=float(list1[1])
if new_list[2]=='face value':
    fv=float(list1[2])
if new_list[3]=='face value':
    fv=float(list1[3])
print (ytm)
print (c)
print (t)
print (fv)
if 'semi' in x1: 
   m = 2
else:
   m = 1
    
pv = ((fv*c/m*(1-(1+ytm/m)**(-m*t)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*t)
final_year = (t*fv)/(pv*(1+(ytm/m))**(m*t)) 
sum = 0
x = 1
while x <= m*t:
    tn = x/m
    x = x + 1
    dur = (fv*c*tn)/(pv*m*(1+(ytm/m))**(m*tn))
    sum = sum + dur
text= sum+final_year
print (text)
