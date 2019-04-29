class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def hashing(self):
        my_dict = {}
        my_dict[self.name] =  self.number 
        
        return '{}'.format(my_dict)


contact1 = Contact('Lucy', '075678')
contact2 = Contact('Caleb', '075678')
contact3 = Contact('Ernest', '075678')

       
print(contact1.hashing())

