# Import libraries
from tkinter import *

# Set Constants
FONT = ("Arial", 12, "normal")

# Initialize our classes
window = Tk()

# Set up the screen
window.title("Miles to KM Converter")
window.minsize(width=300, height=150)
window.config(padx=150, pady=50)

# Miles Entry label
miles_input = Entry(width=10)
miles_input.grid(column=0,row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=1,row=0)

# Km Output label
km_output = Label(text="______________",font=FONT )
km_output.grid(row=1, column=0)
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=1)

# Calculate function
def convert_miles_to_km() -> None:
    """
    Summary:
        Takes the tkinter Entry.get() and converts miles to KM
        Changes the text on the km_output to = kilometers
    Returns:
        None
    Called by:
        calc_button 
    """
    try:
        miles = miles_input.get()
        kilometers = round(float(miles) * 1.6)
        km_output.config(text=kilometers)
    except Exception as e:
        print("Error", str(e))

# Calculate Button
calc_button = Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(row=2, column=0)

# Keep screen open until closed
window.mainloop()