
from plant import Plant
from invisibility_super_power import InvisibilitySuperPower 

class SuperPlant(Plant, InvisibilitySuperPower): 

    def __init__(self, name, visibility=True):
        super().__init__(name)
        self.__visibility = visibility


    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return super().__str__()
    
    def invisible(self): 
        if self.__visibility == True:
            self.__visibility = False
        return self.__visibility


    def visible(self): 
        if self.__visibility == False:
            self.__visibility = True
        return self.__visibility
        
        

    

    
