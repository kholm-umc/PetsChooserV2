"""
Author: Ken Holm
Purpose: Pet class
   Five properties with getter and setter methods
   * Animal ID
   * Animal Type
   * Owner Name
   * Pet's Age
   * Pet's Name
"""


class Pet:
    """
    Private properties
    """
    __petId = 1
    __animalType = "dog"
    __owner = "John Doe"
    __petAge = 0
    __petName = "Spot"

    """
    Class instantiator
    """

    def __init__(self,
                 petId=1,
                 animalType="dog",
                 owner="John Doe",
                 petAge=0,
                 petName="Spot"):
        self.setPetId(petId)
        self.setAnimalType(animalType)
        self.setOwnerName(owner)
        self.setPetAge(petAge)
        self.setPetName(petName)

    """
    Getter for the __animalType property
    """

    def getAnimalType(self):
        return self.__animalType

    """
    Setter for the __animalType property
    """

    def setAnimalType(self, animalType):
        try:
            # Is the argument not empty?
            if animalType:
                self.__animalType = animalType

        except Exception as e:
            raise TypeError(f"AnimalType seems to be empty!")

    """
    Getter for the __owner property
    """

    def getOwnerName(self):
        return self.__owner

    """
    Setter for the __owner property
    """

    def setOwnerName(self, owner):
        try:
            # Is the argument not empty?
            if owner:
                self.__owner = owner

        except Exception as e:
            raise TypeError(f"Owner seems to be empty!")

    """
    Getter for the __petAge property
    """

    def getPetAge(self):
        return self.__petAge

    """
    Setter for the __petAge property
    """

    def setPetAge(self, petAge):
        try:
            # Is the argument not empty?
            if int(petAge):
                self.__petAge = petAge

        except Exception as e:
            raise TypeError(f"{petAge} does not look like an integer!")

    """
    Getter for the __petId property
    """

    def getPetId(self):
        return self.__petId

    """
    Setter for the __petId property
    """

    def setPetId(self, petId):
        try:
            # Is the argument not empty?
            if int(petId):
                self.__petId = petId

        except Exception as e:
            raise TypeError(f"{petId} does not look like an integer!")

    """
    Getter for the __petName property
    """

    def getPetName(self):
        return self.__petName

    """
    Setter for the __petName property
    """

    def setPetName(self, petName):
        try:
            # Is the argument not empty?
            if petName:
                self.__petName = petName

        except Exception as e:
            raise TypeError(f"PetName seems to be empty!")
