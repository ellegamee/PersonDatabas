from tkinter import *

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

root.mainloop()
      