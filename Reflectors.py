class Reflector:

    def __init__(self, setting):
        self.setting = setting
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # below are the wiring types
        self.settings = {"A": "EJMZALYXVBWFCRQUONTSPIKHGD",
                         "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                         "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}

        self.sequence = self.sequence_settings()

    def sequence_settings(self):
        # Set the initial sequence
        return self.settings[self.setting]

    def forward(self, index):
        # Passing through the reflector
        return self.sequence.index(self.base[index])
