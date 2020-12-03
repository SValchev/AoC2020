import re
from pathlib import Path

class RegexPattern:
    class GroupNames:
        FIRST_DIIGIT = 'first_digit'
        SECOND_DIIGIT = 'second_digit'
        VALIDATION_LETTER = 'letter'
        PASSWORD = 'password'
    
    AS_STRING = rf'(?P<{GroupNames.FIRST_DIIGIT}>\d+)-(?P<{GroupNames.SECOND_DIIGIT}>\d+)\s(?P<{GroupNames.VALIDATION_LETTER}>\w):\s(?P<{GroupNames.PASSWORD}>\w+)'


class PasswordEntity:
    def __init__(self, password, first_digit, second_digit, letter):
        self.password = password
        self.first_digit = int(first_digit)
        self.second_digit = int(second_digit)
        self.letter = letter

    def is_valid(self):
        letters_count = self.password.count(self.letter)
        return self.first_digit <= letters_count <= self.second_digit

    def is_valid2(self):
        new_first_digit = self.first_digit - 1
        new_second_digit = self.second_digit - 1
        # XOR operation
        return self.validate_index(new_first_digit) ^ self.validate_index(new_second_digit)

    def validate_index(self, index):
        return self.char_in_scope(index) and self.is_letter(index)

    def char_in_scope(self, index):
        return 0 <= index < len(self.password)
    
    def is_letter(self, index):
        return self.password[index] == self.letter


if __name__ == "__main__":
    total_result = 0
    input_ = Path('input.txt').open().readlines()

    for line in input_:
        match = re.match(RegexPattern.AS_STRING, line)
        total_result += PasswordEntity(**match.groupdict()).is_valid2()
    print(total_result)

    
    