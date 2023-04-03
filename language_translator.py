import tkinter as tk
from tkinter import *
from tkinter import ttk, END
from translate import Translator

mainWindow = tk.Tk()
mainWindow.title('Language Translator App')
mainWindow.geometry('600x550')
mainWindow.resizable(False, False)
mainWindow.attributes('-alpha', 0.9)
mainWindow.config(bg='orange')
mainWindow.iconbitmap()

# layout window
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=2)


# converts text into desired selected language
def display_translation(e):
    translator = Translator(to_lang=languageSelector.get())
    translate_text = translator.translate(input_textfield.get(1.0, END))
    translation_label.config(text=translate_text)


def clear_field():
    input_textfield.delete("1.0", "end")
    translation_label.config(text=" ")


# language selector

language_selection_label = tk.Label(mainWindow, background='orange', text='Select Language', font=('Bradley Hand', 18))
language_selection_label.grid(column=0, row=0, sticky=tk.W, pady=45, padx=25)

language_var = tk.StringVar()
languageSelector = ttk.Combobox(mainWindow, textvariable=language_var, width=30, height=3)
languageSelector.grid(columnspan=1, row=1, sticky=tk.W, pady=5, padx=25)

# add values to combobox
# get the first to letters of each word
languageSelector['values'] = ['Arabic', 'Chinese', 'French', 'Persian','Portuguese', 'Czech', 'Hebrew', 'Slovak']
languageSelector['state'] = 'readonly'

# userinput label
userInput_label = tk.Label(mainWindow, background='orange', text='Enter word or sentence to translate', font= ('Bradley Hand', 18))
userInput_label.grid(column=0, row=2, sticky=tk.N, pady=25, padx=15)

input_textfield = tk.Text(mainWindow, height=6, width=20)
input_textfield.grid(columnspan=3, row=3, sticky=tk.EW, padx=20)


# translation label
translation_label = tk.Label(mainWindow, height=6, background='orange')
translation_label.grid(columnspan=3, row=4, sticky=tk.EW, padx=15, pady=25)

clear_button = tk.Button(mainWindow, text='Clear', bg='#0052cc', height=3, width=100, command=clear_field)
clear_button.grid(columnspan=12, pady=20, sticky=tk.S)

# bind combobox
input_textfield.bind("<Key>", display_translation)



mainWindow.mainloop()
#if __name__ == '__main__':