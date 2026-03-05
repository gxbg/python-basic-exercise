import os

ARQUIVO = "tarefas.txt"

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f.readlines()]

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for t in tarefas:
            f.write(t + "\n")

def mostrar_menu():
    print("\n=== TO-DO LIST ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha: ")

        if opcao == "1":
            tarefa = input("Nova tarefa: ")
            tarefas.append(tarefa)
            salvar_tarefas(tarefas)
            print("Tarefa adicionada!")

        elif opcao == "2":
            if not tarefas:
                print("Nenhuma tarefa.")
            else:
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t}")

        elif opcao == "3":
            num = int(input("Número da tarefa: "))
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                salvar_tarefas(tarefas)
                print(f"Removida: {removida}")
            else:
                print("Número inválido.")

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
