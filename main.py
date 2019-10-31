"""
Author: Ken Holm
Purpose: List all the pets and allow the customer to
          see information about a chosen pet
"""

import pymysql.cursors
from creds import *
from petsClass import *

"""
 Some initial variables
"""
listOfPets = []

"""
 Give our user a list of pets from which to choose
"""


def listChoices():
    counter = 1

    # Clear the screen and put up the header
    print("*".center(30, "*"))
    print(" Pet Chooser ".center(30, "*"))
    print("*".center(30, "*"))

    for aPet in listOfPets:
        if counter < 10:
            print(f"[{counter}]  {aPet.getPetName()}")
        else:
            print(f"[{counter}] {aPet.getPetName()}")
        counter += 1

    # And the option to quit
    print("[Q] Quit")


"""
 Edit the pet's name and age
  Update the data in the database
"""


def editPet(aPet):
    print(f"You have chosen to edit {aPet.getPetName()}")

    newName = input("New name: [ENTER == no change] ")
    try:
        if newName:
            aPet.setPetName(newName)
            print(f"The pet's name is now {aPet.getPetName()}")
        else:
            print("No change")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")
        print()

    newAge = input("New age: [ENTER == no change] ")
    try:
        if newAge:
            if int(newAge):
                aPet.setPetAge(newAge)
                print(f"The pet's Age is now {aPet.getPetAge()}")
        else:
            print("No change")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")
        print()

    # Now we have to update the table
    try:
        dbConnection = pymysql.connect(host=host,
                                       user=username,
                                       password=password,
                                       db=database,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)

    except Exception as e:
        print("An error has occurred.  Exiting.")
        print(e)
        print()
        exit()

    # Now, let's try to update the database
    try:
        with dbConnection.cursor() as dbCursor:
            # Our sql statement, easy to read
            sql = """
                                        update
                                                pets
                                        set
                                                name = %s
                                                , age = %s
                                        where
                                                id = %s
                                """

            # Execute and commit query
            dbCursor.execute(sql, (aPet.getPetName(), aPet.getPetAge(), aPet.getPetId()))
            dbConnection.commit()
            print(f"The database has been updated")

    except Exception as e:
        print("An error has occurred.  Exiting.")
        print(e)
        print()

    # Close connection
    finally:
        dbConnection.close()

    input("Continue")


"""
 Connect to the database
"""
try:
    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 db=database,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print("An error has occurred.  Exiting.")
    print(e)
    print()
    exit()

"""
 Now that we are connected, execute a query
  and do something with the result set.
"""
try:
    with connection.cursor() as cursor:
        # Our sql statement, easy to read
        sql = """
                                select
                                        pets.name as pet
                                        , pets.age
                                        , owners.name as owner
                                        , types.animal_type as animal
                                        , pets.id as id
                                from
                                        pets
                                join
                                        owners
                                on pets.owner_id = owners.id
                                join
                                        types
                                on pets.animal_type_id = types.id;
                                """

        # Execute query
        cursor.execute(sql)

        # Loop through all the results
        #  Append a new Pet object to our list of pets
        for row in cursor:
            tempPet = Pet(animalType=row['animal'],
                          owner=row['owner'],
                          petAge=row['age'],
                          petId=row['id'],
                          petName=row['pet'])
            listOfPets.append(tempPet)

except Exception as e:
    print("An error has occurred.  Exiting.")
    print(e)
    print()

finally:
    """
         Close connection
        """
    connection.close()

"""
 Now, we have a list of pets in listOfPets
  Print our list from which to choose,
  allow our user to choose
"""
while True:
    listChoices()
    choice = ""
    try:
        pet = input("Please choose from the list above: ")
        if pet == "Q" or pet == "q":
            print("Thank you.")
            break

        elif 0 < int(pet) <= len(listOfPets):
            tempPet = listOfPets[int(pet) - 1]
            print()
            print(f"You have chosen {tempPet.getPetName()}, the {tempPet.getAnimalType()}.  {tempPet.getPetName()} is {tempPet.getPetAge()} years old.  {tempPet.getPetName()}'s owner is {tempPet.getOwnerName()}.")
            print()
            choice = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet? ")

            # Does the user want to quit?
            if choice == "Q" or choice == "q":
                print("Thank you")
                break
            # Does the user want to edit a pet?
            elif choice == "E" or choice == "e":
                editPet(tempPet)

            # Let's assume the user must want to continue
            else:
                pass

        else:
            print(f"{pet} is an invalid choice.")
            input("Press [ENTER] to continue.")

    except Exception as e:
        print(f"{pet} is an invalid choice: {e}")
        input("Press [ENTER] to continue.")
