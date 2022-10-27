def encriptar(text, shift):
    result = ''
    
    for i in range(len(text)):
        #Escaneja cada caracter del text per separat
        char = text [i]
        
        #Encripta o no segons el caracter és o no un espai
        if char != " ":
            #Encripta les majúscules
            if (char.isupper()):
                result += chr((ord(char) + shift - 65) % 26 + 65)
             #Encripta les minúscules
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char #Si el caracter és un espai, el deixa tal com està
        
    return result

#Per proves de funcionament
if __name__ == "__main__":
    text = input("Escrigui el missatge: ")
    shift = int(input("Escrigui quants espais vols moure les lletres: "))

    print(encriptar(text, shift))
