from tkinter import *
from tkinter.ttk import *
from functools import partial

class Person():
    def __init__(self, root):
        self.root = root
        self.name = "name_self"
        self.adress = ""
        self.phone_number = ""
        self.id_number = ""
        self.face = ""
      
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
    
def user_management(values, bool):
    listbox_selcted = listbox.get(listbox.curselection())
    # Update already created person
    if bool == True:
        pass
    
    # If new person is created
    elif bool != True and listbox_selcted == 'Add Person':
        users.append(Person(root))
        for index, key in enumerate(values):
            users[-1].update_info(values[key], index)
        
        #print('name', users[-1].name)
        listbox.insert(0, users[-1].name)

def entry_information():
    lst = {}    
    for key, (index, entry) in zip(label_text, enumerate(entrys)):
        lst[f'{label_text[key]}'] = entry.get()
    
    return lst

# Window Made        
root = Tk()
root.configure(bg="#dcdad5")
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

# Users
users = []

# Listbox
listbox = Listbox(root)
listbox.place(anchor="center" ,relx=0.1, rely=0.5, relheight=0.9, relwidth=0.15)

# Add person choice
listbox.insert(0, 'Add Person')

# Information boxes
label_text = {'Name': 'name', 'Adress': 'adress', 'Phone nummber': 'phone_number', 'ID number': 'id_number'}
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
Button(button_frame, text="Save", command=lambda : (user_management(entry_information(), False))).pack()
Button(button_frame, text="Cancel").pack()

button_frame.pack()

root.mainloop()
      