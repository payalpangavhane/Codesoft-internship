import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update(self, name=None, phone=None, email=None, address=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)

    def view_contacts(self):
        return self.contacts

    def search_contact(self, query):
        return [contact for contact in self.contacts if query in contact.name or query in contact.phone]

    def update_contact(self, contact, name=None, phone=None, email=None, address=None):
        contact.update(name, phone, email, address)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

class ContactBookApp:
    def __init__(self, root):
        self.contact_book = ContactBook()
        self.root = root
        self.root.title("Contact Book")

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.phone_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.email_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.address_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Search:").grid(row=6, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.search_var).grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=7, column=0, columnspan=2, pady=10)

        self.contact_listbox = tk.Listbox(self.root)
        self.contact_listbox.grid(row=0, column=2, rowspan=8, padx=10, pady=5, sticky="nsew")
        self.contact_listbox.bind('<Double-1>', self.on_contact_select)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()
        if name and phone and email and address:
            self.contact_book.add_contact(name, phone, email, address)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_fields()
        else:
            messagebox.showwarning("Input Error", "Please fill all fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_book.view_contacts():
            self.contact_listbox.insert(tk.END, contact)

    def search_contact(self):
        query = self.search_var.get()
        results = self.contact_book.search_contact(query)
        self.contact_listbox.delete(0, tk.END)
        for contact in results:
            self.contact_listbox.insert(tk.END, contact)
        if not results:
            messagebox.showinfo("No Results", "No contacts found.")

    def on_contact_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contact_listbox.get(selected_index[0])
            contact = next(c for c in self.contact_book.view_contacts() if str(c) == contact)
            action = simpledialog.askstring("Action", "Enter 'update' to update or 'delete' to delete:")
            if action == 'update':
                self.update_contact(contact)
            elif action == 'delete':
                self.delete_contact(contact)

    def update_contact(self, contact):
        name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact.name)
        phone = simpledialog.askstring("Update Phone", "Enter new phone:", initialvalue=contact.phone)
        email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact.email)
        address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact.address)
        self.contact_book.update_contact(contact, name, phone, email, address)
        messagebox.showinfo("Success", "Contact updated successfully.")
        self.view_contacts()

    def delete_contact(self, contact):
        self.contact_book.delete_contact(contact)
        messagebox.showinfo("Success", "Contact deleted successfully.")
        self.view_contacts()

    def clear_fields(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
