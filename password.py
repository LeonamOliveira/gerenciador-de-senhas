import sqlite3

MASTER_PASSWORD = "123456"

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')


def menu():
    print("********************************")
    print("* I: Inserir uma nova senha:   *")
    print("* L: Listas serviços salvos:   *")
    print("* R: Recuperar uma senha       *")
    print("* S: Sair                      *")
    print("********************************")


while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ['L', 'I', 'R', 'S', 'l', 'i', 'r', 's']:
        print("Opção inválida!")
        continue

    if op == 's' or op == 'S':
        break

conn.close()
