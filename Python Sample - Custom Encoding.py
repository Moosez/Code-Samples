class main:
    #The main class of the entire program.
    def menu():
        #Decision based on User Input
        if (EnDe == "Encode"):
            main.encode()
        elif (EnDe == "Decode"):
            main.decode()
        else:
            print("Thats not an option, friend.")
    def encode():
        #The function for encoding data
        value = input("Information to be encoded: ")
        intermediatedec = int(value) + 8192
        encoded = '{0:04x}'.format(int("0" + str('{0:b}'.format(intermediatedec))[0:7] + "0" + str('{0:b}'.format(intermediatedec))[7:14], base=2))
        print(encoded)
        return(encoded)
    def decode():
        #The function for decoding data
        hi = int(input("Hi Byte: "), base=16)
        lo = int(input("Lo Byte: "), base=16)
        decoded = int('{0:08b}'.format(hi)[1:8] + '{0:08b}'.format(lo)[1:8], base=2) - 8192
        print(decoded)
        return(decoded)
#User Input
EnDe = input("Encode or Decode: ")
#Running the menu function for decision making
while 1 == 1:
    main.menu()
