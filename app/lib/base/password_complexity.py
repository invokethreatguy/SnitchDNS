import string


class PasswordComplexityManager:
    def __init__(self, min_length, min_lower, min_upper, min_digits, min_special):
        self.min_length = int(min_length)
        self.min_lower = int(min_lower)
        self.min_upper = int(min_upper)
        self.min_digits = int(min_digits)
        self.min_special = int(min_special)

        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation

    def meets_requirements(self, password):
        if len(password) < self.min_length:
            return False

        lower = upper = digits = special = 0
        for c in password:
            if c in self.lower:
                lower += 1
            elif c in self.upper:
                upper += 1
            elif c in self.digits:
                digits += 1
            elif c in self.special:
                special += 1

        if lower < self.min_lower:
            return False
        elif upper < self.min_upper:
            return False
        elif digits < self.min_digits:
            return False
        elif special < self.min_special:
            return False

        return True

    def get_requirement_description(self):
        desc = [
            "Minimum Length: " + str(self.min_length),
            "Minimum Lowercase: " + str(self.min_lower),
            "Minimum Uppercase: " + str(self.min_upper),
            "Minimum Digits: " + str(self.min_digits),
            "Minimum Special: " + str(self.min_special)
        ]

        return ", ".join(desc)
