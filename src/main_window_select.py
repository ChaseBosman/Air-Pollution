from tkinter import *
from api_window import ApiWindow


class MainWindowSelect:

    def __init__(self, master=None):
        # initialize and set Tk windows
        self.master = master.geometry("300x200")
        self.frame = Frame(self.master)

        # call method to create widgets and pack them
        self.create_widgets()
        self.frame.pack(fill=BOTH, expand=YES)

    def open_api_screen(self):
        self.new_window = ApiWindow()

    def open_compute_screen(self):
        """This method will eventually be implemented to open the computation screen"""
        pass

    def create_widgets(self):
        # Single Label
        self.tbl_label = Label(self.frame, text="Select a menu option:").pack(side=TOP, expand=YES)
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
