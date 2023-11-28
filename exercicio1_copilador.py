def gramatica(string_input):
    cadeia = []
    k = 0
    while k < len(string_input):
        letra = string_input[k]
        def S(string_input1):
            i = 0
            while i < len(string_input1):
                if string_input1 == '0':
                    cadeia.append(string_input1)
                A(string_input1)
                B(string_input1)
                i += 1

        def A (string_input2):
            j = 0
            while j < len(string_input2):
                if string_input2 == 'a':
                    cadeia.append(string_input2)
                S(string_input2)    
                A(string_input2)
                j+=1    
            
        def B(string_input3):
            l =0
            while l < len(string_input3):
                if string_input3 == 'b':
                    cadeia.append(string_input3)
                else:
                    raise ValueError("Simbolo invalido" + string_input3)
                l += 1
        S(letra)
        k +=1
    
    return cadeia




teste = gramatica('0aa')
print(teste)
    

    
