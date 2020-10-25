import sys
from Enigma import Enigma


def main():

    chosen_rotors = []
    print("Choose rotors. Type I / II/ III/ IV/ V/ VI/ VII/ VIII")
    for i in range(3):
        inp = str(input('Write your choice in ROMAN form for no. {}: '.format(i + 1)))
        chosen_rotors.append(inp)

    chosenreflector = str(input('Choose a reflector. Type A/B/C: '))
    chosenplugs = int(input('Choose a plugboard. Type 1/2/3/4/5: ')) - 1

    machine = Enigma(chosen_rotors, chosenreflector, chosenplugs)
    machine.print_setup()
    try:
        print('1. Check the setup\n2. Test for an input\n3. Copy the output\n4. Rerun with the same setup\n')
        for i in range(5):
            plaintext = input('Write to test Enigma Machine: \n')
            if plaintext == '':
                sys.exit()

            ciphertext = ""
            print("Plaintext", "\t", plaintext)
            for character in plaintext:
                ciphertext += machine.encode(character)

            print("Ciphertext", "\t", ciphertext)

            # Reset and Decode same message
            machine.reset()
            plaintext = ""
            for character in ciphertext:
                plaintext += machine.encode(character)
            print("Cipher text to Plain text", "\t", plaintext)
            print('\nPress Enter twice to quit')
    except IndexError:
        for plaintext in sys.stdin:
            for character in plaintext:
                sys.stdout.write(machine.encode(character))


if __name__ == '__main__':
    main()
