import csv

print("Olá, bem-vindo ao seu assistente virtual de plantação!")

total_insumos = [0, 0, 0, 0]  # [Nitrogênio, Fósforo, Potássio, Cálcio]
nomes_insumos = ['Nitrogênio', 'Fósforo', 'Potássio', 'Cálcio']

def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Escolher a cultura e calcular os insumos")
    print("2. Visualizar os cálculos")
    print("3. Alterar algum dado")
    print("4. Deletar dados")
    print("5. Criar CSV com os dados")
    print("6. Sair do programa")

def entrada_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['sim', 'não', 'nao']:
            return resposta == 'sim'
        else:
            print("Entrada inválida! Por favor, responda com 'sim' ou 'não'.")

def entrada_dados():
    global crops, tamanho, num_safras

    while True:
        try:
            crops = int(input("Digite 1 se você deseja plantar soja ou 2 se deseja plantar cana-de-açúcar: "))
            if crops == 1 or crops == 2:
                print(f"Você escolheu plantar {'soja' if crops == 1 else 'cana-de-açúcar'}.")
                break  
            else:
                print("Entrada inválida! Por favor, digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número (1 ou 2).")

    nitro = entrada_sim_nao("Você deseja fertilizar com nitrogênio? (sim/não): ")
    fosforo = entrada_sim_nao("Você deseja fertilizar com fósforo? (sim/não): ")
    pota = entrada_sim_nao("Você deseja fertilizar com potássio? (sim/não): ")
    cal = entrada_sim_nao("Você deseja fertilizar com cálcio? (sim/não): ")

    tamanho = int(input("Quantos metros quadrados você pretende plantar? "))

    if crops == 1:  # Soja
        num_safras = int(input("Quantas safras de soja você pretende cultivar? (1-2 por ano): "))
        tempo_safra = num_safras * 6  # Cada safra de soja é de aproximadamente 6 meses
    elif crops == 2:  # Cana-de-açúcar
        num_safras = int(input("Quantas safras de cana-de-açúcar você pretende cultivar? (1-2 por ano): "))
        tempo_safra = num_safras * 12  # Cada safra de cana é de aproximadamente 12 meses

    nitrosoja = 5  
    nitrocana = 10 
    fosforosoja = 10
    fosforocana = 10
    potasoja = 10
    potacana = 20
    calsoja = 3
    calcana = 6

    if crops == 1:  # Soja
        total_insumos[0] = (tamanho * num_safras * nitrosoja) / 1000 if nitro else 0  # Nitrogênio
        total_insumos[1] = (tamanho * num_safras * fosforosoja) / 1000 if fosforo else 0  # Fósforo
        total_insumos[2] = (tamanho * num_safras * potasoja) / 1000 if pota else 0  # Potássio
        total_insumos[3] = (tamanho * num_safras * calsoja) / 1000 if cal else 0  # Cálcio
    elif crops == 2:  # Cana-de-açúcar
        total_insumos[0] = (tamanho * num_safras * nitrocana) / 1000 if nitro else 0  # Nitrogênio
        total_insumos[1] = (tamanho * num_safras * fosforocana) / 1000 if fosforo else 0  # Fósforo
        total_insumos[2] = (tamanho * num_safras * potacana) / 1000 if pota else 0  # Potássio
        total_insumos[3] = (tamanho * num_safras * calcana) / 1000 if cal else 0  # Cálcio

    saida_dados()

def saida_dados():
    print(f"\nVocê terá {tamanho} metros quadrados de {'soja' if crops == 1 else 'cana-de-açúcar'} para {num_safras} safra(s),")
    print("Demandas de fertilizantes para o período escolhido:")
    for i in range(len(nomes_insumos)):
        print(f"- {nomes_insumos[i]}: {total_insumos[i]:.2f} kg")

def atualizar_dados():
    saida_dados()
    try:
        indice = int(input("Digite o número do fertilizante que deseja atualizar (1: Nitrogênio, 2: Fósforo, 3: Potássio, 4: Cálcio): ")) - 1
        if 0 <= indice < len(total_insumos):
            novo_tamanho = int(input("Digite a nova quantidade de metros quadrados que deseja plantar: "))
            novo_valor_calculado = 0

            if crops == 1:  # Soja
                if indice == 0:  # Nitrogênio
                    novo_valor_calculado = (novo_tamanho * num_safras * 5) / 1000
                elif indice == 1:  # Fósforo
                    novo_valor_calculado = (novo_tamanho * num_safras * 10) / 1000
                elif indice == 2:  # Potássio
                    novo_valor_calculado = (novo_tamanho * num_safras * 10) / 1000
                elif indice == 3:  # Cálcio
                    novo_valor_calculado = (novo_tamanho * num_safras * 3) / 1000
            elif crops == 2:  # Cana-de-açúcar
                if indice == 0:  # Nitrogênio
                    novo_valor_calculado = (novo_tamanho * num_safras * 10) / 1000
                elif indice == 1:  # Fósforo
                    novo_valor_calculado = (novo_tamanho * num_safras * 10) / 1000
                elif indice == 2:  # Potássio
                    novo_valor_calculado = (novo_tamanho * num_safras * 20) / 1000
                elif indice == 3:  # Cálcio
                    novo_valor_calculado = (novo_tamanho * num_safras * 6) / 1000

            total_insumos[indice] = novo_valor_calculado
            print(f"{nomes_insumos[indice]} atualizado para {novo_valor_calculado:.2f} kg.")
            saida_dados()  
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def deletar_dados():
    saida_dados()
    try:
        indice = int(input("Digite o número do fertilizante que deseja deletar (1: Nitrogênio, 2: Fósforo, 3: Potássio, 4: Cálcio): ")) - 1
        if 0 <= indice < len(total_insumos):
            total_insumos[indice] = 0
            print(f"{nomes_insumos[indice]} deletado.")
            saida_dados()  
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def criar_csv():
    try:
        with open('total_insumos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Fertilizante', 'Quantidade (kg)'])
            for i in range(len(nomes_insumos)):
                writer.writerow([nomes_insumos[i], f"{total_insumos[i]:.2f}"])
        print("Arquivo CSV 'total_insumos.csv' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o arquivo CSV: {e}")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            entrada_dados()
        elif opcao == '2':
            saida_dados()
        elif opcao == '3':
            atualizar_dados()
        elif opcao == '4':
            deletar_dados()
        elif opcao == '5':
            criar_csv()
        elif opcao == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha entre 1 e 6.")

main()
