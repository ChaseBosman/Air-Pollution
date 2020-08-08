from tkinter import *
from pollution_api import PollutionApi


class ApiWindow(Toplevel):
    def __init__(self):
        self.top = Toplevel.__init__(self)
        self.geometry("450x300")

        self.api_data = PollutionApi()
        # call method to create widgets
        self.create_widgets()
        self.display_widgets()

    def create_widgets(self):
        self.header_label = Label(self, text="Current air quality statistics in your area")

        self.loc_label = Label(self, text="Data source location:")
        self.co_label = Label(self, text="CO:")
        self.h_label = Label(self, text="Humidity:")
        self.no2_label = Label(self, text="NO2:")
        self.o3_label = Label(self, text="O3:")
        self.p_label = Label(self, text="Pressure:")
        self.pm10_label = Label(self, text="PM 10:")
        self.pm25_label = Label(self, text="PM 2.5:")
        self.so2_label = Label(self, text="SO2:")
        self.t_label = Label(self, text="Temperature:")
        self.wind_label = Label(self, text="Wind speed:")

        self.loc_display = Label(self, text=self.api_data.get_location())
        self.co_display = Label(self, text=self.api_data.get_co())
        self.h_display = Label(self, text=self.api_data.get_h())
        self.no2_display = Label(self, text=self.api_data.get_no2())
        self.o3_display = Label(self, text=self.api_data.get_o3())
        self.p_display = Label(self, text=self.api_data.get_p())
        self.pm10_display = Label(self, text=self.api_data.get_pm10())
        self.pm25_display = Label(self, text=self.api_data.get_pm25())
        self.so2_display = Label(self, text=self.api_data.get_so2())
        self.t_display = Label(self, text=self.api_data.get_t())
        self.wind_display = Label(self, text=self.api_data.get_w())

    def display_widgets(self):
        self.header_label.grid(row=0, column=1, pady=8)

        self.loc_label.grid(row=1, column=0, sticky=E)
        self.h_label.grid(row=2, column=0, sticky=E)
        self.no2_label.grid(row=3, column=0, sticky=E)
        self.o3_label.grid(row=4, column=0, sticky=E)
        self.p_label.grid(row=5, column=0, sticky=E)
        self.pm10_label.grid(row=6, column=0, sticky=E)
        self.pm25_label.grid(row=7, column=0, sticky=E)
        self.so2_label.grid(row=8, column=0, sticky=E)
        self.t_label.grid(row=9, column=0, sticky=E)
        self.wind_label.grid(row=10, column=0, sticky=E)
        self.co_label.grid(row=11, column=0, sticky=E)

        self.loc_display.grid(row=1, column=1)
        self.h_display.grid(row=2, column=1)
        self.no2_display.grid(row=3, column=1)
        self.o3_display.grid(row=4, column=1)
        self.p_display.grid(row=5, column=1)
        self.pm10_display.grid(row=6, column=1)
        self.pm25_display.grid(row=7, column=1)
        self.so2_display.grid(row=8, column=1)
        self.t_display.grid(row=9, column=1)
        self.wind_display.grid(row=10, column=1)
        self.co_display.grid(row=11, column=1)


