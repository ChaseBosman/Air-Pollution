import unittest
import calculations


class TestCalcs(unittest.TestCase):

    def test_electricity_conversion(self):
        """
        Test that the addition of two integers returns the correct total
        """
        calcs = calculations.Calculations()
        result = calcs.convert_electricity(2)
        self.assertEqual(result, 2 * .707)

    def test_therms_conversion(self):
        """
        Test that the addition of two integers returns the correct total
        """
        calcs = calculations.Calculations()
        result = calcs.convert_nat_gas_therms(2)
        self.assertEqual(result, 2 * 5.3)

    def test_mcf_conversion(self):
        """
        Test that the addition of two integers returns the correct total
        """
        calcs = calculations.Calculations()
        result = calcs.convert_nat_gas_mcf(2)
        self.assertEqual(result, 2 * 54.9)

    def test_fuel_conversion(self):
        """
        Test that the addition of two integers returns the correct total
        """
        calcs = calculations.Calculations()
        result = calcs.convert_fuel_oil(11486)
        self.assertEqual(result, 4630)

    def test_propane_conversion(self):
        """
        Test that the addition of two integers returns the correct total
        """
        calcs = calculations.Calculations()
        result = calcs.propane(2)
        self.assertEqual(result, 2 * 24)