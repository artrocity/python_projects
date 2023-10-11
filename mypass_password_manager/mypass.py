# Import Libraries
from tkinter import *
from tkinter import messagebox
from mypass_password import PasswordManager


# Define Constants
FONT = ("Courier", 14, "normal")

# Initialize classes
window = Tk()
canvas = Canvas(width=200, height=200)

# Load photos
try:
    logo_image = PhotoImage(file="logo.png")
    photo = PhotoImage(file="logo_icon.png")
except FileNotFoundError as e:
    print("Error: ", str(e))

# Save all the entries to a csv file
def save_to_csv() :
    """
    Summary:
        Uses the PasswordManager Class to get the entries for the website, username, and password
        Verifies the inputs all have a len > 0, Confirms if the user wants to save them
        Saves entries via PasswordManager save_entries method
    Returns:
        None
    Called By:
        add_entry_button command
    """
    web = pass_manager.get_website()
    username = pass_manager.get_username()
    passwd = pass_manager.get_password()

    if len(web) == 0 or len(username) == 0 or len(passwd) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields")
    else:
        save_changes = messagebox.askokcancel(title="Confirm Changes", message=f"Save these Details: \nWebsite: {web} "
                                 f"\nUsername: {username}"
                                 f"\nPassword: {passwd}"
                                 f"\nPress 'OK' to save")
        if save_changes:
            pass_manager.save_entries()
            website_input.delete(0, END)
            password_input.delete(0, END)

# Generate a random password
def generate_password() -> str:
    """
    Summary:
        Calls the generate password method from the PasswordManager class
    Returns:
        str: Random Password
    Called By:
        generate_password_button command
    """
    password = pass_manager.generate_password()
    password_input.insert(END, password)

# Search for pre-saved website, username, and password entries
def get_entries():
    """
    Summary:
        Retrieves the website entry and searches to see if website is in the passwords.json
        Dictionary via get_website()
        If its located, passes the website to the retrieve_entries() method from the pass_manager class
        and saves the dictionary to a variable called entry
        Then shows the user the entry results via a messagebox
    Return:
        None
    Called By:
        search_button
    """
    # Obtain the website entry
    website = pass_manager.get_website()

    # Attempt to retrieve associated dictionary values from the website key
    try:
        entry = pass_manager.retrieve_entries(website)
    except KeyError as e:
        messagebox.showerror(title="Website not found", message=f"Cant not find any entries for the website: {website}")
    else:
        messagebox.showinfo(title=f"Information for: {website}", message=f"Website: {website}\n"
                                                                        f"Username: {entry['Username']}\n"
                                                                        f"Password: {entry['Password']}\n")

    
# Setup the file icon
window.wm_iconphoto(False, photo)

# Setup the screen
window.title("MyPass Password Manager")
window.config(padx=60, pady=60)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=1, column=2)

# Website/Search label and text entry
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=2, column=1)

website_input = Entry(width=20)
website_input.focus()
website_input.grid(row=2, column=2)

search_button = Button(text="Search", width=11, command=get_entries)
search_button.grid(row=2, column=3, sticky="EW")

# Email/Username label and text entry
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(row=3, column=1)

username_input = Entry(width=35)
username_input.insert(0, "myemail@gmail.com")
username_input.grid(row=3, column=2, columnspan=2)

# Password label, text entry, and generate password button
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=4 ,column=1)

password_input = Entry(width=20, show="*")
password_input.grid(row=4, column=2)

generate_password_button = Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(row=4, column=3, sticky="EW")

# Add Entry
add_entry_button = Button(text="Add", width=32, command=save_to_csv)
add_entry_button.grid(row=5, column=2, columnspan=2)

#Pass all the information to the PasswordManager Class
pass_manager = PasswordManager(website_input,username_input, password_input)

# Keep window open until closed
window.mainloop()