from tkinter import *
from tkinter.ttk import *

class Person():
    def __init__(self, root):
        self.root = root
        self.name
        self.adress
        self.phone_number
        self.id_number
        self.face
      
    def all_info(self):
        return [self.name, self.adress, self.phone_number,
                self.id_number, self.face]
    
    def update_info(self, varible, value):
        varible_dict = {'name': self.name, 'adress': self.adress, 'phone_number': self.phone_number,
               'id_number': self.id_number, 'face': self.face}
        
        varible_dict[varible] = value
        root.update()

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if name_entry.get() == 'Enter Name':
       name_entry.delete(0, "end") # delete all the text in the entry
       name_entry.insert(0, '') #Insert blank for user input

def on_focusout(event):
    if name_entry.get() == '':
        name_entry.insert(0, 'Enter Name')

# Window Made        
root = Tk()

# Display size
screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())

# Window settings
root.title('Person Database')

top_padding = round(screen_height * 0.138888889)
height = round(screen_height * 0.694444444)
left_padding = round(screen_width * 0.15625)
width = round(screen_width * 0.625)
root.geometry(f'{width}x{height}+{left_padding}+{top_padding}')

# Users
users = []

# Listbox
listbox = Listbox(root)
listbox.place(anchor="center" ,relx=0.1, rely=0.5, relheight=0.9, relwidth=0.15)

# Add person choice
listbox.insert(0, 'Add Person')

# Information boxes
name_label = Label(text="Name")

name_entry = Entry(text="Type name")
name_entry.insert(0, 'Enter your user name...')
name_entry.bind('<FocusIn>', on_entry_click)
name_entry.bind('<FocusOut>', on_focusout)

name_entry.pack()

root.mainloop()
      