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
    "Q": 'QUALQUER'
}

base_8 = []

def gerador_base_8_digitos(base):
    for _ in range(8):
        n = random.randint(0,9)
        base.append(n)
    print(base)

def separador():
    print("===========================")

def mostrar_estados(uf):
    separador()
    print("Escolha um Estado abaixo: ")
    separador()
    
    for chave, valor in uf.items():
        print(f"{chave} -> {valor}")
    
    separador()


def escolha_9_digito(base):
    mostrar_estados(estados)

    separador()
    escolha_uf = input(f"Digito o número referente ao estado escolhido ou Q para gerar aleatoriamente:").strip().upper()
    separador()
    
    if escolha_uf == "Q":
        escolha_uf = random.randint(0,9)

    base.append(int(escolha_uf))    
    #print(base)
    return base

def digito_verificador_1(base):
    soma1 = (base[0] * 10) + (base[1] * 9) + (base[2] * 8) + (base[3] * 7) + (base[4] * 6) + (base[5] * 5) + (base[6] * 4) + (base[7] * 3) + (base[8] * 2)
    resto1 = soma1 % 11

    if resto1 < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto1
    
    base.append(int(dv1))
    #print(base)

    return base

def digito_verificador_2(base):
    soma2 = (base[0] * 11) + (base[1] * 10) + (base[2] * 9) + (base[3] * 8) + (base[4] * 7) + (base[5] * 6) + (base[6] * 5) + (base[7] * 4) + (base[8] * 3) + (base[9] * 2)
    resto2 = soma2 % 11

    if resto2 < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto2

    base.append(int(dv2))
    # print(base)
    return base

def com_ou_sem_ponto(base):

    cpf_puro = "".join(map(str,base))
    
    escolha_pontuacao = input(f"Você quer com ou sem pontuação, Digite S para sim e N para Não:").strip().upper()
    
    if escolha_pontuacao == "S":
        bloco_1 = cpf_puro[0:3]
        bloco_2 = cpf_puro[3:6]
        bloco_3 = cpf_puro[6:9]
        bloco_4 = cpf_puro[9:11]

        cpf_formatado = f"{bloco_1}.{bloco_2}.{bloco_3}-{bloco_4}"
        print(cpf_formatado)
    else:
        print(cpf_puro)

gerador_base_8_digitos(base_8)
escolha_9_digito(base_8)
digito_verificador_1(base_8)
digito_verificador_2(base_8)
com_ou_sem_ponto(base_8)
