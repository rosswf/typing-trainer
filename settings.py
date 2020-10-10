import tkinter  as tk
# window = tk.Tk()
# window.geometry('400x400')
# greeting = tk.Label(text="Hello, Tkinter")
# label = tk.Label(text="Name")
# entry = tk.Entry(window)
# label.pack()
# entry.pack()
# check = tk.Button(window,text='check 3', command=window.destroy)
# check.pack()
# print(entry.get())
# window.mainloop()
WIDTH = 800
HEIGHT = 600
FONT = 'carlito'
FONT_SIZE = 72
# BG_COLOUR = pygame.Color('0x584B53')
# FONT_COLOUR = pygame.Color('0xFFBA0A')
# SCORE_COLOUR = pygame.Color('0xF4F7F5')
# END_SCREEN_COLOUR = pygame.Color('0x584B53')
VELOCITY = 180  # SHOULD BE MULTIPLE OF FPS
FPS = 60
WORDS_PER_SECOND = 0.5
WORD_FILE = 'words.txt'
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 5
MAX_WORDS = 50
SOUND = True    # Will be set to False if issues opening audio files
VOLUME = 0.5    # Value between 0.0 and 1.0
KEYBOARD_LAYOUT = 0
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

        button = tk.Button(self.root, text = 'Start The GAME', command=self.start)
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
