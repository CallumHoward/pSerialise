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
