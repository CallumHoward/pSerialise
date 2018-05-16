"""
PersonalData, class for specifying data to serialise. Can be extended.
"""

class PersonalData():
    def __init__(self, name, address, phone):
        self.name = name

        self.addresses = {
            'billing': address,
            # add additional addresses, eg. `'mail': address,`
        }

        self.phones = {
            'home': phone,
            # add additional phone numbers, eg `'work': phone,`
        }
