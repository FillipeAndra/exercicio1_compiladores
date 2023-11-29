def gramatica(string_input):
    cadeia = []
    k = 0
    while k < len(string_input):
        letra = string_input[k]
        def S(string_input1):
            if string_input1 == '0':
                cadeia.append(string_input1)
            elif string_input1 == 'a' and k > 0:
                A(string_input1)
            elif string_input1 == 'b':
                B(string_input1)
            else:
                raise ValueError("pela regra da gramática o first tem que ser 0 e você digitou: " + string_input1)
        
        def A (string_input2):
            if string_input2 == 'a':
                cadeia.append(string_input2)
            else:
                S(string_input2)    
             
            
        def B(string_input3):
            if string_input3 == 'b':
                cadeia.append(string_input3)
            else:
                raise ValueError("Simbolo invalido" + string_input3)
            
        S(letra)
        k +=1
    
    return cadeia




teste = gramatica('0aa')
print(teste)