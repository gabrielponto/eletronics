class Decimal(object):
    def __init__(self, decimal_number):
        self.value = decimal_number

    def convert_to_binary(self):
        return Binary(self.value)

class Binary(object):
    def __str__(self):
        return self.value

    def __init__(self, decimal_number):
        binary_number = bin(decimal_number)
        binary_number = binary_number.replace('0b', '')
        self.value = binary_number

    def last(self):
        return self.value[-1]

    def first(self):
        return self.value[0]

    def pos(self, pos):
        return self.value[pos]

    def equal_bits_length(self, other_number):
        max_length = self.len()
        if other_number.len() > max_length:
            self.value = self.value.zfill(other_number.len())

    def len(self):
        return len(self.value)

    def __int__(self):
        return int(self.value)

    def __getitem__(self, pos):
        return self.value[pos]
