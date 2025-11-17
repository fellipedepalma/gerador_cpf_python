import random

ESTADOS = {
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

CPF_INVALIDOS = ["11111111111", "22222222222", "33333333333", "44444444444", "55555555555", "66666666666", "77777777777", "88888888888", "99999999999", "00000000000"]

def gerador_base_8_digitos(base):
    for _ in range(8):
        n = random.randint(0,9)
        base.append(n)
    return(base)


def separador():
    print("----------------------------------")


def mostrar_estados(uf):
    separador()
    print("ESCOLHA UM ESTADO DA LISTA ABAIXO: ")
    separador()
    
    for chave, valor in uf.items():
        print(f"{chave} -> {valor}")
    

def escolha_9_digito(base):
    mostrar_estados(ESTADOS)

    separador()
    print()
    escolha_uf = input(f"Digite o número referentea ao estado \n escolhido ou 'Q' para gerar aleatóriamente: ").strip().upper()
    print()
    separador()
    print()

    if escolha_uf == "Q":
        escolha_uf = random.randint(0,9)

    base.append(int(escolha_uf))    
    return base

def digito_verificador_1(base):
    soma1 = 0
    peso = 10

    for digito in base:
        soma1 += digito * peso
        peso -= peso

    resto1 = soma1 % 11

    if resto1 < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto1

    base.append(int(dv1))

    return base    



def digito_verificador_2(base):
    soma2 = 0
    peso  = 11

    for digito in base:
        soma2 += soma2 * peso
        peso -= peso

        resto2 = soma2 % 11

    if resto2 < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto2

    base.append(int(dv2))

    return base




#def digito_verificador_2(base):
#    soma2 = (base[0] * 11) + (base[1] * 10) + (base[2] * 9) + (base[3] * 8) + (base[4] * 7) + (base[5] * 6) + (base[6] * 5) + (base[7] * 4) + (base[8] * 3) + (base[9] * 2)
#    resto2 = soma2 % 11

#    if resto2 < 2:
#        dv2 = 0
#    else:
#        dv2 = 11 - resto2

#   base.append(int(dv2))
#    return base

def eh_invalido(base):
    cpf_puro = "".join(map(str,base))
    if cpf_puro in CPF_INVALIDOS:
        return True

def com_ou_sem_ponto(base):
    cpf_puro = "".join(map(str,base))
    origem_estado = ESTADOS[base[8]]
    escolha_pontuacao = input(f"VOCÊ QUER COM OU SEM PONTUAÇÃO, \nDIGITE 'S' PARA SIM OU 'N' PARA NÃO: ").strip().upper()
    print()
    
    if escolha_pontuacao == "S":
        bloco_1 = cpf_puro[0:3]
        bloco_2 = cpf_puro[3:6]
        bloco_3 = cpf_puro[6:9]
        bloco_4 = cpf_puro[9:11]

        cpf_formatado = f"{bloco_1}.{bloco_2}.{bloco_3}-{bloco_4}"

        separador()
        print()
        print(cpf_formatado)
        print(f"CPF pertence ao Estado(s) de {origem_estado}")
        print()

        separador()
    else:
        separador()
        print()
        print(cpf_puro)
        print(f"CPF pertence ao Estado(s) de {origem_estado}")
        print()
        separador()


def gerar_cpf():
    base_8 = []
    print()
    print("==================================")
    print(f"          GERADOR DE CPF         ")
    print("==================================")
    print()

    while True:
        gerador_base_8_digitos(base_8)
        escolha_9_digito(base_8)
        digito_verificador_1(base_8)
        digito_verificador_2(base_8)

        if not eh_invalido(base_8):
            break

    com_ou_sem_ponto(base_8)

gerar_cpf()