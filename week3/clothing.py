from clothing_size import ClothingSize

class Clothing():

    def __init__(self, colour, material):
        self.__colour = colour
        self.__material = material
        self.__size = ClothingSize() 

    def __repr__(self):
        return f'Clothing(colour={self.__colour} , material={self.__material} , size={self.__size})'
    
    def __str__(self):
        return f'Clothing colour: {self.__colour} , clothing material: {self.__material} , clothing size: {self.__size}'
    