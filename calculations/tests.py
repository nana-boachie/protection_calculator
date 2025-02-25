from django.test import TestCase

from .models import Relay
# Create your tests here.

class RelayTripTimeTest(TestCase):
    def setUp(self):
        # Create test relays with different parameters
        self.iec_relay_inverse = Relay.objects.create(
            name="IEC Inverse Relay", type='oc', standard='iec', curve_type='standard_inverse', tds=0.1, current_setting=100
        )
        self.iec_relay_very_inverse = Relay.objects.create(
            name="IEC Very Inverse Relay", type='oc', standard='iec', curve_type='very_inverse', tds=0.2, current_setting=200
        )
        self.ieee_relay_inverse = Relay.objects.create(
            name="IEEE Inverse Relay", type='oc', standard='ieee', curve_type='moderately_inverse', tds=0.3, current_setting=150
        )
        # ... create more test relays as needed

    def test_iec_inverse_trip_time(self):
        fault_current = 200  # Amperes
        expected_trip_time = self.iec_relay_inverse.calculate_trip_time(fault_current)
        self.assertAlmostEqual(expected_trip_time, 1.003, places=3)  # Compare with expected value (adjust places as needed)

    def test_iec_very_inverse_trip_time(self):
        fault_current = 400
        expected_trip_time = self.iec_relay_very_inverse.calculate_trip_time(fault_current)
        self.assertAlmostEqual(expected_trip_time, 2.7, places=3) # Compare with expected value (adjust places as needed)

    def test_ieee_inverse_trip_time(self):
        fault_current = 300
        expected_trip_time = self.ieee_relay_inverse.calculate_trip_time(fault_current)
        self.assertAlmostEqual(expected_trip_time, 1.141, places=3) # Compare with expected value (adjust places as needed)

    def test_no_oc_relay(self):
        relay = Relay.objects.create(name="Non-OC Relay", type='dist')
        trip_time = relay.calculate_trip_time(1000)
        self.assertIsNone(trip_time)

    def test_missing_parameters(self):
        relay = Relay.objects.create(name="Missing Params Relay", type='oc')  # Missing standard, curve_type, tds
        trip_time = relay.calculate_trip_time(1000)
        self.assertIsNone(trip_time)

    def test_no_trip_current_less_than_pickup(self):
      fault_current = 50 # less than pickup current
      expected_trip_time = self.iec_relay_inverse.calculate_trip_time(fault_current)
      self.assertIsNone(expected_trip_time)
