import os
import disciplina

ESPACAMENTO = 130

def menu():
    print("\n-- Gerenciar Disciplinas --")
    print("1. Cadastrar novas disciplinas")
    print("2  Listar situacao do aluno nas disciplinas cadastradas")
    print("3. Atualizar disciplina")
    print("4. Remover dados de uma disciplina especifica")
    print("5. Remover todos os dados armazenados")
    print("0. Sair")
    return input("Escolha uma opção: ")

def cadastrarDisciplina():
    print("\n-- Cadastro de Nova Disciplina --")
    
    disciplinaId = int(input("Digite o ID: "))
    nome = input("Digite o nome: ")
    nota1 = float(input("Digite a nota da 1ª unidade: "))
    nota2 = float(input("Digite a nota da 2ª unidade: "))
    disciplina.addDisciplina(disciplinaId, nome, nota1, nota2)
    
    print("\n Disciplina cadastrada com sucesso!")    
    input("\nPressione Enter para continuar...")

def listarSituacao():    
    print("\n-- Situação do Aluno --")
    print("-" * ESPACAMENTO)
    print(f"{'ID':<5} | {'Nome da Disciplina':<30} | {'Nota 1':<8} | {'Nota 2':<8} | {'Média':<7} | {'Status'}")
    print("-" * ESPACAMENTO)

    disciplinas = disciplina.selectDisciplina() 
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
        return False 
    for dis in disciplinas:
        disId, nome, nota1, nota2 = dis
        media = (nota1 + nota2) / 2
        status = ""
        if media >= 7.0:
            status = "Aprovado"
        elif media < 4.0:
            status = "Reprovado"
        else:
            nota_final_necessaria = (50 - (media * 6)) / 4
            status = f"Precisa tirar {nota_final_necessaria:.2f} na prova final"
        print(f"{disId:<5} | {nome:<30} | {nota1:<8.2f} | {nota2:<8.2f} | {media:<7.2f} | {status}")

    print("-" * ESPACAMENTO)

    input("\nPressione Enter para continuar...")


def atualizarDisciplina():
    print("\n-- Atualizar Disciplina --")

    disId = int(input("\nDigite o ID da disciplina que deseja atualizar: "))
    print("\nDigite os dados para atualizar a disciplina:")
    nome = input("Novo nome da disciplina: ")
    nota1 = float(input("Nova nota da 1ª unidade: "))
    nota2 = float(input("Nova nota da 2ª unidade: "))

    disciplina.updateDisciplina(nome, nota1, nota2, disId)
   
    print("\n Disciplina atualizada com sucesso!")
    input("\nPressione Enter para continuar...")


def removerDisciplina():
    print("\n-- Remover Disciplina --") 
    
    disId = int(input("\nDigite o ID da disciplina que deseja remover: "))
    confirmacao = input(f"Tem certeza que deseja remover a disciplina com ID {disId}? (s/n): ").lower()
    if confirmacao == 's':
        disciplina.deleteDisciplina(disId)
        print("\n Disciplina removida com sucesso!")
    else:
        print("\nOperação cancelada.")

    input("\nPressione Enter para continuar...")


def removerTodasDisciplinas():
    print("\n-- Remover todas as Disciplinas --")
    
    confirmacao = input("Tem certeza que deseja remover todas as disciplinas? (s/n)").lower()
    if confirmacao == 's':
        disciplina.clearDisciplina()
        print("\n Todos os dados foram removidos com sucesso.")
    else:
        print("\nOperação cancelada.")

    input("\nPressione Enter para continuar...")

while True:
    os.system('cls')
    
    escolha = menu()
    if escolha == '1':
        cadastrarDisciplina()
    elif escolha == '2':
        listarSituacao()
    elif escolha == '3':
        atualizarDisciplina()
    elif escolha == '4':
        removerDisciplina()
    elif escolha == '5':
        removerTodasDisciplinas()
    elif escolha == '0':
        disciplina.conn.close()
        print("Saindo...")
        break
    else:
        print("\n Opção invalida.")