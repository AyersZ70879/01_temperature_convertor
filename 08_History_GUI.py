from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['this is a string, '
                              'this is a string']

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # History Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial", "12"), padx=5, pady=5,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press the cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history Heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History", font="arial 19 bold",
                                     bg=background)
        self.how_heading.grid(row=0)

        # History text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                               "calculations. Please use the "
                                                               "export button to create a text file"
                                                               "of all your calculations for this "
                                                               "session",
                                      justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(column=0, row=1)

        # History Output goes here... (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, bg=background,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_dismiss_button = Button(self.export_dismiss_frame, text="Export", font="Arial 12 bold")
        self.export_dismiss_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss", font="Arial 12 bold",
                                         command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
