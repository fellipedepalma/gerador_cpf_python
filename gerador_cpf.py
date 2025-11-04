import random

estados = {
    0: 'RS', 
    1: 'DF, GO, MT, MS e TO',
    2: 'PA, AM, AC, AP, RO e RR',
    3: 'CE, MA e PI',
    4: 'PE, RN, PB e AL',
    5: 'BA e SE',
    6: 'MG',
    7: 'RJ e ES',
    8: 'SP',
    9: 'PR e SC',
    "Q": 'Qualquer'
}

base_8 = []

def gerador_base_8_digitos(base):
    for _ in range(8):
        n = random.randint(0,9)
        base.append(n)
    print(base)

def mostrar_estados(uf):
    for chave, valor in uf.items():
        print(f"{chave} -> {valor}")

#def validar_entrada_nono_digito(nono_digito):
#    if not nono_digito.isInteger() or "Q":
#
#    if nono_digito < 0 or nono_digito > 9:
#        print("Escolha um estado valido: ")

def escolha_9_digito():
    print("===========================")
    print("Escolha um Estado abaixo: ")
    print("===========================")
    mostrar_estados(estados)
    print("===========================")
    
    escolha_uf = int(input(f"Digito o número referente ao estado escolhido ou Q para gerar aleatoriamente:"))
    
    if escolha_uf == "Q":
        escolha_uf = random.randint(0,9)
    



gerador_base_8_digitos(base_8)
escolha_9_digito()