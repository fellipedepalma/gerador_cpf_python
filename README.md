# 🐍 Gerador de CPF em Python Puro

Este é um projeto de estudo focado em praticar lógica de programação e algoritmos em Python puro.

O objetivo é criar um script capaz de gerar números de CPF válidos, incluindo o cálculo correto dos dígitos verificadores (DV), a formatação e a identificação do estado de origem.

---

## ✨ Funcionalidades

* **Geração Aleatória:** Cria os 9 primeiros dígitos de forma aleatória.
* **Cálculo dos Dígitos Verificadores:** Implementa o algoritmo "Módulo 11" para calcular o primeiro e o segundo dígito verificador.
* **Verificação de Invalidez:** Garante que CPFs com todos os números repetidos (ex: `111.111.111-11`) não sejam gerados.
* **Formatação:** Apresenta o CPF gerado em dois formatos:
    * Com pontuação (Ex: `XXX.XXX.XXX-XX`)
    * Apenas números (Ex: `XXXXXXXXXXX`)
* **Estado de Origem:** Exibe a Região Fiscal (Estado) correspondente ao 9º dígito do CPF.

---

## 🚀 Como Usar

Este projeto é um script simples. Para executá-lo, você precisa ter o Python 3 instalado.

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/fellipedepalma/gerador-cpf-python.git](https://github.com/fellipedepalma/gerador-cpf-python.git)
    ```

2.  Navegue até a pasta do projeto:
    ```bash
    cd gerador-cpf-python
    ```

3.  Execute o script principal:
    ```bash
    python gerador_cpf.py
    ```

---

## 🧠 O Algoritmo Implementado

A geração do CPF segue rigorosamente as regras definidas pela Receita Federal, baseadas no cálculo do "Módulo 11".

1.  **Geração da Base:** São gerados 9 dígitos aleatórios. O 9º dígito determina o estado de origem.
2.  **Cálculo do 1º DV (Dígito Verificador):**
    * Os 9 dígitos da base são multiplicados por pesos decrescentes (10 a 2).
    * A soma desses valores é dividida por 11.
    * O `Resto` da divisão define o dígito:
        * Se `Resto < 2`, o DV1 é `0`.
        * Senão, o DV1 é `11 - Resto`.
3.  **Cálculo do 2º DV:**
    * O processo é repetido, mas agora incluindo o DV1.
    * Os 9 dígitos da base + o DV1 são multiplicados por pesos decrescentes (11 a 2).
    * O mesmo cálculo do `Resto` é aplicado para encontrar o DV2.
4.  **Verificação Final:** O script verifica se o CPF gerado é uma sequência de números repetidos (como `000...` ou `111...`). Se for, o processo é reiniciado para garantir um CPF válido.

### 🗺️ Tabela de Estados de Origem (9º Dígito)

| 9º Dígito | Região Fiscal |
| :---: | :--- |
| **0** | RS |
| **1** | DF, GO, MT, MS, TO |
| **2** | PA, AM, AC, AP, RO, RR |
| **3** | CE, MA e PI |
| **4** | PE, RN, PB, AL |
| **5** | BA e SE |
| **6** | MG |
| **7** | RJ e ES |
| **8** | SP |
| **9** | PR e SC |

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.