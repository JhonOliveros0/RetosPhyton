def decimal_a_binario(num):

    binario = ""

    while num // 2 != 0 :
        binario = str(num%2) + binario
        num = num //2
    return str(num) + binario

valor_prueba = int(input())

valor_binario = decimal_a_binario(valor_prueba)

print(valor_binario)
