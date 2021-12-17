def recebeDadosLivros():
    livros = {}
    key = 100
    while True:
        key += 1
        title = input().strip()
        if title == '': break
        isbn = input().strip()
        author = input().strip()
        price = float(input())
        livros[key] = (title, isbn, author, price)

    return livros


def main():
    biblioteca = recebeDadosLivros()

    for livro in biblioteca:
        print(f'Código: {livro}')
        print(f'Título: {biblioteca[livro][0]}')
        print(f'ISBN: {biblioteca[livro][1]}')
        print(f'Autor: {biblioteca[livro][2]}')
        print(f'Preço: {biblioteca[livro][3]:.2f}')


if __name__ == '__main__':
    main()
