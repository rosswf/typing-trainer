import tkinter  as tk
class App():
   def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Options")
        self.root.geometry('250x340')
        self.ops = {'WIDTH':1024,'HEIGHT':768,'FONT_SIZE' : 72,'VELOCITY': 180,
        'WORDS_PER_SECOND' : 0.5,'WORD_FILE' : 'words.txt',
        'MIN_WORD_LENGTH' : 4,'MAX_WORD_LENGTH' : 5,
        'MAX_WORDS' : 50,'SOUND' : True,'KEYBOARD_LAYOUT' : 0
        }
        self.ops2 = [1024,768,72,180,0.5,'words.txt',4,5,50,0]
        self.abc = []
        self.entries = []
        r = 0
        for i in self.ops:
            if i == 'SOUND':
                self.var1 = tk.IntVar(value=1)
                i = tk.Checkbutton(self.root,text="SOUND" ,variable=self.var1)
                i.pack()
                i.place(x=80, y=10+20+20*r)
                self.entries.append(i)
                r += 1
                continue
            if i  =='KEYBOARD_LAYOUT':
                self.var2 = tk.IntVar(value=1)
                i = tk.Checkbutton(self.root,text="KEYBOARD_LAYOUT" ,variable=self.var2)
                i.pack()
                i.place(x=80, y=10+20+20*r)
                self.entries.append(i)
                r += 1
                continue
            self.abc.append(tk.Label(text = i))
            self.abc[r].pack()
            self.abc[r].place(x=10, y=10+20+20*r)
            i=tk.Entry(self.root)
            i.pack()
            
            i.place(x=80, y=10+20+20*r)
            i.insert(0,self.ops2[r])
            self.entries.append(i)
            r += 1

        button = tk.Button(self.root, text = 'START THE  GAME', command=self.start)
        button.pack()
        button.place(x=80,y=260)
        self.root.mainloop()

   def start(self):
       self.dfg = []
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
            self.dfg.append(i.get())
            r+=1
       self.root.destroy()
