# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:21:42 2020

@author: Louis
"""
from collections import Counter
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

if 'ar value' in x1:
    x1=x1.replace('ar value', 'face value', 1)
if 'yield' in x1:
    x1=x1.replace('yield', 'YTM', 1)
if 'trad' in x1:
    x1=x1.replace('trad', 'price', 1)
x3=x1

if 'YTM' and 'zero' in x3:
    list1 = ['face value', 'year', 'YTM', 'price']
    list2 = re.findall('\d*\.?\d+', x1)
    filter1 = re.findall('\d*\.?\d+|face value|year|YTM|price', x1)
    cnt = Counter(filter1)
    twice=[k for k, v in cnt.items() if v > 1]
    if len(twice) != 0:
        filter1.remove((twice[0]))
    if filter1[0] in list1 and filter1[1] in list2 or filter1[1] in list1 and filter1[0] in list2:
        f1=[filter1[0], filter1[1]]
        if filter1[2] in list1 and filter1[3] in list2 or filter1[3] in list1 and filter1[2] in list2:
            f2=[filter1[2], filter1[3]]
            if filter1[4] in list1 and filter1[5] in list2 or filter1[5] in list1 and filter1[4] in list2:
                f3=[filter1[4], filter1[5]]
                g=filter1[6]

            else:
                g = filter1[4]
                f3=[filter1[5], filter1[6]]
        else:
            g = filter1[2]
            f2=[filter1[2], filter1[3]]
            f3=[filter1[5], filter1[6]]
    else:
        g = filter1[0]
        f1=[filter1[1], filter1[2]]
        f2=[filter1[3], filter1[4]]
        f3=[filter1[5], filter1[6]]

    question_list = [f1+f2+f3]
    questionf = ''
 
    for elements in question_list: 
        questionf += str(elements) + " " 
 

    question = (questionf+ g)
    print(question) 
    
    
if 'YTM' in x3 and 'zero' not in x3:
    list1 = ['coupon','face value', 'year', 'YTM', 'price']
    list2 = re.findall('\d*\.?\d+', x1)
    filter1 = re.findall('\d*\.?\d+|face value|year|YTM|price|coupon|acaulay', x1)
    cnt = Counter(filter1)
    twice=[k for k, v in cnt.items() if v > 1]
    if len(twice) != 0:
        filter1.remove((twice[0]))
    if filter1[0] in list1 and filter1[1] in list2 or filter1[1] in list1 and filter1[0] in list2:
        f1=[filter1[0], filter1[1]]
        if filter1[2] in list1 and filter1[3] in list2 or filter1[3] in list1 and filter1[2] in list2:
            f2=[filter1[2], filter1[3]]
            if filter1[4] in list1 and filter1[5] in list2 or filter1[5] in list1 and filter1[4] in list2:
                f3=[filter1[4], filter1[5]]
                if filter1[6] in list1 and filter1[7] in list2 or filter1[7] in list1 and filter1[6] in list2:
                    f4=[filter1[6], filter1[7]]
                    g=filter1[8]
                else:
                    g = filter1[6]
                    f4 = [filter1[7], filter1[8]]
            else:
                g = filter1[4]
                f3=[filter1[5], filter1[6]]
                f4 = [filter1[7], filter1[8]]
        else:
            g = filter1[2]
            f2=[filter1[2], filter1[3]]
            f3=[filter1[5], filter1[6]]
            f4 = [filter1[7], filter1[8]]
    else:
        g = filter1[0]
        f1=[filter1[1], filter1[2]]
        f2=[filter1[3], filter1[4]]
        f3=[filter1[5], filter1[6]]
        f4 = [filter1[7], filter1[8]]

    question_list = [f1+f2+f3+f4]
    questionf = ''
 
    for elements in question_list: 
        questionf += str(elements) + " " 
 

    question = (questionf+ g)
    print(question) 
    


if 'YTM' and 'zero' in x3:
    float1 = x3
    list1 = (re.findall('\d*\.?\d+', question))
    list3 = ['YTM', 'year', 'face value', 'price']
    filter2 = sorted(list3, key=question.find)
    if filter2[3]== 'price':
    #################################### yield
        if filter2[0]==('YTM'):
            ytm=float(list1[0])/100
        if filter2[1]==('YTM'):
            ytm=float(list1[1])/100
        if filter2[2]==('YTM'):
            ytm=float(list1[2])/100
#################################### year
        if filter2[0]=='year':
            t=float(list1[0])
        if filter2[1]=='year':
            t=float(list1[1])
        if filter2[2]=='year':
            t=float(list1[2])
#################################### face value
        if filter2[0]=='face value':
            fv=float(list1[0])
        if filter2[1]=='face value':
            fv=float(list1[1])
        if filter2[2]=='face value':
            fv=float(list1[2])
        c=1
        m = 0
        pv = ((fv)/(1+ytm)**t)
        print (pv)

    if g == 'YTM':
    #################################### yield
        if filter2[0]=='price':
            pv=float(list1[0])
        if filter2[1]=='price':
            pv=float(list1[1])
        if filter2[2]=='price':
            pv=float(list1[2])
#################################### year
        if filter2[0]=='year':
            t=float(list1[0])
        if filter2[1]=='year':
            t=float(list1[1])
        if filter2[2]=='year':
            t=float(list1[2])
#################################### face value
        if filter2[0]=='face value':
            fv=float(list1[0])
        if filter2[1]=='face value':
            fv=float(list1[1])
        if filter2[2]=='face value':
            fv=float(list1[2])
        c=1
        m = 0
        ytm=((fv/pv)**(1/t))-1
        print ('yield to maturity=', ytm*100,'%')
if 'YTM' in x3 and 'zero' not in x3:
    float1 = x3
    list1 = (re.findall('\d*\.?\d+', question))
    list3 = ['YTM', 'year', 'face value', 'coupon', 'price']
    macaulaylist = ['YTM', 'year', 'face value', 'coupon']
    filter2 = sorted(list3, key=question.find)
    macaulayfilter = sorted(macaulaylist, key=question.find)
    if 'semi' in x3:
        m = 2
    else:
        m = 1

    if 'acaulay' in x3:
        #################################### yield
        if macaulayfilter[0]=='YTM':
            ytm=float(list1[0])/100
        if macaulayfilter[1]=='YTM':
            ytm=float(list1[1])/100
        if macaulayfilter[2]=='YTM':
            ytm=float(list1[2])/100
        if macaulayfilter[3]=='YTM':
            ytm=float(list1[3])/100
#################################### coupon
        if macaulayfilter[0]=='coupon':
            c=float(list1[0])/100
        if macaulayfilter[1]=='coupon':
            c=float(list1[1])/100
        if macaulayfilter[2]=='coupon':
            c=float(list1[2])/100
        if macaulayfilter[3]=='coupon':
            c=float(list1[3])/100
#################################### year
        if macaulayfilter[0]=='year':
            t=float(list1[0])
        if macaulayfilter[1]=='year':
            t=float(list1[1])
        if macaulayfilter[2]=='year':
            t=float(list1[2])
        if macaulayfilter[3]=='year':
            t=float(list1[3])
#################################### face value
        if macaulayfilter[0]=='face value':
            fv=float(list1[0])
        if macaulayfilter[1]=='face value':
            fv=float(list1[1])
        if macaulayfilter[2]=='face value':
            fv=float(list1[2])
        if macaulayfilter[3]=='face value':
            fv=float(list1[3])
        if 'year ago' in x1:
            t =  t-1
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
        print ('Macaulay Duration=',text, '%')
        
        
    if g == 'price':
        
#################################### yield
        if filter2[0]=='YTM':
            ytm=float(list1[0])/100
        if filter2[1]=='YTM':
            ytm=float(list1[1])/100
        if filter2[2]=='YTM':
            ytm=float(list1[2])/100
        if filter2[3]=='YTM':
            ytm=float(list1[3])/100
#################################### coupon
        if filter2[0]=='coupon':
            c=float(list1[0])/100
        if filter2[1]=='coupon':
            c=float(list1[1])/100
        if filter2[2]=='coupon':
            c=float(list1[2])/100
        if filter2[3]=='coupon':
            c=float(list1[3])/100
#################################### year
        if filter2[0]=='year':
            t=float(list1[0])
        if filter2[1]=='year':
            t=float(list1[1])
        if filter2[2]=='year':
            t=float(list1[2])
        if filter2[3]=='year':
            t=float(list1[3])
#################################### face value
        if filter2[0]=='face value':
            fv=float(list1[0])
        if filter2[1]=='face value':
            fv=float(list1[1])
        if filter2[2]=='face value':
            fv=float(list1[2])
        if filter2[3]=='face value':
            fv=float(list1[3])
        if 'year ago' in x1:
            t =  t-1
        pv = ((fv*c/m*(1-(1+ytm/m)**(-m*t)))/(ytm/m)) + fv*(1+(ytm/m))**(-m*t)
        final_year = (t*fv)/(pv*(1+(ytm/m))**(m*t))
        print (pv)
        

    if (filter2[4]== 'YTM') and ('zero' and 'acaulay' not in x3):
        if filter2[0]=='price':
            pv=float(list1[0])
        if filter2[1]==('price'):
            pv=float(list1[1])
        if filter2[2]==('price'):
            pv=float(list1[2])
        if filter2[3]==('price'):
            pv=float(list1[3])
#################################### coupon
        if filter2[0]=='coupon':
            c=float(list1[0])/100
        if filter2[1]=='coupon':
            c=float(list1[1])/100
        if filter2[2]=='coupon':
            c=float(list1[2])/100
        if filter2[3]=='coupon':
            c=float(list1[3])/100
#################################### year
        if filter2[0]=='year':
            t=float(list1[0])
        if filter2[1]=='year':
            t=float(list1[1])
        if filter2[2]=='year':
            t=float(list1[2])
        if filter2[3]=='year':
            t=float(list1[3])
#################################### face value
        if filter2[0]=='face value':
            fv=float(list1[0])
        if filter2[1]=='face value':
            fv=float(list1[1])
        if filter2[2]=='face value':
            fv=float(list1[2])
        if filter2[3]=='face value':
            fv=float(list1[3])
        if 'year ago' in x1:
            t =  t-1
        ytm = (((c*fv)+((fv-pv))/t)/((fv+pv)/2))
        print ((ytm)*100)