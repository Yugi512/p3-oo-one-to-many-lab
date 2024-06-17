class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        self.check_pet_type(self.pet_type)
        self.all.append(self)
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,owner):
        if not isinstance(owner,Owner):
            raise Exception("not owner")
        self._owner = owner
    
    def check_pet_type(self,type):
        if type not in self.PET_TYPES:
            raise Exception("Not in pet type")
        self.pet_type = type
    
    

class Owner:

    def __init__(self,name):
        self.name = name


    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
 
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise Exception("not pet")
        pet.owner = self
    
    
    def get_sorted_pets(self):
        sorts = sorted([pet for pet in Pet.all], key = lambda pet: pet.name)
        return sorts


