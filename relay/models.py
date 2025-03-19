from django.db import models

# Create your models here.


RELAY_PROTECTED_EQUIPMENT = [
    ('tra','Transformer'),
    ('line','Transmission Line')
]

RELAY_CHOICES = [
    ('oc', 'Overcurrent'),  # More descriptive labels
    ('dist', 'Distance'),
    ('diff', 'Differential'),
    ('ref','Restricted Earth Fault')
    # Add other relay types as needed
]
STANDARD_CHOICES = [
    ('iec', 'IEC'),
    ('ieee', 'IEEE'),

]

class Relay(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Name of the relay
    type = models.CharField(max_length=4, choices=RELAY_CHOICES)
    protected_equipment = models.CharField(max_length=4,choices=RELAY_PROTECTED_EQUIPMENT)
    standard = models.CharField(max_length=4, choices=STANDARD_CHOICES, blank=True, null=True)  # Standard (IEC/IEEE)
    curve_type = models.CharField(max_length=20, blank=True, null=True) # e.g., 'inverse', 'very_inverse', 'extremely_inverse'
    tds = models.FloatField(blank=True, null=True) # Time Dial Setting
    current_setting = models.FloatField(blank=True, null=True) # Pickup Current

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.type != 'oc':
            self.standard = None # if not oc, standard is null
            self.curve_type = None
            self.tds = None
            self.current_setting = None
        super().save(*args, **kwargs)


    def calculate_trip_time(self, fault_current):
            if self.type != 'oc' or self.standard is None or self.curve_type is None or self.tds is None or self.current_setting is None:
                return None  # Not an OC relay or missing parameters

            current_in_pu = fault_current / self.current_setting  # Current in per unit
            if current_in_pu <= 1:
              return None # No trip if current is less than pickup current

            if self.standard == 'iec':
                return self._calculate_iec_trip_time(current_in_pu)
            elif self.standard == 'ieee':
                return self._calculate_ieee_trip_time(current_in_pu)
            else:
                return None

    def _calculate_iec_trip_time(self, current_in_pu):
        # IEC Curve Equations (Example - adapt as needed)
        # These are examples, you'll need to use the actual IEC curve equations.
        # Different curves have different formulas.  Consult the IEC standard.

        if self.curve_type == 'standard_inverse':
        #Example Formula
            return self.tds * (0.14 / ((current_in_pu**0.02) - 1) )
        elif self.curve_type == 'very_inverse':
            #Example Formula
            return self.tds * (13.5 / (current_in_pu - 1) )
        elif self.curve_type == 'extremely_inverse':
            #Example Formula
            return self.tds * (80 / ((current_in_pu**2) - 1) )
        elif self.curve_type == 'long_time_standard_inverse':
            #Example Formula
            return self.tds * (120 / (current_in_pu - 1) )
        else:
            return None #Invalid curve type

    def _calculate_ieee_trip_time(self, current_in_pu):
            # IEEE Curve Equations (Example - adapt as needed)
            # These are examples, you'll need to use the actual IEEE curve equations.
            # Different curves have different formulas.  Consult the IEEE standard.

        if self.curve_type == 'moderately_inverse':
            #Example Formula
            return self.tds * (0.0515 / ((current_in_pu**0.02) - 1) + 0.114)
        elif self.curve_type == 'very_inverse':
            #Example Formula
            return self.tds * (19.61 / ((current_in_pu**2) - 1) + 0.491)
        elif self.curve_type == 'extremely_inverse':
            #Example Formula
            return self.tds * (28.2 / ((current_in_pu**2) - 1) + 0.1217)

        # Add more IEEE curve types as needed
        else:
            return None #Invalid curve type


