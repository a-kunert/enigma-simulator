class Letters:

    offset = 96

    @staticmethod
    def char(code):
        if type(code) is str:
            return code
        return chr(code + Letters.offset).upper()

    @staticmethod
    def code(char):
        if type(char) is int:
            return char
        return ord(char.lower()) - Letters.offset
