from database import db, Lista
import os

db.connect()
db.create_tables([Lista])

def create():
    os.system('cls')
    try:
        item_compra = input('Digite nome do item: ')
        Lista.create(item=item_compra)
    except:
        print('Houve um erro')

def read():
    os.system('cls')
    lista_itens = Lista.select()
    print('id | item')
    for itens in lista_itens:
        print(f'{itens.id}  | {itens.item}')

def update():
    try:
        id_item = int(input("digite o id: "))
        item = input('Digite o novo Valor: ')
        update_item = Lista.get(Lista.id == id_item)
        update_item.item = item
        update_item.save()
    except:
        print('Houve um erro')
    

def delete():
    os.system('cls')
    try:
        id_item = int(input("digite o id: "))
        delete_item = Lista.get(Lista.id == id_item)
        delete_item.delete_instance()
    except:
        print('Houve um erro')

while True:
    print('1) Adiconar')
    print('2) Ver itens')
    print('3) Atualizar item')
    print('4) Deletar item')
    print('5) Sair')
    opcao = int(input('>> '))
    while  opcao not in [1, 2, 3, 4, 5]:
        print('opção inválida...\n')
        opcao = int(input('>> '))

    match opcao:
        case 1:
            create()
        case 2:
            read()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            break