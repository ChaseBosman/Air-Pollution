
class CarbonFootprintCalcs:

    #ALL emissions factors are based in units of kgCO2/unit
    def convert_electricity(self, kwh_per_year):
        ef = .707
        self.elect_pollut_total = kwh_per_year * ef
        return self.elect_pollut_total

    def convert_nat_gas_therms(self, therms_used):
        ef = 5.3
        self.therms_pollut_total = therms_used * ef
        return self.therms_pollut_total

    def convert_nat_gas_mcf(self, mcf_used):
        ef = 54.9
        self.mcf_pollut_total = mcf_used * ef
        return self.convert_nat_gas_mcf()

    def convert_fuel_oil(self, miles_driven):
        avg_miles = 11486
        ef_per_year_avg = 4630
        self.driven_pollut = miles_driven / avg_miles * ef_per_year_avg
        return self.driven_pollut

    def propane(self, litres_used):
        #per cylinder
        ef = 24
        self.propane_pollut = litres_used * ef
        return self.propane_pollut
