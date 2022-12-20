import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

window = tk.Tk()
window.title('B777017 PJH')
window.geometry('1200x800')

mainMenu = tk.Menu(window)
window.config(menu = mainMenu)

###Menus
file = tk.Menu(window, tearoff = False)
edit = tk.Menu(window, tearoff = False)
view = tk.Menu(window, tearoff = False)
colorTheme = tk.Menu(window, tearoff = False)

##color

themeChoice = tk.StringVar()
colorDict = {
    'Light Default' :('#000000','#ffffff'),
    'Light Plus' :('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Ping' : ('#2d2d2d','#ffe8e8'),
    'Charcoal' : ('#d3b774','#474747'),
    'Night Blue' :('#ededed','#6b9dc2')
}

mainMenu.add_cascade(label = 'File', menu = file)
mainMenu.add_cascade(label = 'edit', menu = edit)
mainMenu.add_cascade(label = 'view', menu = view)
mainMenu.add_cascade(label = 'Color Theme', menu = colorTheme)


###toolBar
toolBar = ttk.Label(window)
toolBar.pack(side = tk.TOP, fill = tk.X)

#font
fontTuple = tk.font.families()
fontFamily = tk.StringVar()
fontBox = ttk.Combobox(toolBar, width = 30, textvariable = fontFamily, state = 'readonly')
fontBox['values'] = fontTuple
fontBox.current(fontTuple.index('Arial'))
fontBox.grid(row = 0 , column = 0, padx = 5)

#size
sizeVar = tk.IntVar()
fontSize = ttk.Combobox(toolBar, width = 14, textvariable = sizeVar, state = 'readonly')
fontSize['values'] = tuple(range(8,80,2))
fontSize.current(2)
fontSize.grid(row=0,column=1,padx = 5)

#bold
boldIcon = tk.PhotoImage(file = 'icon/bold.png')
boldBtn = ttk.Button(toolBar, image = boldIcon)
boldBtn.grid(row = 0, column = 2, padx=5)

#italic
italicIcon = tk.PhotoImage(file = 'icon/italic.png')
italicBtn = ttk.Button(toolBar, image = italicIcon)
italicBtn.grid(row = 0, column = 3, padx = 5)

#underline
underlineIcon = tk.PhotoImage(file = 'icon/underline.png')
underlineBtn = ttk.Button(toolBar, image = underlineIcon)
underlineBtn.grid(row = 0, column = 4, padx = 5)

#fontColor
fontColorIcon = tk.PhotoImage(file = 'icon/font_color.png')
fontColorBtn = ttk.Button(toolBar, image = fontColorIcon)
fontColorBtn.grid(row = 0, column = 5, padx = 5)

#alignLeft
alignLeftIcon = tk.PhotoImage(file = 'icon/align_left.png')
alignLeftBtn = ttk.Button(toolBar, image = alignLeftIcon)
alignLeftBtn.grid(row = 0, column = 6, padx = 5)

#alignCenter
alignCenterIcon = tk.PhotoImage(file = 'icon/align_center.png')
alignCenterBtn = ttk.Button(toolBar, image = alignCenterIcon)
alignCenterBtn.grid(row = 0, column = 7, padx = 5)

#alignRight
alignRightIcon = tk.PhotoImage(file = 'icon/align_right.png')
alignRightBtn = ttk.Button(toolBar, image = alignRightIcon)
alignRightBtn.grid(row = 0, column = 8, padx = 5)



###text edit
textEditor = tk.Text(window)
textEditor.config(wrap = 'word', relief = tk.FLAT)

scrollBar = tk.Scrollbar(window)
textEditor.focus_set()
scrollBar.pack(side = tk.RIGHT, fill = tk.Y)
textEditor.pack(fill = tk.BOTH, expand = True)
scrollBar.config(command = textEditor.yview)
textEditor.config(yscrollcommand = scrollBar.set)

###font Setting
currentFontFamily = 'Arial'
currentFontSize = 12

def changeFont(event = None):
    global currentFontFamily
    currentFontFamily = fontFamily.get()
    textEditor.config(font = (currentFontFamily, currentFontSize))

def changeSize(event = None):
    global currentFontSize
    currentFontSize = fontSize.get()
    textEditor.config(font = (currentFontFamily, currentFontSize))
    
fontBox.bind("<<ComboboxSelected>>",changeFont)
fontSize.bind("<<ComboboxSelected>>",changeSize)

def changeBold():
    textProperty = tk.font.Font(font=textEditor['font'])
    if textProperty.actual()['weight'] == 'normal' :
       textEditor.configure(font = (currentFontFamily, currentFontSize, 'bold'))
    if textProperty.actual()['weight'] == 'bold' :
        textEditor.configure(font = (currentFontFamily, currentFontSize, 'normal'))
def changeItalic():
    textProperty = tk.font.Font(font=textEditor['font'])
    if textProperty.actual()['slant'] == 'roman' :
       textEditor.configure(font = (currentFontFamily, currentFontSize, 'italic'))
    if textProperty.actual()['slant'] == 'italic' :
        textEditor.configure(font = (currentFontFamily, currentFontSize, 'normal'))
def underLine():
    textProperty = tk.font.Font(font=textEditor['font'])
    if textProperty.actual()['underline'] == 0 :
       textEditor.configure(font = (currentFontFamily, currentFontSize, 'underline'))
    if textProperty.actual()['underline'] == 1 :
        textEditor.configure(font = (currentFontFamily, currentFontSize, 'normal'))
def changeFontColor():
    colorVar = tk.colorchooser.askcolor()
    textEditor.configure(fg = colorVar[1])
def alignLeft():
    textContent = textEditor.get(1.0, 'end')
    textEditor.tag_config('left', justify = tk.LEFT)
    textEditor.delete(1.0, tk.END)
    textEditor.insert(tk.INSERT, textContent, 'left')
def alignCenter():
    textContent = textEditor.get(1.0, 'end')
    textEditor.tag_config('center', justify = tk.CENTER)
    textEditor.delete(1.0, tk.END)
    textEditor.insert(tk.INSERT, textContent, 'center')
def alignRight():
    textContent = textEditor.get(1.0, 'end')
    textEditor.tag_config('right', justify = tk.RIGHT)
    textEditor.delete(1.0, tk.END)
    textEditor.insert(tk.INSERT, textContent, 'right')

boldBtn.configure(command = changeBold)
italicBtn.configure(command = changeItalic)
underlineBtn.configure(command = underLine)
fontColorBtn.configure(command = changeFontColor)
alignLeftBtn.configure(command = alignLeft)
alignCenterBtn.configure(command = alignCenter)
alignRightBtn.configure(command = alignRight)

textEditor.configure(font = ('Arial', 12))

###statusBar
statusBar = ttk.Label(window, text = 'Status Bar')
statusBar.pack(side = tk.BOTTOM)

###Functions
textChange = False

def changedText(event = None):
    global textChange
    
    if textEditor.edit_modified():
        textChange = True
        words = len(textEditor.get(1.0, 'end-1c').split())
        characters = len(textEditor.get(1.0,'end-1c'))
        statusBar.config(text = f'words : {words} Characters : {characters}')
    textEditor.edit_modified(False)
textEditor.bind('<<Modified>>', changedText)
        

##file
url = ''

def newFile(event = None):
    global url
    url = ''
    textEditor.delete(1.0,tk.END)

def openFile(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File',
                                     filetypes = (('Text file', '*.txt'),('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            textEditor.delete(1.0, tk.END)
            textEditor.insert(1.0, fr.read())
    except FileNotFoundError:
        print('error')
        return
    except :
        print('error2')
        return
    window.title(os.path.basename(url))

def saveFile(event = None):
    global url
    try:
        if url :
            content = str(textEditor.get(1.0,tk.END))
            with open(url, 'w', encoding = 'utf-8') as fw:
                fw.write(content)
        else :
            url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',
                                           filetypes = (('Text file', '*.txt'),('All files', '*.*')))
            url.write(content)
            url.close()
    except:
        return

def saveAs(event = None):
    global url
    try:
        content = textEditor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',
                                       filetypes = (('Text file', '*.txt'),('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

def exitFunc(event = None):
    global url, textChange
    try:
        if textChange:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
            if mbox is True :
                if url:
                    content = textEditor.get(1.0,tk.End)
                    with open(url,'w',encoding = 'utf-8') as fw:
                        fw.write(content)
                        window.destroy()
                else:
                    content2 = str(textEditor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',
                                                   filetypes=(('Text file','*.txt'),('All files','*.*')))
                    url.write(content2)
                    ril.close()
                    window.destroy()
            elif mbox is False:
                window.destroy()
        else:
            window.destroy()
    except:
        return
file.add_command(label = 'New', command = newFile, accelerator = 'Ctrl+N')
file.add_command(label = 'Open', command = openFile, accelerator = 'Ctrl+O')
file.add_command(label = 'Save', command = saveFile, accelerator = 'Ctrl+S')
file.add_command(label = 'Save As', command = saveAs, accelerator = 'Ctrl+Alt+S')
file.add_command(label = 'Exit', command = exitFunc, accelerator = 'Ctrl+Q')

##edit
def findFunc(event = None):

    def find():
        word = findInput.get()
        textEditor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word :
            startPos = '1.0'
            while True:
                startPos = textEditor.search(word, startPos, stopindex=tk.END)
                if(not startPos):
                    break
                endPos = f'{startPos} + {len(word)}c'
                textEditor.tag_add('match', startPos, endPos)
                matches += 1
                startPos = endPos
                textEditor.tag_config('match', foreground = 'red', background = '')

    def replace():
        word = findInput.get()
        replaceText = replaceInput.get()
        content = textEditor.get(1.0,tk.END)
        newContent = content.replace(word,replaceText)
        textEditor.delete(1.0,tk.END)
        textEditor.insert(1.0,newContent)
    
    findDialogue = tk.Toplevel()
    findDialogue.geometry('450x250+500+200')
    findDialogue.resizable(0,0)

    findFrame = ttk.LabelFrame(findDialogue, text = 'Find/Replace')
    findFrame.pack(pady = 20)

    textFindLabel = ttk.Label(findFrame,text = 'Find : ')
    textReplaceLabel = ttk.Label(findFrame,text = 'Replace')

    findInput = ttk.Entry(findFrame,width = 30)
    replaceInput = ttk.Entry(findFrame, width = 30)

    findButton = ttk.Button(findFrame, text = 'Find', command = find)
    replaceButton = ttk.Button(findFrame, text = 'replace', command = replace)

    textFindLabel.grid(row = 0 , column = 0, padx = 4, pady = 4)
    textReplaceLabel.grid(row = 1, column = 0, padx = 4, pady = 4)

    findInput.grid(row = 0, column = 1, padx = 4, pady = 4)
    replaceInput.grid(row = 1, column = 1, padx = 4, pady = 4)

    findButton.grid(row = 2, column = 0, padx = 8, pady = 4)
    replaceButton.grid(row = 2, column = 1, padx = 8, pady = 4)

    findDialogue.mainloop()

def clearAll(evnet = None):
    textEditor.delete(1.0,tk.END)

edit.add_command(label='Copy',command=lambda:textEditor.event_generate("<Control c>"), accelerator='Ctrl+C')
edit.add_command(label='Paste',command=lambda:textEditor.event_generate("<Control v>"), accelerator='Ctrl+V')
edit.add_command(label='Cut',command=lambda:textEditor.event_generate("<Control x>"), accelerator='Ctrl+X')
edit.add_command(label='Clear All', accelerator='Ctrl+ALt+X')
edit.add_command(label='Find', command=findFunc, accelerator='Ctrl+F')

##view
showStatusBar = tk.BooleanVar()
showStatusBar.set(True)
showToolBar = tk.BooleanVar()
showToolBar.set(True)

def hideToolBar():
    global showToolBar
    if showToolBar:
        toolBar.pack_forget()
        showToolBar = False
    else :
        textEditor.pack_forget()
        statusBar.pack_forget()
        toolBar.pack(side = tk.TOP, fill = tk.X)
        textEditor.pack(fill = tk.BOTH, expand = True)
        statusBar.pack(side = tk.BOTTOM)
        sohwToolBar = True

def hideStatusBar():
    global showStatusBar
    if showStatusBar:
        statusBar.pack_forget()
        showStatusBar = False
    else :
        statusBar.pack(side = tk.BOTTOM)
        showStatusBar = True

view.add_checkbutton(label = 'Tool Bar', onvalue = True, offvalue = 0,
                     variable = showToolBar, command  = hideToolBar)
view.add_checkbutton(label = 'Status Bar', onvalue = 1, offvalue = False,
                     variable = showStatusBar, command  = hideStatusBar)
    
##color theme
def changeTheme():
    chooseTheme = themeChoice.get()
    colorTuple = colorDict.get(chooseTheme)
    fgColor, bgColor = colorTuple[0], colorTuple[1]
    textEditor.config(background = bgColor, fg = fgColor)


for i in colorDict:
    colorTheme.add_radiobutton(label = i, variable = themeChoice, command = changeTheme)




#커맨드

window.bind("<Control-n>", newFile)
window.bind("<Control-o>", openFile)
window.bind("<Control-s>", saveFile)
window.bind("<Control-Alt-s>", saveAs)
window.bind("<Control-q>", exitFunc)
window.bind("<Control-f>", findFunc)
window.bind("<Control-Alt-x>", clearAll)

window.protocol('WM_DELETE_WINDOW', exitFunc)


window.mainloop()
