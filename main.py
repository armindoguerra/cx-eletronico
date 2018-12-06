# coding: utf-8

# Função que verifica a possibilidade de saque com as cédulas disponíveis. Essa função dentro de uma classe

def withdrawal_verify(value,bills):
    
    bills.reverse() # Invertendo a ordem da lista de cédulas

    numBills = []
    for i in bills:
        
        # Dividindo cada cádula disponível pelo valor que se quer sacar e populando a lista 'numBills'        
        numBills.append(value/i) 
        value %= i

    
    numTotalBills = 0
    for i in range(len(bills)):
        a,b = divmod(numBills[i],1)
        numTotalBills += a
        print("Notas de R$ %d: %d" % (bills[i], numBills[i]))

    # Verificando a possibilidade do saque para retornar o resultado final
    if value != 0:
        result = -1
        print(result)
    else:
        result = int(numTotalBills)
        print(result)
    
    return result

# Invocando a fução withdrawal_verify(value,bills)

value = 93
billsList = [1,2,20,50,100]
withdrawal_verify(value, billsList)

