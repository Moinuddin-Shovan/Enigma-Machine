from Rotors import Rotor
from Reflectors import Reflector
from Plugboard import Plugboard


class Enigma:

    def __init__(self, chosenrotors, chosenreflector, chosenplugs):
        self.numcycles = 0
        self.rotors = []

        # Settings for the machine
        self.rotorsettings = [(chosenrotors[0], 0),
                              (chosenrotors[1], 0),
                              (chosenrotors[2], 0)]
        self.reflectorsetting = chosenreflector
        self.plugboardsetting = []

        # Create the plugboard
        self.plugboard = Plugboard(self.plugboardsetting, chosenplugs)

        # Create each of the rotors
        for i in range(len(self.rotorsettings)):
            self.rotors.append(Rotor(self.rotorsettings[i]))

        # Create reflector
        self.reflector = Reflector(self.reflectorsetting)

    def print_setup(self):
        # Prints initial setup information
        print("\nRotor sequence: (right to left)")
        for r in self.rotors:
            print(r.setting, "\t \t", r.sequence)
        print("\nReflector sequence:")
        print(self.reflector.setting, "\t", self.reflector.sequence, "\n")

        print("Plugboard settings:")
        print(self.plugboard.mapping, "\n")

    def reset(self):
        # Reset to initial state
        self.numcycles = 0
        for r in self.rotors:
            r.reset()

    def encode(self, c):
        # Run a cycle of the enigma with one character
        c = c.upper()

        if not c.isalpha():
            return c

        self.rotors[0].rotate()

        # Double step
        if self.rotors[1].base[0] in self.rotors[1].notch:
            self.rotors[1].rotate()

        # Normal stepping
        for i in range(len(self.rotors) - 1):
            if self.rotors[i].turnover:
                self.rotors[i].turnover = False
                self.rotors[i + 1].rotate()

        # Pass through the plugboard forward
        index = self.plugboard.forward(c)

        # Move through the rotors forward
        for r in self.rotors:
            index = r.forward(index)

        # Pass through the reflector
        index = self.reflector.forward(index)

        # Move back through rotors in reverse
        for r in reversed(self.rotors):
            index = r.reverse(index)

        # Pass through the plugboard reverse
        c = self.plugboard.reverse(index)

        return c
