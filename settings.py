import tkinter  as tk
from tkinter import ttk 
import json, os
class App():
    def __init__(self):
        self.dfg = []
        try:
            self.check = self.check()
            if self.check == 1:
                return self.use_the_save_data()
        except:
            pass
        self.root = tk.Tk()
        self.root.title("Game Options")
        self.root.geometry('300x340')
        self.ops = {'WIDTH':1024,'HEIGHT':768,'FONT_SIZE' : 72,'VELOCITY': 180,
        'WORDS_PER_SECOND' : 0.5,'WORD_FILE' : 'words.txt',
        'MIN_WORD_LENGTH' : 4,'MAX_WORD_LENGTH' : 5,
        'MAX_WORDS' : 50,'SOUND' : True,'KEYBOARD_LAYOUT' : 0
        ,"DON'T SHOW AGAIN":0}
        self.ops2 = [1024,768,72,180,0.5,'words.txt',4,5,50,0,0]
        self.abc = []
        self.entries = []
        self.x = 160
        self.data = {}
        r = 0
        for i in self.ops:
            if i == "WORD_FILE":
                self.abc.append(tk.Label(text = i))
                self.abc[r].pack()
                self.abc[r].place(x=10, y=10+20+20*r)
                i = ttk.Combobox(self.root,width=17,textvariable = 'n')
                i['values']= os.listdir("./samples")
                i.place(x=self.x,  y=10+20+20*r)
                i.insert(0, self.ops2[r])
                i.current() 
                self.entries.append(i)
                r +=1
                continue
            if i == "DON'T SHOW AGAIN":
                self.var3 = tk.IntVar()
                i = tk.Checkbutton(self.root,text="DON'T SHOW AGAIN" ,variable=self.var3)
                i.pack()
                i.place(x=self.x, y=10+20+20*r)
                self.entries.append(i)
                r += 1
                continue
            if i == 'SOUND':
                self.var1 = tk.IntVar(value=1)
                i = tk.Checkbutton(self.root,text="SOUND" ,variable=self.var1)
                i.pack()
                i.place(x=self.x, y=10+20+20*r)
                self.entries.append(i)
                r += 1
                continue
            if i  =='KEYBOARD_LAYOUT':
                self.var2 = tk.IntVar(value=1)
                i = tk.Checkbutton(self.root,text="KEYBOARD_LAYOUT" ,variable=self.var2)
                i.pack()
                i.place(x=self.x, y=10+20+20*r)
                self.entries.append(i)
                r += 1
                continue
            self.abc.append(tk.Label(text = i))
            self.abc[r].pack()
            self.abc[r].place(x=10, y=10+20+20*r)
            i=tk.Entry(self.root)
            i.pack()
            
            i.place(x=self.x, y=10+20+20*r)
            i.insert(0,self.ops2[r])
            self.entries.append(i)
            
            r += 1

        button = tk.Button(self.root, text = 'START THE  GAME', command=self.start)
        button.pack()
        button.place(x=90,y=290)
        self.root.mainloop()
    
    def start(self):
        
        r = 0
        for i in self.entries:
            if r==9:
                if self.var1.get() ==1:
                    self.SOUND = True
                else:
                    self.SOUND = False
                self.dfg.append(self.SOUND)
                r+=1
                continue
            if r==10:
                self.dfg.append(self.var2.get())
                r+=1
                continue
            if r==11:
                self.dfg.append(self.var3.get())
                r+=1
                continue
            self.dfg.append(i.get())
            r+=1
        self.insert_data()
        self.root.destroy()


    def insert_data(self):
        with open('settings.json','w') as settings_json:
            json.dump(self.dfg, settings_json)
    def check(self):
        with open('settings.json') as settings_json:
            settings = json.load(settings_json)
        return settings[11]
    def use_the_save_data(self):
        with open('settings.json') as json_file:
            settings = json.load(json_file)
        for i in settings:
            self.dfg.append(i)
        
