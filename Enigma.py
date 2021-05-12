from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor
from RotorTypes import RotorTypes


class Enigma:

    def __init__(self, reflector="UKW-B", rotors=["III", "II", "I"], rings=[1, 1, 1], plugboard=""):
        self.plugboard = Plugboard(plugboard)
        self.rotors = Reflector(**RotorTypes.get(reflector))

        for index, rotor_type in enumerate(rotors):
            rotor = Rotor(**RotorTypes.get(rotor_type))
            rotor.set_ring_position(rings[index])
            self.rotors = self.rotors.assemble(rotor)
        # Add the Entry-Rotor
        self.rotors = self.rotors.assemble(Rotor())

    def set_position(self, position):
        pass

    def encrypt(self, letter):
        letter = self.plugboard.apply(letter)
        letter = self.rotors.rotate().encrypt(letter)
        letter = self.plugboard.apply(letter)
        return letter
