from tkinter import *
from api_window import ApiWindow
from compute_window import ComputeWindow


class MainWindowSelect:

    def __init__(self, master=None):
        # initialize and set Tk windows
        self.master = master.geometry("300x200")
        self.frame = Frame(self.master)

        # call method to create widgets and pack them
        self.create_widgets()
        self.frame.pack(fill=BOTH, expand=YES)

    @staticmethod
    def open_api_screen():
        """This method creates a new ApiWindow object, found in compute_window.py (opens api window)"""
        ApiWindow()

    @staticmethod
    def open_compute_screen():
        """This method creates a new ComputeWindow object, found in compute_window.py (opens computation window)"""
        ComputeWindow()

    def create_widgets(self):
        # Two buttons, one to visit the API page and one for computing carbon footprint
        self.compute_but = Button(self.frame, text="Compute Your Carbon Footprint", command=lambda:
                            self.open_compute_screen()).pack(side=TOP, expand=YES)
        self.api_but = Button(self.frame, text="Find Current Pollution Levels", command=lambda:
                            self.open_api_screen()).pack(side=TOP, expand=YES)


if __name__ == "__main__":
    root_window = Tk()
    root_window.title("Clean Air")
    curr_menu = MainWindowSelect(master=root_window)
    root_window.mainloop()
