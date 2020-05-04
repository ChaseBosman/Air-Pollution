

class UserInput:
    def __init__(self):
        self.miles_driven = 0
        self.kw_hour = 0
        self.therms = 0
        self.mcf = 0
        self.propane = 0

    def get_miles_driven(self):
        self.miles_driven = input("Enter the number of miles you drive in a year")
        return self.miles_driven

    def get_kw_hour(self):
        self.kw_hour = input("Enter the number of kilowatt hours you consume in a year")
        return self.kw_hour * 12

    def get_therms(self):
        self.therms = input("Enter the amount of therms you use in a year")
        return self.therms

    def mcf(self):
        self.mcf = input("Enter the amount of mcf you use in a year")
        return self.mcf

    def propane(self):
        self.propane = input("Enter the amount of propane you use in a year")
        return self.propane
