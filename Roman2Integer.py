class Roman2Integer():

    def __init__(self, r):
        self.r = r

    def roman_to_integer(self):
        letter_value = {"I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000}

        number_value = 0
        invalid_combinations = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM']
        for combination in invalid_combinations:
            if combination in self.r:
                return f"Enter valid roman numeral!"
        try:
            for i in range(len(self.r)):
                if i > 0 and letter_value[self.r[-i]] > letter_value[self.r[-i - 1]]:
                    number_value -= letter_value[self.r[-i - 1]]
                else:
                    number_value += letter_value[self.r[-i - 1]]
            return f"{self.r} = {number_value}"
        except KeyError:
            undefined_letters = list()
            for item in self.r:
                if item not in letter_value.keys():
                    undefined_letters.append(item)
            return f"Undefined Input: {undefined_letters}"




