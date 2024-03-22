class Person:
  """
  A class representing a person with attributes name, age, and gender.
  """

  def __init__(self, name, age, gender):
    """
    Initializes the Person object with name, age, and gender.

    Args:
      name: The person's name (string).
      age: The person's age (integer).
      gender: The person's gender (string).
    """
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """
    Prints a message introducing the person with their name, age, and gender.
    """
    print(f"Hello! My name is {self.name}. I am {self.age} years old and a {self.gender}.")

# Create an instance of the Person class
person1 = Person("Antony", 22, "Male")

# Call the introduce method to display person1's information
person1.introduce()
