from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
# from requests.exceptions import HTTPError
from ArticleReader import *

# Creating a new frame when 'File' is chosen
def file_window():
    f4.pack_forget()
    
    # Opens a new window for browsing and selecting the desired text file
    def browseFiles():
        file_name = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),))

        ent_file_path.insert(0, file_name)
        final_values["input_path"]=ent_file_path.get()

    label_file_path = Label(f3, text = "File Path:")
    label_file_path.grid(row=3,column=0)
    ent_file_path = Entry(f3)
    ent_file_path.grid(row=3,column=1)
    final_values["clear_field"] = ent_file_path
    button_browse = Button(f3,
                        text = "Browse Files",
                        command = browseFiles)
    button_browse.grid(row=3,column=3)
    submit_btn = Button(f3,text = 'Speak', command = extract)
    submit_btn.grid(row=5,column=1)
    f3.pack()

# Creating a new frame when 'Article Link' is chosen
def link_window():
    f3.pack_forget()
    
    # Grabbing the entered URL and the option for downloading the article
    def submit():
        final_values["input_path"]=ent_url.get()
        final_values["save_flag"]=save_file.get()
        extract()

    label_url = Label(f4, text = "URL:")
    label_url.grid(row=3,column=0)
    ent_url = Entry(f4)
    ent_url.grid(row=3,column=1)
    final_values["clear_field"] = ent_url
    save_file = IntVar()
    save_chkbtn = Checkbutton(f4,text = "Download article",variable=save_file,onvalue=1,offvalue = 0)
    save_chkbtn.grid(row=4,column=1)
    submit_btn = Button(f4, text = 'Speak', command = submit)
    submit_btn.grid(row=5, column=1)
    f4.pack()

# Connects the GUI to the backend functions
def extract():
    index = speaker_list.index(selected_spkr.get())
    engine = generate_voice(index, float(selected_rate.get()))
    try:
        if selected_input_type.get()=="File":
            speak_text_file(final_values["input_path"], engine)
        else:
            speak_web_file(final_values["input_path"], final_values["save_flag"], engine)
    except requests.RequestException as e:
        messagebox.showerror(title='INVALID URL', message=f'{e}\nIf not, please re-enter a valid URL')
    except FileNotFoundError as e:
        messagebox.showerror(title='FILE NOT FOUND', message=f'File not found.\nPlease enter a valid path')
    except Exception as e:
        messagebox.showerror(title='ERROR', message=e)
    finally:
        if final_values['clear_field'] != "":
            final_values['clear_field'].delete(0, END)
        final_values["input_path"]=""
 
# Dictionary for saving the values/button names required outside their scope
final_values = {"input_path":"", "save_flag":"", 'clear_field':""}

win = Tk()
win.title("Article Reader")
win.geometry()

# Frame 1
f1 = Frame(win)
heading = Label(f1,text = 'Text to Speech',justify=CENTER)
heading.pack()
f1.pack(side=TOP,fill=BOTH)

# Frame 2
f2 = Frame(win)

# Selecting the speaker using a drop-down menu
speaker_list = ['David','Zira']
selected_spkr = StringVar(f2)
selected_spkr.set(speaker_list[0])
speaker_lbl = Label(f2, text="Select Speaker", pady = 10, justify = RIGHT)
speaker_lbl.grid(row=0,column = 0)
speakers= OptionMenu(f2, selected_spkr, *speaker_list)
speakers.grid(row=0,column=1)

# Selecting the speaker rate using radiobuttons
rate_lbl = Label(f2,text="Select speech rate",padx=10,justify = RIGHT)
rate_lbl.grid(row=1,column = 0)
values = {"Slow" : "0.5",       # Offset values for modifying the rate
        "Medium" : "0.9",
        "Fast" : "1.25"}
selected_rate = StringVar()
selected_rate.set("0")
for col,(text,value) in enumerate(values.items()):
    Radiobutton(f2, text=text, value=value, variable=selected_rate).grid(row=1,column=col+1)

# Selecting the input format
input_lbl= Label(f2,text="Select input format", padx=10, justify = RIGHT)
input_lbl.grid(row=2,column=0)
commands = {"File":file_window, "Article link":link_window}
selected_input_type = StringVar()
selected_input_type.set("1")
for col,(text,command) in enumerate(commands.items()):
    Radiobutton(f2, text=text, value=text, variable=selected_input_type, command=command).grid(row=2,column=col+1)
f2.pack()

# New frames for both the cases
f3 = Frame(win)
f4 = Frame(win)

win.mainloop()