# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:01:04 2020

@author: Carl
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
if 'growth rate' in x1:
    x1=x1.replace('growth rate', 'grow rate', 1)


x3=x1

if 'equit' in x3 and 'divid' in x3:
    if 'grow rate' in x3 and 'YTM' in x3:
        list1 = ['equit', 'grow rate', 'YTM']
        list2 = re.findall('\d*\.?\d+', x1)
        filter1 = re.findall('\d*\.?\d+|equit|YTM|grow rate', x1)
        cnt = Counter(filter1)
        twice=[k for k, v in cnt.items() if v > 1]
        if len(twice) != 0:
            filter1.remove((twice[0]))
            if len(twice) != 1:
                filter1.remove((twice[1]))
        if filter1[0] in list1 and filter1[1] in list2 or filter1[1] in list1 and filter1[0] in list2:
            f1=[filter1[0], filter1[1]]
            if filter1[2] in list1 and filter1[3] in list2 or filter1[3] in list1 and filter1[2] in list2:
                f2=[filter1[2], filter1[3]]
                g = filter1[4]

            else:
                g = filter1[2]
                f2=[filter1[2], filter1[3]]

        else:
            g = filter1[0]
            f1=[filter1[1], filter1[2]]
            f2=[filter1[3], filter1[4]]

        question_list = [f1+f2]
        questionf = ''
 
        for elements in question_list: 
            questionf += str(elements) + " " 
 

        question = (questionf+ g)
        print(question)
        print(71)
    
    
    if 'share' in x3 and 'grow rate' not in x3:
        list1 = ['equit', 'divid', 'share']
        list2 = re.findall('\d*\.?\d+', x1)
        filter1 = re.findall('\d*\.?\d+|equit|divid|share', x1)
        cnt = Counter(filter1)
        twice=[k for k, v in cnt.items() if v > 1]
        if len(twice) != 0:
            filter1.remove((twice[0]))
            if len(twice) != 1:
                filter1.remove((twice[1]))
        if filter1[0] in list1 and filter1[1] in list2 or filter1[1] in list1 and filter1[0] in list2:
            f1=[filter1[0], filter1[1]]
            if filter1[2] in list1 and filter1[3] in list2 or filter1[3] in list1 and filter1[2] in list2:
                f2=[filter1[2], filter1[3]]
                g = filter1[4]

            else:
                g = filter1[2]
                f2=[filter1[2], filter1[3]]

        else:
            g = filter1[0]
            f1=[filter1[1], filter1[2]]
            f2=[filter1[3], filter1[4]]

        question_list = [f1+f2]
        questionf = ''
 
        for elements in question_list: 
            questionf += str(elements) + " " 
 

        question = (questionf+ g)
        print(question) 
        print(107)
    
    if 'share' in x3 and 'grow rate' in x3:
        list1 = ['equit', 'divid', 'share', 'grow rate']
        list2 = re.findall('\d*\.?\d+', x1)
        filter1 = re.findall('\d*\.?\d+|equit|divid|share|grow rate', x1)
        cnt = Counter(filter1)
        twice=[k for k, v in cnt.items() if v > 1]
        if len(twice) != 0:
            filter1.remove((twice[0]))
            if len(twice) != 1:
                filter1.remove((twice[1]))
        if filter1[0] in list1 and filter1[1] in list2 or filter1[1] in list1 and filter1[0] in list2:
            f1=[filter1[0], filter1[1]]
            if filter1[2] in list1 and filter1[3] in list2 or filter1[3] in list1 and filter1[2] in list2:
                f2=[filter1[2], filter1[3]]
                if filter1[4] in list1 and filter1[5] in list2 or filter1[5] in list1 and filter1[4] in list2:
                    f3=[filter1[4], filter1[5]]
                    g = filter1[6]
                else:
                    g=filter1[4]
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
        print(150)
    
    



    if 'share' in x3 or 'grow rate' in x3:
        float1 = x3
        list1 = (re.findall('\d*\.?\d+', question))
        list3 = ['divid', 'equit', 'share']
        filter2 = sorted(list3, key=question.find)
        if g == 'grow rate':
    #################################### yield
            if filter2[0]==('divid'):
                di=float(list1[0])
            if filter2[1]==('divid'):
                di=float(list1[1])
            if filter2[2]==('divid'):
                di=float(list1[2])
#################################### year
            if filter2[0]=='equit':
                eq=float(list1[0])/100
            if filter2[1]=='equit':
                eq=float(list1[1])/100
            if filter2[2]=='equit':
                eq=float(list1[2])/100
##################################### share
            if filter2[0]=='share':
                s=float(list1[0])
            if filter2[1]=='share':
                s=float(list1[1])
            if filter2[2]=='share':
                s=float(list1[2])
                
            gr= s/(di/eq)*100
            print (gr)

        if g == 'share':
    #################################### yield
            if filter2[0]==('divid'):
                di=float(list1[0])/100
            if filter2[1]==('divid'):
                di=float(list1[1])/100
#################################### year
            if filter2[0]=='equit':
                eq=float(list1[0])
            if filter2[1]=='equit':
                eq=float(list1[1])

            print (eq)
            if 'YTM' in x3:
                float1 = x3
                list1 = (re.findall('\d*\.?\d+', question))
                list3 = ['YTM', 'equit', 'grow rate']
                filter2 = sorted(list3, key=question.find)
                if g == 'grow rate':
            #################################### yield
                    if filter2[0]==('YTM'):
                        ytm=float(list1[0])
                    if filter2[1]==('YTM'):
                        ytm=float(list1[1])
                    if filter2[2]==('YTM'):
                        ytm=float(list1[2])
#################################### year
                    if filter2[0]=='equit':
                        eq=float(list1[0])
                    if filter2[1]=='equit':
                        eq=float(list1[1])
                    if filter2[2]=='equt':
                        eq=float(list1[2])
 
                gr = (eq-ytm)
                print (gr)


eq = str(eq)
