# Pet Class
class Pet:
    # Constructor
    def __init__(self, name="", type="", age=0):
        self.__name = name
        self.__type = type
        self.__age = age

    # Mutator methods
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def setAge(self, age):
        self.__age = age

    # Accessor methods
    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getAge(self):
        return self.__age

# Main program
def main():
    # Create a Pet object
    animal = Pet()

    # Get values for the pet
    input_name = input("Enter a pet name: ")
    animal.setName(input_name)

    input_type = input("Enter a pet type (e.g., Dog, Cat, Bird): ")
    animal.setType(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.setAge(input_age)

    # Display the pet's information
    print("\nThe pet name is:", animal.getName())
    print("The pet type is:", animal.getType())
    print("The pet age is:", animal.getAge())

# Run the main function
if __name__ == "__main__":
    main()
