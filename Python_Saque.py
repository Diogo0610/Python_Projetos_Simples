valor = int(input("Digite o valor a ser sacado: R$"))

def saque(valor):
    valorTotal = valor
    ced_duzentos = valor//200
    valor -= ced_duzentos * 200
    ced_cem = valor//100
    valor -= ced_cem * 100
    ced_cinquenta = valor//50
    valor -= ced_cinquenta * 50
    ced_vinte = valor//20
    valor -= ced_vinte * 20
    ced_dez = valor//10
    valor -= ced_dez * 10
    ced_cinco = valor//5
    valor -= ced_cinco * 5
    ced_dois = valor//2
    valor -= ced_dois * 2
    
    print('Notas R$200,00 = ',ced_duzentos )
    print('Notas R$100,00 = ',ced_cem)
    print('Notas R$ 50,00 = ',ced_cinquenta)
    print('Notas R$ 20,00 = ',ced_vinte)
    print('Notas R$ 10,00 = ',ced_dez)
    print('Notas R$  5,00 = ',ced_cinco)
    print('Notas R$  2,00 = ',ced_dois)
    if valor!= 0:
        print(f"Não foi possível sacar R${valor},00 de R${valorTotal},00")
   
saque(valor)
