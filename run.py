from tkinter import *
from tkinter.ttk import *
from functools import partial

class Person():
    def __init__(self, root):
        self.root = root
        self.name = None
        self.adress = None
        self.phone_number = None
        self.id_number = None
        self.face = None
      
    def all_info(self):
        return [self.name, self.adress, self.phone_number,
                self.id_number, self.face]
    
    def update_info(self, value, index):
        if index == 0:
            self.name = value
        elif index == 1:
            self.adress = value
        elif index == 2:
            self.phone_number = value
        elif index == 3:
            self.id_number = value          
    
def user_management(values):
    if listbox.curselection() != '':
        listbox_selcted = listbox.get(listbox.curselection())
        
        # If new person is created
        if listbox_selcted == 'Add Person +':
            users.insert(0, Person(root))
            for index, value in enumerate(values):
                users[0].update_info(value, index)
            listbox.insert(0, users[0].name)
            
            # Selected newly created person
            listbox.selection_clear(0, END)
            listbox.selection_set(0)

        # Update already created person
        else:
            for index, value in enumerate(values):
                users[listbox.curselection()[0]].update_info(value, index)
            
            set_entry_information(listbox.curselection()[0])

def set_entry_information(selected_index):        
    listbox.delete(selected_index)
    listbox.insert(selected_index, users[selected_index].name)
    listbox.selection_clear(0, END)
    listbox.selection_set(selected_index)

def get_entry_information():
    lst = []    
    for entry in entrys:
        lst.append(entry.get())
    
    return lst

def clickEvent(event):
    # If add person
    if listbox.get(listbox.curselection()) == 'Add Person +':
        for entry in entrys:
            entry.delete(0,'end')
            entry.insert(0, '')
    
    else:
        entry_info = users[listbox.curselection()[0]].all_info()
        for var, entry in zip(entry_info, entrys):
            entry.delete(0,'end')
            entry.insert(0, var)

# Window Made        
root = Tk()
root.configure(bg='#dcdad5')
style = Style()
style.theme_use('clam')

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

# Menu
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)
file_menu = Menu(menubar, tearoff=False)

file_menu.add_command(
    label="Save"
)

file_menu.add_command(
    label="Reset all"
)

file_menu.add_command(
    label="Exit"
)

menubar.add_cascade(
    label='File',
    menu=file_menu
)

# Users
users = []

# Listbox
listbox = Listbox(root, exportselection=False)
listbox.place(anchor='center' ,relx=0.1, rely=0.5, relheight=0.9, relwidth=0.15)
listbox.bind('<<ListboxSelect>>', clickEvent)

# Add person choice
listbox.insert(0, 'Add Person +')

# Information boxes
label_text = ['Name', 'Adress', 'Phone nummber', 'ID number']
info_frames = []
labels = []
entrys = []

for index, text in enumerate(label_text):
    info_frames.append(Frame(root))
    labels.append(Label(info_frames[index], text=text))
    entrys.append(Entry(info_frames[index]))
    
    labels[index].pack() 
    entrys[index].pack()
    
for index in range(len(label_text)):    
    info_frames[index].pack()

# Save and Cancel
button_frame = Frame(root)
Button(button_frame, text='Save', command=lambda : (user_management(get_entry_information()))).pack()
Button(button_frame, text='Cancel').pack()

button_frame.pack()

root.mainloop()
      