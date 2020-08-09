import unittest
import sys
import os

def get_abs_dir_for_module(*args):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), *args)
repo_dir = get_abs_dir_for_module("..")
sys.path.append(repo_dir)
import src.calculation as calculation

from calculation import Calculation


class TestCalcs(unittest.TestCase):

    def test_electricity_conversion(self):
        """
        Electricity conversion to pollution units
        """
        calcs = calculation.Calculation()
        result = calcs.convert_electricity(2)
        self.assertEqual(result, 2 * .707)

    def test_therms_conversion(self):
        """
        therms conversion to pollution units
        """
        calcs = calculation.Calculation()
        result = calcs.convert_nat_gas_therms(2)
        self.assertEqual(result, 2 * 5.3)

    def test_mcf_conversion(self):
        """
        mcf conversion to pollution units
        """
        calcs = calculation.Calculation()
        result = calcs.convert_nat_gas_mcf(2)
        self.assertEqual(result, 2 * 54.9)

    def test_fuel_conversion(self):
        """
        test_fuel_conversion conversion to pollution units
        """
        calcs = calculation.Calculation()
        result = calcs.convert_fuel_oil(11486)
        self.assertEqual(result, 4630)

    def test_propane_conversion(self):
        """
        propane conversion to pollution units
        """
        calcs = calculation.Calculation()
        result = calcs.propane(2)
        self.assertEqual(result, 2 * 24)


if __name__ == '__main__':
    unittest.main()