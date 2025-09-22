class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        return "Value is not a float"
    @classmethod
    def from_roman(cls, value):
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }

        int_value = 0

        roman_input = value.upper()

        for i in range(len(roman_input)):
            if roman_input[i] in roman_numerals:
                if i + 1 < len(roman_input) and roman_numerals[roman_input[i]] < roman_numerals[roman_input[i + 1]]:
                    int_value -= roman_numerals[roman_input[i]]
                else:
                    int_value += roman_numerals[roman_input[i]]
            else:
                return "Wrong Input"
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string("2"))