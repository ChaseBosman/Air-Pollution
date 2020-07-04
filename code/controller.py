from user_input import UserInput
from calculations import Calculation
from pollut_api import PollutionApi
from print_carbon_footprint import PrintStatistics


class Controller:
    def __init__(self):
        self.user_info = UserInput()
        self.user_calcs = Calculation()
        self.api_data = PollutionApi()
        self.print_data = PrintStatistics()

    def calculate(self):
        """Calculate exchanges a users pollut_input info with calculations and calculates
        a users pollution."""
        if not self.user_info.stats_set:
            self.get_stats()

        self.print_data.print_kw_hour(self.user_calcs.convert_electricity(self.user_info.get_kw_hour_to_years()))
        self.print_data.print_therms(self.user_calcs.convert_nat_gas_therms(self.user_info.get_therms()))
        self.print_data.print_mcf(self.user_calcs.convert_nat_gas_mcf(self.user_info.get_mcf()))
        self.print_data.print_miles_driven(self.user_calcs.convert_fuel_oil(self.user_info.get_miles_driven()))
        self.print_data.print_propane(self.user_calcs.propane(self.user_info.get_propane()))

    def get_stats(self):
        """"This method is used to obtain a users statistics for the first time"""
        self.user_info.set_miles_driven()
        self.user_info.set_kw_hour()
        self.user_info.set_therms()
        self.user_info.set_mcf()
        self.user_info.set_propane()
        self.user_info.stats_set = True

    def get_api_data(self):
        """This method retrieves and prints current air pollution details"""
        self.api_data.get_api_ip_based()
        self.api_data.get_location()
        self.api_data.read_json_data()


if __name__ == "__main__":
    quit_task = False
    while not quit_task:
        controller = Controller()
        task = input("Type 'C' to calculate data or 'api' to get current data: ")

        if task.lower() == 'c':
            controller.calculate()
        else:
            controller.get_api_data()

        quit_prompt = input("Quit? Type Q to quit, else any other key to stay.")
        if quit_prompt.lower() == 'q':
            quit_task = True


