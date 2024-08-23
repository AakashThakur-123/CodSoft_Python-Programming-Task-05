import tkinter as tk
from tkinter import messagebox

# Initialize contact list
contacts = {}

# Functions
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def view_contacts():
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{name}: {details['phone']}")

def search_contact():
    search_query = entry_search.get()
    listbox_contacts.delete(0, tk.END)
    for name, details in contacts.items():
        if search_query.lower() in name.lower() or search_query in details['phone']:
            listbox_contacts.insert(tk.END, f"{name}: {details['phone']}")

def update_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0].strip()
        if name in contacts:
            contacts[name] = {'phone': entry_phone.get(), 'email': entry_email.get(), 'address': entry_address.get()}
            messagebox.showinfo("Success", "Contact updated successfully!")
            clear_entries()
            view_contacts()

def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(":")[0].strip()
        if name in contacts:
            del contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            view_contacts()

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Manager")

# Labels and Entries
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=4, column=0, columnspan=2, pady=5)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.grid(row=5, column=0, columnspan=2, pady=5)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=6, column=0, columnspan=2, pady=5)

# Contact Listbox
listbox_contacts = tk.Listbox(root, height=10, width=50)
listbox_contacts.grid(row=7, column=0, columnspan=2, pady=5)

# Search bar
entry_search = tk.Entry(root)
entry_search.grid(row=8, column=0, padx=5, pady=5)

btn_search = tk.Button(root, text="Search Contact", command=search_contact)
btn_search.grid(row=8, column=1, padx=5, pady=5)

# Start the GUI
root.mainloop()
