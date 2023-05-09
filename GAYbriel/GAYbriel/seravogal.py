#Faça um programa que peça para o usuario digitar uma letra 
#e verifique se a letra é vogal ou consoante

letrinha=input("Digite uma letra:\n")
print("voce digitou", letrinha)
if letrinha=="a":
    print("voce digitou uma vogal a")
elif letrinha=="e":
    print("voce digitou uma vogal e")
elif letrinha=="i":
    print("voce digitou uma vogal i")
elif letrinha=="o":
    print("voce digitou uma vogal o")
elif letrinha=="u":
    print ("voce digitou uma vogal")
elif letrinha=="aeiou":
    print("voce digitou uma vogal")
else:
    print("Voce digitou uma cosoante")
