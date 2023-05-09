letra=input("Digite uma letra: \n")#pede para usuario digitar uma letra, e armazena na variavel letra
vogais=["a","e","i","o","u"] #delcara as vogais
if letra in vogais:#use letra for um dos itens do vogal
    print ("A letra ", letra, "é uma vogal")
else:
    print("A letra", letra, "é uma consoante")