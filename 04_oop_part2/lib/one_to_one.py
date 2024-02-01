class House:
    def __init__(self, roof_type, sqft, color, price):
        
        ## instance variables (attributes) need to be defined as part of the __init__ method because they are unique to each instance of the class
        self.roof_type = roof_type
        self.sqft = sqft
        self.color = color
        self.price = price
        
        ## some instance variables are not unique to each instance of the class
        self._owner = None
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, People):
            self._owner = new_owner
        else:   
            raise ValueError('Owner must be a person')
        
    def add_feature(self, feature):
        print(f"Adding {feature} to the house")
        
    def is_eligible(self, person):
        if person.age > 18:
            print(f"{person.name} is eligible to buy the house")
            return True
        else:
            return False
    
        
        
class People:
    def __init__(self, name, age):
        self.name = name
        if age > 18:
            self.age = age
        else:
            raise ValueError('Age must be greater than 18')
        self._house = None
        
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, new_house):
        if isinstance(new_house, House):
            self._house = new_house
            new_house.owner = self
        else:
            raise ValueError('House must be a house')
        
if __name__ == "__main__":
    house1 = House('flat', 1500, 'white', 100000)
    house2 = House('slant', 2000, 'blue', 200000)
    house3 = House('slant', 2000, 'blue', 200000)
    
    person1 = People('John', 30)
    person2 = People('Jane', 15)
    
    house1.add_feature('pool')
    house2.add_feature('garden')
    
    house1.owner = person1
    house2.owner = person2
    
    print(house1.owner.name)
    print(house2.owner.name)
    
    person2.house = house3
    print(person2.house.color)
    
    house1.is_eligible(person1)
    house1.is_eligible(person2)
    
    house2.is_eligible(person1)
    house2.is_eligible(person2)
    
    house3.is_eligible(person1)
    house3.is_eligible(person2)