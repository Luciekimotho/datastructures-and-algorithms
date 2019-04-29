
message = 'The sky above the port was the color of television, tuned to a dead channel.'
key = 13
for symbol in message:
    #print(symbol.isalpha())
    encr_symbol = ''

    #encrypt the alphabets
    if symbol.isalpha():
        if symbol.isupper():
            encr_chr = ord(symbol) + key
            if encr_chr > ord('Z'):
                encr_chr -= 26
            elif encr_chr < ord('A'):
                encr_chr += 26
            encr_symbol = chr(encr_chr)
            print(encr_symbol)

        elif symbol.islower():
            encr_chr = ord(symbol) + key
            
            if encr_chr > ord('z'):
                encr_chr -= 26
            elif encr_chr < ord('a'):
                encr_chr += 26

            #print(encr_chr)
            encr_symbol = chr(encr_chr)
            print(encr_symbol)

    else:
        encr_symbol = symbol
        print(encr_symbol)

    #print(encr_symbol)



