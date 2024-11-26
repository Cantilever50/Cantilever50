class Superhero:
    # Constructor to initialize the superhero with unique attributes
    def __init__(self, name, alias, power):
        self.name = name  # Real name of the superhero
        self.alias = alias  # Alias of the superhero (e.g., "Spiderman")
        self._power = power  # Superpower (encapsulation)

    # Getter for power (encapsulation)
    def get_power(self):
        return self._power

    # Method to display superhero information
    def display_info(self):
        return f"Superhero {self.alias} ({self.name}) has the power of {self._power}."

    # Method to perform an action (polymorphism example)
    def perform_action(self):
        print(f"{self.alias} is using {self.get_power()}!")


# Derived class: FlyingSuperhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, power, flying_speed):
        super().__init__(name, alias, power)  # Call the base class constructor
        self.flying_speed = flying_speed  # Additional attribute for flying speed

    # Overriding the perform_action method (polymorphism)
    def perform_action(self):
        print(f"{self.alias} takes to the sky, flying at {self.flying_speed} mph, while using {self.get_power()}!")

    # Method to display flying details
    def fly(self):
        print(f"{self.alias} is flying at {self.flying_speed} mph!")


# Example usage:

# Create a generic superhero (non-flying)
hero1 = Superhero("Clark Kent", "Superman", "Super Strength")
print(hero1.display_info())  # Show basic info
hero1.perform_action()  # Superman uses his power

# Create a flying superhero
hero2 = FlyingSuperhero("Peter Parker", "Spiderman", "Web-Slinging", 50)
print(hero2.display_info())  # Show basic info for Spiderman
hero2.perform_action()  # Polymorphism: Spiderman uses flying and web-slinging power
hero2.fly()  # Specific to FlyingSuperhero

