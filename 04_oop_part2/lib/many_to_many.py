class Cocktails:
    all_bars = []
    def __init__(self, spirit, oz, name):
        self.spirit = spirit
        self.oz = oz
        self.name = name
        self.bars = []

    def __str__(self):
        return f"Cocktail: {self.spirit}, Oz: {self.oz}"

    # in order to present both the cocktail object as well as the string representation of the cocktail object
    # we need to define a __repr__ method
    def __repr__(self):
        # to return the string representation of the Cocktails object in addition to the object itself, we can use the f-string
        for bar in self.bars:
            return f"Cocktail: {self.name}, Spirit: {self.spirit}, Oz: {self.oz}, Bar: {bar.name}"

    
    
        
        
    
        
class Bar:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cocktails = []
        Cocktails.all_bars.append(self)
    
    def build_menu(self, menu_arr):
        for item in menu_arr:
            if type(item) is Cocktails:
                self.cocktails.append(item)
                item.bars.append(self)
                
if __name__ == "__main__":
    margarita = Cocktails('tequila', 2, 'margarita')
    mojito = Cocktails('rum', 2, 'mojito')
    manhattan = Cocktails('whiskey', 3, 'manhattan')
    old_fashioned = Cocktails('whiskey', 3, 'old fashioned')
    cosmopolitan = Cocktails('vodka', 2, 'cosmopolitan')
    martini = Cocktails('vodka', 2, 'martini')
    
    bar1 = Bar('The Alamo', 'Denver')
    bar2 = Bar('The Cruise Room', 'Denver')
    
    bar1.build_menu([margarita, mojito, manhattan, old_fashioned])
    bar2.build_menu([cosmopolitan, martini])
    
    print(bar1.cocktails)
    print(bar2.cocktails)