# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:17:51 2020

@author: Asha
"""


import os
import urllib.request as uq
import tkinter as tk
from PIL import ImageTk, Image


def start():
    ent_start.insert(0, 'sof')

def stop():
    ent_stop.insert(0, 'eof')

def store():
    text = ent_start.get()
    text1 = ent_stop.get()
    text2 = notes.get('1.0', tk.END)
    #f = open('/Users/aryasafshari/Downloads/gui.txt', 'a+')
    f = open('/users/asha/desktop/gui.txt', 'a+')
    print(i.split('_')[6]+i.split('_')[7][0:6])
    f.write(text+'/'+text1+'/'+i.split('_')[6]+i.split('_')[7][0:6]+'\n')
    f.close()
    #f = open('/Users/aryasafshari/Downloadsgui.txt', 'a+')
    f = open('/users/asha/desktop/notation.txt', 'a+')
    f.write('\n'+text+'/'+text1+'/'+i.split('_')[6]+i.split('_')[7][0:6]+' : '+'\n'+text2+'\n')
    f.close()
    
def next():
    window.destroy()

def begin():
    text = label.get()
    entry.append(text)
    window.destroy()
    
#open file
#f = open('/Users/aryasafshari/Downloads/fgm_new.txt', 'r')
f = open('/users/asha/desktop/fgm_new.txt', 'r')
fgmurl = []
for i in f.readlines():
    youmst = i.rstrip('\n')
    fgmurl.append(youmst)
f.close


#spread by underscore and extract dates and timnes
date = []
for i in fgmurl:
    date.append(i.split('_'))

entry = []
window = tk.Tk()

label = tk.Entry()
label.pack()

name = label.get()
entry.append(name)
button = tk.Button(text = 'next', command = begin)
button.pack()
window.mainloop()


starting = entry[1]

if starting == '':
    brst_urls = []
    for i in date:
        year = str(i[4][0:4])
        month = str(i[4][4:6])
        day = str(i[4][6:8])
        hour = str(i[4][8:10])
        minute = str(i[4][10:12])
        second = str(i[4][12:14])
        tag = 'https://lasp.colorado.edu/mms/sdc/public/data/sdc/burst/all_mms1_summ/'+year+'/'+month+'/'+day+'/burst_all_mms1_summ_'+year+month+day+'_'+hour+minute+second+'.png'
        brst_urls.append(tag)
else:
    brst_url = []
    brst_urls = []
    year = starting[0:4]
    month = starting[4:6]
    day = starting[6:8]
    hour = starting[8:10]
    minute = starting[10:12]
    second = starting[12:14]
    for i in fgmurl:
        if starting in i:
            index = fgmurl.index(i)
        else:
            pass
    for i in date:
        year = str(i[4][0:4])
        month = str(i[4][4:6])
        day = str(i[4][6:8])
        hour = str(i[4][8:10])
        minute = str(i[4][10:12])
        second = str(i[4][12:14])
        tag = 'https://lasp.colorado.edu/mms/sdc/public/data/sdc/burst/all_mms1_summ/'+year+'/'+month+'/'+day+'/burst_all_mms1_summ_'+year+month+day+'_'+hour+minute+second+'.png'
        brst_url.append(tag)
    brst_urls = brst_url[index:]

for i in brst_urls:
    #uq.urlretrieve(i, '/Users/aryasafshari/Downloads/'+year+month+day+hour+minute+second+'.png')   
    uq.urlretrieve(i, '/users/asha/desktop/checkmate/'+year+month+day+hour+minute+second+'.png')
    
    window = tk.Tk()
    
    window.attributes('-fullscreen', True)

    #image
    #image = Image.open('/Users/aryasafshari/Downloads/'+year+month+day+hour+minute+second+'.png')
    image = Image.open('/users/asha/desktop/checkmate/'+year+month+day+hour+minute+second+'.png')
    image = image.resize((860, 900), Image.ANTIALIAS)
    #image.save('/Users/aryasafshari/Downloads/youmst.png', quality=99)
    #image = Image.open('/Users/aryasafshari/Downloads/youmst.png')
    image.save('/users/asha/desktop/checkmate/youmst.png', quality=99)
    image = Image.open('/users/asha/desktop/checkmate/youmst.png')
    img = ImageTk.PhotoImage(image)
    panel = tk.Label(master=window, image=img)
    panel.pack(side=tk.LEFT)
    
    frame_2 = tk.Frame(master=window)
    frame_3 = tk.Frame(master=frame_2)
    
        #buttons pass/fail    
    frame_1 = tk.Frame(master=window)
    frame_4 = tk.Frame(master=frame_2)
    btn_pass = tk.Button(master=frame_4, text = 'Pass', width=25, height=10, command=store)
    btn_fail = tk.Button(master=frame_4, text = 'Fail', width=25, height=10, command=next)
    btn_next = tk.Button(master=frame_4, text = 'Next', width=25, height = 10, command = next)
    btn_next.pack(side=tk.RIGHT)
    btn_fail.pack(side=tk.LEFT)
    btn_pass.pack(side=tk.LEFT)
    frame_4.pack(side=tk.BOTTOM)
    
    #eof/sof
    btn_sof = tk.Button(master=frame_3, text='sof', command=start)
    btn_eof = tk.Button(master=frame_3, text='eof', command=stop)
    btn_sof.pack(side=tk.LEFT)
    btn_eof.pack(side=tk.RIGHT)
    
    #notes and time
    frame_start = tk.Frame(master=frame_3)
    frame_stop = tk.Frame(master=frame_3)
    lbl_start = tk.Label(master=frame_start, text='start time')
    lbl_stop = tk.Label(master=frame_stop, text='stop time')
    ent_start = tk.Entry(master=frame_start)
    ent_stop = tk.Entry(master=frame_stop)
    lbl_entry = tk.Label(master = frame_2, text = 'notes')
    notes = tk.Text(master=frame_2)
    name = notes.get('1.0', tk.END)
    lbl_start.pack(side=tk.TOP)
    ent_start.pack(side=tk.BOTTOM)
    frame_start.pack(side=tk.LEFT, padx=5)
    lbl_stop.pack(side=tk.TOP)
    ent_stop.pack(side=tk.BOTTOM)
    frame_stop.pack(side=tk.RIGHT, padx=5)
    frame_3.pack(side=tk.TOP, pady=15)
    lbl_entry.pack() 
    notes.pack(side=tk.RIGHT)
    
    frame_2.pack(side=tk.LEFT)
    

    window.mainloop()
    os.remove('/Users/aryasafshari/Downloads/'+year+month+day+hour+minute+second+'.png')
    #os.remove('/users/asha/desktop/checkmate/'+year+month+day+hour+minute+second+'.png')