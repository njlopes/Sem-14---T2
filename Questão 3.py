def removeMEnor18(dicionario):
    menores = {}
    cont = 0
    for pessoa in range(20):
        if dicionario[pessoa][1] < 18:
            menores[cont] = dicionario[pessoa]
            cont += 1
            del dicionario[pessoa]
    return dicionario, menores


def dicionarioComDados20Pessoais():
    dados_pessoais = {}
    for pessoa in range(20):
        nome = input().strip()
        idade = int(input())
        cpf = input().strip()
        dados_pessoais[pessoa] = (nome, idade, cpf)
    return dados_pessoais


def main():
    cadastro = dicionarioComDados20Pessoais()
    cadastro_mais18, cadastro_menores = removeMEnor18(cadastro)

    print('========== MAIORES DE 18 ANOS ==========')
    for pessoa in cadastro_mais18:
        print(cadastro_mais18[pessoa][0], cadastro_mais18[pessoa][1], cadastro_mais18[pessoa][2], sep=';')

    print('========== MENORES DE 18 ANOS ==========')
    for menores in cadastro_menores:
        print(cadastro_menores[menores][0], cadastro_menores[menores][1], cadastro_menores[menores][2], sep=';')


if __name__ == '__main__':
    main()
