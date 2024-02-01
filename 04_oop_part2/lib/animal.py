class Animal:
    def __init__(self, name, color, size):
        self.name= name
        self.color= color
        self.size= size
        
    def pet_animal(self):
        print(f"Petting {self.name}")
        
class Friend:
    def __init__(self, name, status, duration):
        self.status = status
        self.duration = duration
        self.name = name
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        available_status = ['friend', 'enemy', 'neutral']
        if new_status in available_status:
            self._status = new_status
        else:
            raise ValueError('Status not available')
        
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, new_duration):
        if new_duration > 0:
            self._duration = new_duration
        else:
            raise ValueError('Duration cannot be negative')
        
    def length_of_friendship(self):
        print(f"Length of friendship is {self.duration} years")
    
class Dog(Animal):
    def __init__(self, name, color, size, breed, age):
        super().__init__(name, color, size)
        self.breed= breed
        self.age= age
        
    def pet_animal(self):
        super().pet_animal()
        print(f"{self.name} wags tail")
        
class Bird(Animal, Friend):
    def __init__(self, name, color, size, habitat, status, duration):
        # Friend.__init__(self, name, status, duration)
        # super().__init__(name, color, size,)
        Animal.__init__(self, name, color, size)
        Friend.__init__(self, name, status, duration)
        self.habitat = habitat
        
        
        
        
pigeon = Bird("Pigeon", "grey", "small", "urban", "friend", 3)

# Accessing attributes from Animal class
print(pigeon.name)
print(pigeon.color)
print(pigeon.size)

# Accessing attributes from Friend class
print(pigeon.status)
print(pigeon.duration)

# Accessing methods from Animal class
pigeon.pet_animal()

# Accessing methods from Friend class
pigeon.length_of_friendship()

