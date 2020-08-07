from tkinter import *


class ApiWindow:
    def __init__(self, master=None):
        # initialize and set Tk windows
        self.master = master.geometry("450x300")
        self.frame = Frame(self.master)

        # call method to create widgets and pack them
        self.create_widgets()

    def create_widgets(self):
        self.header_label = Label(self.master, text="Current air quality statistics in your local area")
        self.loc_label = Label(self.master, text="Data source location:")
        self.co_label = Label(self.master, text="CO:")
        self.h_label = Label(self.master, text="Humidity:")
        self.no2_label = Label(self.master, text="NO2:")
        self.o3_label = Label(self.master, text="O3:")
        self.p_label = Label(self.master, text="Pressure:")
        self.pm10_label = Label(self.master, text="PM 10:")
        self.pm25_label = Label(self.master, text="PM 2.5:")
        self.so2_label = Label(self.master, text="SO2:")
        self.t_label = Label(self.master, text="Temperature:")
        self.wind_label = Label(self.master, text="Wind speed:")

        self.header_label.grid(row=0, column=1)
        self.loc_label.grid(row=1, column=0)
        self.h_label.grid(row=2, column=0)
        self.no2_label.grid(row=3, column=0)
        self.o3_label.grid(row=4, column=0)
        self.p_label.grid(row=5, column=0)
        self.pm10_label.grid(row=6, column=0)
        self.pm25_label.grid(row=7, column=0)
        self.so2_label.grid(row=8, column=0)
        self.t_label.grid(row=9, column=0)
        self.wind_label.grid(row=10, column=0)
        self.co_label.grid(row=11, column=0)


if __name__ == "__main__":
    root_window = Tk()
    root_window.title("api")
    curr_menu = ApiWindow(master=root_window)
    root_window.mainloop()
