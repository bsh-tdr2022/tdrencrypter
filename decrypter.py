def desencriptar(text):
    final = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    x = 0

    while x < 26:
        x +=1 #Va sumant 1 terme a x fins que x = 26
        shift = int (x)
        text = text.lower() #El programa té problemes per desencriptar majúscules, per tant, passa tot el text a minúscules abans
        frasedesencriptada = ""
    
        for character in text:
            posicio = alfabet.find (character) #Busca en quina posició es troba el caracter
            novap = posicio - shift
            if character in alfabet:
                frasedesencriptada += alfabet [novap] #Substitució de cada caracter encriptat pel desencriptat
            else:
                frasedesencriptada += character #Si no forma part de l'alfabet, afegeix el caracter sense encriptar.
        final += f'Clau: {shift}\n'
        final += f'Missatge: {frasedesencriptada}\n'

    return final

#Per proves de funcionament
if __name__ == "__main__":
    frase = input ("Escrigui el missatge encriptat: ")
    print(desencriptar(frase))
