"""
PersonalData, class for specifying data to serialise. Can be extended.
"""

class PersonalData():
    def __init__(self, name=None, address=None, phone=None):
        """
        Constructor for personal data.
        Parameters should have default constructor of None
        """
        self.name = name
        self.address = address
        self.phone = phone

        #self.addresses = {
        #    'billing': address,
        #    # add additional addresses, eg. `'mail': address,`
        #}

        #self.phones = {
        #    'home': phone,
        #    # add additional phone numbers, eg `'work': phone,`
        #}


    #@staticmethod
    #def dict_decoder(input_dict):
    #    import pdb; pdb.set_trace()
    #    return PersonalData(
    #            input_dict['name'],
    #            input_dict['address'],
    #            input_dict['phone'])
