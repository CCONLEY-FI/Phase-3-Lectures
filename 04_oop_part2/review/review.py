# import sys
# #!/usr/bin/env python3

# # Create a class
# # Create a method
# # Global variables
# # Properties, we can do any checks in here!!
# # Decorators

# # Review property underscore

# #Create python environments

# class Bird:
#     all_birds = []
#     def __init__(self, size, species, color, habitat, name=None):
#         self.size = size
#         self.species = species
#         self.color = color
#         self.habitat = habitat
#         self.name = name
#         Bird.all_birds.append(self)
        
#     @property
#     def get_color(self):
#         return self._color
    
#     @get_color.setter
#     def get_color(self, new_color):
#         available_colors = ['red', 'blue', 'green', 'black', 'white']
#         if new_color in available_colors:
#             self._color = new_color
#         else:
#             raise ValueError('Color not available')
        
#     @property
#     def get_species(self):
#         return self._species
    
#     @get_species.setter
#     def set_species(self):
#         raise Exception('You cannot change the species')
    
#     #instance method
#     def migrate(self, new_habitat):
#         print(f"migrating to {new_habitat}")
#         self.habitat = new_habitat
        
        
#     @classmethod
#     def find_species(cls, find_species):
#         return [bird for bird in cls.all_birds if bird.species == find_species]
#         # new_list = []
#         # for bird in cls.all_birds:
#         #     if bird.species == find_species:
#         #         new_list.append(bird)
#         # return new_list

# Crow = Bird(size="small", species="crow", color="black", habitat="urban", name="Scarecrow")

# print(id(Crow))
# print(type(Crow))
# Crow.migrate("rural")
# print(Crow.habitat)
# print(Crow)
# print(Crow.get_color)
