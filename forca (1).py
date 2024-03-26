def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "maça".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas2 = []
    
    for letra in (palavra_secreta):
        letras_acertadas2.append("_")
        
        
        enforcou = False
        acertou = False
        erros = 0
        
        print(letras_acertadas)
        
        while (not enforcou and not acertou):
            chute = input("Qual letra?")
            chute = chute.strip().upper()
            
            if (chute in palavra_secreta):
            
        
        
        
        print(letras_acertaas)
        
        while (not enforcou and not acertou):
            chute = input("Qual letra? ")
            chute = chute.strip().upper()

