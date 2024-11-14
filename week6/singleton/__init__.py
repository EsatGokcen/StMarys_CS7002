# Singleton 
# works by having a private constructor to prevent direct instantiation 
# of the object from outside the class. Only a singleton itslef can initiate an object.

# Example:
# class Singleton:
#   __instance = None

#   def __new__(cls):
#       if cls.__instance is None:
#           cls.__instance = super().__new__(cls)
#       return cls.__instance

