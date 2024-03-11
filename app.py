
import os

todos_os_itens = []

def erro_tratamento():
    print('Erro')
    main()
   
def exibir():
    print("Escolha algumas das opções : ")
    print("1. Adicionar item : ")
    print("2. Listar  : ")
    print("3. Remover item : ")
    print("4. Sair : ")

def ecolha_uma_opcao():
    os.system('cls')

    exibir()
    opcao_escolhida = int(input("Digite uma opção :\n"))
   
    try:
        if opcao_escolhida == 1:
            adicionar_item()
            main()
       
        elif opcao_escolhida == 2:
             listar_item()
             main()
           
        elif opcao_escolhida == 3:
             print('Remover')
       
        elif opcao_escolhida == 4:
             print('Sair')
       
        else:
            erro_tratamento()
    except:
        print('Deu um erro : ')
     
     
def adicionar_item():
    os.system('cls')
    print("Adicionar um novo ITEM :")
    novo_item = input('Adicione o nome : \n')
    todos_os_itens.append(novo_item)
    input('Press enter para dar andamento!')
   
def listar_item():
    os.system('cls')
    for i in todos_os_itens:
        print(i)
    
    input('Press enter para dar andamento!')
   

def main():
    exibir()
    ecolha_uma_opcao()
 
if __name__ == '__main__':
    main()