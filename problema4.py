palabra = 'humanidad' 
letras = dict() 
contador = 0 

for letra in palabra: 
    if letra in letras: 
        if letras[letra] == 1: 
            contador += 1 
        letras[letra] += 1 
    else:
        letras[letra] = 1 #Si la letra no esta en el diccionario, la agrego
    
print(letras)