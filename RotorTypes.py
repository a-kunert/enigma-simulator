class RotorTypes:
    rotors = [
        {
            "name": "I",
            "permutation": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "notches": "Q"
        },
        {
            "name": "II",
            "permutation": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "notches": "E"
        },
        {
            "name": "III",
            "permutation": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            "notches": "V"
        },
        {
            "name": "IV",
            "permutation": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            "notches": "J"
        },

        {
            "name": "V",
            "permutation": "VZBRGITYUPSDNHLXAWMJQOFECK",
            "notches": "Z"
        },

        {
            "name": "UKW-A",
            "permutation": "EJMZALYXVBWFCRQUONTSPIKHGD",
            "notches": ""
        },

        {
            "name": "UKW-B",
            "permutation": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "notches": ""
        },
        {
            "name": "UKW-C",
            "permutation": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
            "notches": ""
        }
    ]

    @staticmethod
    def get(name):
        result = next((rotor for rotor in RotorTypes.rotors if rotor["name"] == name), None)
        return {key: result[key] for key in result if key in ["permutation", "notches"]}
