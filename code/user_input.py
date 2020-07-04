

class UserInput:
    def __init__(self):
        self.miles_driven = 0
        self.kw_hour = 0
        self.therms = 0
        self.mcf = 0
        self.propane = 0
        self.stats_set = False

    def set_miles_driven(self):
        self.miles_driven = float(input("Enter the number of miles you drive in a year: "))

    def set_kw_hour(self):
        self.kw_hour = float(input("Enter the number of kilowatt hours you consume in a month: "))

    def set_therms(self):
        self.therms = float(input("Enter the amount of therms you use in a month: "))

    def set_mcf(self):
        self.mcf = float(input("Enter the amount of mcf you use in a month: "))

    def set_propane(self):
        self.propane = float(input("Enter the amount of propane you use in a year: "))

    def get_miles_driven(self):
        return self.miles_driven

    def get_kw_hour_to_years(self):
        return self.kw_hour * 12

    def get_therms(self):
        return self.therms * 12

    def get_mcf(self):
        return self.mcf * 12

    def get_propane(self):
        return self.propane
