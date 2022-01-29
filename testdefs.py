#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:44:57 2021

@author: srilthe
"""
from matchsmall import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import numpy as np
import ToolTip as tt

global conn, vessel, send_txt, returned
returned = []     

def click_btn(x):
    exec(btncmds[x])
    send_txt(btncmds[x])

def CreateToolTip(widget, text):
    toolTip = tt.ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
      
def send_txt(txt='blank'):
    if lb.size() > 16:
        lb.delete(0,'end')
    lb.insert('end', txt)

#tkinter_setup
root = tk.Tk()
root.geometry('300x200+1400+220')
root.title('tk tt krpc ksp')   
root.wait_visibility(root)
root.wm_attributes('-alpha',0.3,'-topmost', True)
rframe = Frame(root) 
rframe.place(x=65, y=44)
var2 = tk.StringVar()
var2.set(())
lb = tk.Listbox(rframe, listvariable=var2, height=8, width=24)    
    
#button setup
btntxts = []
btncmds = []

for cmd in match.zGenerate():
    click = f'match.{cmd[0]}()'
    btncmds.append(f'{click}')
    q = f'match.{cmd[0]}.btn'
    exec(f'Btn = {q}')
    btntxts.append(Btn)
txtbtn = btntxts
tt_var = [tk.StringVar() for i in range(len(txtbtn))]
cmds = btncmds
btn = [i for i in range(len(txtbtn))]
btn_text = [tk.StringVar() for i in range(len(txtbtn))]
for ctr,cmd in enumerate(txtbtn):
    btn[ctr] = Button(root,textvariable=btn_text[ctr],width=5, height=1, command= lambda x1=ctr: click_btn(x1))
    btn_text[ctr].set(f"{txtbtn[ctr]}")
    btn[ctr].place(x=3, y=ctr*32+38)
    CreateToolTip(btn[ctr], text = tt_var[ctr])
    tt_var[ctr].set(f'{txtbtn[ctr]}')

lb.pack()  
root.mainloop()    
