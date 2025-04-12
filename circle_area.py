import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math

def populate_main_window(frm_main):
    """Populate the main window with widgets."""
    # Create a label that displays "Radius"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create an integer entry box for the radius
    ent_radius = IntEntry(frm_main, width=4, lower_bound=1)

    # Create a label that displays "Area:"
    lbl_area_label = Label(frm_main, text="Area:")

    # Create a label that will display the calculated area
    lbl_area_result = Label(frm_main, width=10)

    # Create a label for the units
    lbl_area_units = Label(frm_main, text="square meters")

    # Create the Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Layout widgets
    lbl_radius.grid(row=0, column=0, padx=3, pady=3, sticky="e")
    ent_radius.grid(row=0, column=1, padx=3, pady=3)

    lbl_area_label.grid(row=1, column=0, padx=3, pady=3, sticky="e")
    lbl_area_result.grid(row=1, column=1, padx=3, pady=3)
    lbl_area_units.grid(row=1, column=2, padx=3, pady=3, sticky="w")

    btn_clear.grid(row=2, column=0, columnspan=3, padx=3, pady=6, sticky="w")

    def calculate(event):
        """Compute and display the area of the circle."""
        try:
            radius = ent_radius.get()
            area = math.pi * radius ** 2
            lbl_area_result.config(text=f"{area:.2f}")
        except ValueError:
            lbl_area_result.config(text="")

    def clear():
        """Clear all inputs and outputs."""
        ent_radius.clear()
        lbl_area_result.config(text="")
        ent_radius.focus()

    # Bind calculate to key release in radius entry
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind clear to the Clear button
    btn_clear.config(command=clear)

    # Set initial focus
    ent_radius.focus()

def main():
    # Create the Tk root object.
    root = tk.Tk()
 
    # Create the main window (frame).
    frm_main = Frame(root)
    frm_main.master.title("Circle Area Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
 
    # Populate the main window with widgets.
    populate_main_window(frm_main)
 
    # Start the tkinter event loop.
    root.mainloop()    

if __name__ == "__main__":
    main()

