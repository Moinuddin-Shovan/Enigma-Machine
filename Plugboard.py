class Plugboard:
    def __init__(self, mapping, chosenplugs):
        self.plugs = [
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "QAZXCDSEWRFVBGTYHNMJKUIOLP",
            "ZMXNCBVGFHDJSKALQPWOEIRUTY",
            "MLPOKNJIUHBVGYTFCXDRESZAWQ",
            "QWERFVDSMKPOIJUHYGTCXZBNLA"
        ]
        self.base = self.plugs[chosenplugs]
        self.mapping = {}

        for m in self.base:
            self.mapping[m] = m

        for m in mapping:
            self.mapping[m[0]] = m[1]
            self.mapping[m[1]] = m[0]

    def forward(self, c):
        # Return index of the character
        return self.base.index(self.mapping[c])

    def reverse(self, index):
        # Return the character of the index
        return self.mapping[self.base[index]]
