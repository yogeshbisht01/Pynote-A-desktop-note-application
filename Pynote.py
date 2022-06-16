import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename 
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os
import pyttsx3 
import speech_recognition as sr 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)  # 1 for female voice & 0 for male voice  


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.minsize(870,500)
main_application.maxsize(870,500)

 

main_application.title('Pynote')
main_application.wm_iconbitmap('icon.ico')


############################################## main menu ###################################################

main_menu = tk.Menu()

#file 
new_icon = tk.PhotoImage(file='')
open_icon = tk.PhotoImage(file='')
save_icon = tk.PhotoImage(file='')
save_as_icon = tk.PhotoImage(file='')
exit_icon = tk.PhotoImage(file='')  

file = tk.Menu(main_menu, tearoff=False)



#####edit  
copy_icon = tk.PhotoImage(file='')
paste_icon = tk.PhotoImage(file='')
cut_icon = tk.PhotoImage(file='')
undo_icon = tk.PhotoImage(file='')
redo_icon = tk.PhotoImage(file='')
clear_all_icon = tk.PhotoImage(file='')
find_icon = tk.PhotoImage(file='')

edit = tk.Menu(main_menu, tearoff=False)


########view 
tool_bar_icon = tk.PhotoImage(file='')
status_bar_icon = tk.PhotoImage(file='')
view = tk.Menu(main_menu, tearoff=False)


########colortheme 
light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
red_icon = tk.PhotoImage(file='icons/red.png')
night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_plus_icon,red_icon,night_blue_icon)

color_dict = {
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

#####about
def about():
 main_appli = tk.Tk()
 main_appli.geometry('300x100')
 main_appli.minsize(300, 100)
 main_appli.maxsize(300, 100)
 main_appli.config(bg="White")
 main_appli.title('About')
 Label(main_appli,text="Pynote - A Desktop Notes Application™\n\nTechnology Used </> :  Python 3\n\nDeveloper 💻 :  Yogesh Singh Bisht  ",font="Bahnschrift 11",bg="white",justify=LEFT).pack()

# cascade 
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='Themes', menu=color_theme)
main_menu.add_cascade(label="About ℹ",command=about)


############################################## toolbar  ###################################################


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font box 
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


## size box 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(18)
font_size.grid(row=0, column=1, padx=5)

## bold button 
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

##voiceassistant
voice_assis_icon = tk.PhotoImage(file='icons/voice1.png')
voice_assis_btn = ttk.Button(tool_bar, image=voice_assis_icon)
voice_assis_btn.grid(row=0, column=9, padx=5)

##nightmode
night_mode_icon = tk.PhotoImage(file='icons/night_mode.png')
night_mode_btn = ttk.Button(tool_bar, image=night_mode_icon)
night_mode_btn.grid(row=0, column=10, padx=5)

##lightmode
light_mode_icon = tk.PhotoImage(file='icons/light_mode.png')
light_mode_btn = ttk.Button(tool_bar,image=light_mode_icon)
light_mode_btn.grid(row=0, column=11, padx=5)

##backup
backup_mode_icon = tk.PhotoImage(file='icons/drive.png')
backup_mode_btn = ttk.Button(tool_bar,image=backup_mode_icon)
backup_mode_btn.grid(row=0, column=12, padx=5)

#mail
share_mode_icon = tk.PhotoImage(file='icons/gmail.png')
share_mode_btn = ttk.Button(tool_bar,image=share_mode_icon)
share_mode_btn.grid(row=0, column=13, padx=5)



text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT,undo=True)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set,wrap="none")

def voice_assis():

    def speak(audio):
     engine.say(audio)                            #voice function
     engine.runAndWait() 

    def wishMe():
     speak("what can i do sir")

    def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        r.pause_threshold = 0.8            
        audio = r.listen(source)
        
     try:   
        query = r.recognize_google(audio, language='en-in')
   
     except Exception as e:
    
        return "None"
     return query
  

    if __name__ == "__main__":
     wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'close' in query:                                            
            speak('sure sir, closing application')
            main_application.destroy()

        elif 'about' in query:
            about()
            speak('here it is')
        else:
         break

voice_assis_btn.configure(command=voice_assis)

# font family and font size functionality 
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality 

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)


## font color functionality 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)

def night_mode():
    def speak(audio):
     engine.say(audio)                            #voice function
     engine.runAndWait() 
    night_icon = tk.PhotoImage(file='icons/dark.png')
    text_editor.config(background='#2d2d2d', fg='#c4c4c4')
    speak('dark mode enabled')
night_mode_btn.configure(command=night_mode)


def light_mode():
    def speak(audio):
     engine.say(audio)                            #voice function
     engine.runAndWait() 
    light_default_icon = tk.PhotoImage(file='icons/light_default.png')
    text_editor.config(background='#ffffff', fg='#000000')
    speak('light mode enabled')
light_mode_btn.configure(command=light_mode)


def backup_mode():
    def speak(audio):
     engine.say(audio)                            #voice function
     engine.runAndWait()
    speak("select your note to backup")
    import drive
    speak('note uploaded')
backup_mode_btn.configure(command=backup_mode)


def share_mode():
    def speak(audio):
     engine.say(audio)                            #voice function
     engine.runAndWait()
    speak("select your note to share")
    import mail
    speak('note shared')
share_mode_btn.configure(command=share_mode)


##################################################################################################################



text_editor.configure(font=('Arial', 12))
##statusbar

status_bar = ttk.Label(main_application, text = 'Status Bar')

text_changed = False 
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True 
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)

status_bar.pack(side=tk.BOTTOM)
show_statusbar = True


# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## main menu functinality ###################################################

## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    text_editor.delete("1.0", tk.END)

## file commands 
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


## open functionality
def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)


## save file 
def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 

file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return 


file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+A+S', command=save_as)


## exit functionality 
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return 
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands 
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Undo',  compound=tk.LEFT, accelerator='Ctrl+Z', command=lambda:text_editor.event_generate("<Control z>"))
edit.add_command(label='Redo', compound=tk.LEFT, accelerator='Ctrl+Y', command=lambda:text_editor.event_generate("<Control y>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+A+X', command= lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)



## color theme 
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color) 
count = 0 
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1 


# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------

main_application.config(menu=main_menu)

#### bind shortcut keys 
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


main_application.mainloop()