import csv

print("Olá, bem-vindo ao seu assistente virtual de plantação!")


dados_cultivos = []


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

def nome_cultura(cultura):
    if cultura == 1:
        return "soja"
    elif cultura == 2:
        return "cana-de-açúcar"
    else:
        return "desconhecida"

def recomendar_geometria(cultura):
    if cultura == 1:  # Soja
        return "Quadrado ou Retângulo (preferencial para o manejo de máquinas)"
    elif cultura == 2:  # Cana-de-açúcar
        return "Retângulo longo e estreito (ótimo para fileiras longas)"
    else:
        return "desconhecida"

def calcular_fileiras_e_insumos(largura_campo, comprimento_fileira, espacamento, quantidade_por_metro):
    numero_fileiras = largura_campo / espacamento
    total_metros_pulverizar = numero_fileiras * comprimento_fileira  
    quantidade_total_insumo = total_metros_pulverizar * quantidade_por_metro
    return numero_fileiras, quantidade_total_insumo

def estimar_tempo(cultura, ciclos):
    if cultura == 1:  # Soja
        return ciclos * 4, ciclos * 6  # Soja leva de 4 a 6 meses por safra
    elif cultura == 2:  # Cana-de-açúcar
        return ciclos * 12, ciclos * 18  # Cana leva de 12 a 18 meses por safra

def entrada_dados():
    while True:
        try:
            crops = int(input("Digite 1 se você deseja plantar soja ou 2 se deseja plantar cana-de-açúcar: "))
            if crops == 1 or crops == 2:
                print(f"Você escolheu plantar {nome_cultura(crops)}.")
                break
            else:
                print("Entrada inválida! Por favor, digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número (1 ou 2).")

    
    print(f"Geometria recomendada para {nome_cultura(crops)}: {recomendar_geometria(crops)}")

   
    largura = float(input("Informe a largura do campo (em metros): "))
    comprimento = float(input("Informe o comprimento do campo (em metros): "))
    tamanho = largura * comprimento

    
    nitro = entrada_sim_nao("Você deseja fertilizar com nitrogênio? (sim/não): ")
    fosforo = entrada_sim_nao("Você deseja fertilizar com fósforo? (sim/não): ")
    pota = entrada_sim_nao("Você deseja fertilizar com potássio? (sim/não): ")
    cal = entrada_sim_nao("Você deseja fertilizar com cálcio? (sim/não): ")

    if crops == 1:  # Soja
        num_safras = int(input("Quantas safras de soja você pretende cultivar? (1-2 por ano): "))
    elif crops == 2:  # Cana-de-açúcar
        num_safras = int(input("Quantas safras de cana-de-açúcar você pretende cultivar? (1-2 por ano): "))

    
    min_tempo, max_tempo = estimar_tempo(crops, num_safras)

    
    espacamento = 0.5 if crops == 1 else 1.5  
    quantidade_por_metro = 500  
    numero_fileiras, quantidade_total_insumo = calcular_fileiras_e_insumos(largura, comprimento, espacamento, quantidade_por_metro)

    
    nitrosoja = 5
    nitrocana = 10
    fosforosoja = 10
    fosforocana = 10
    potasoja = 10
    potacana = 20
    calsoja = 3
    calcana = 6

    total_insumos = [0, 0, 0, 0]  # [Nitrogênio, Fósforo, Potássio, Cálcio]

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

    
    dados = {
        'cultura': crops,
        'largura': largura,
        'comprimento': comprimento,
        'tamanho': tamanho,
        'num_safras': num_safras,
        'total_insumos': total_insumos.copy(),
        'numero_fileiras': numero_fileiras,
        'quantidade_total_insumo': quantidade_total_insumo,
        'min_tempo': min_tempo,
        'max_tempo': max_tempo,
        'fertilizantes': {
            'nitro': nitro,
            'fosforo': fosforo,
            'pota': pota,
            'cal': cal
        }
    }
    dados_cultivos.append(dados)

    
    saida_dados()

def saida_dados():
    if len(dados_cultivos) == 0:
        print("Nenhum dado inserido.")
    else:
        for idx, dados in enumerate(dados_cultivos):
            print(f"\n--- Dados do cultivo {idx + 1} ---")
            print(f"Cultura: {nome_cultura(dados['cultura'])}")
            print(f"Tamanho do campo: {dados['tamanho']} m²")
            print(f"Dimensões do campo: {dados['largura']} m x {dados['comprimento']} m")
            print(f"Número de safras: {dados['num_safras']}")
            print(f"Tempo estimado de cultivo: entre {dados['min_tempo']} e {dados['max_tempo']} meses")
            print(f"Número de fileiras: {dados['numero_fileiras']:.0f}")
            print(f"Quantidade total de insumo para pulverização: {dados['quantidade_total_insumo'] / 1000:.2f} litros")

            print("Demandas de fertilizantes para o período escolhido:")
            for i in range(len(nomes_insumos)):
                print(f"- {nomes_insumos[i]}: {dados['total_insumos'][i]:.2f} kg")
            print()

def atualizar_dados():
    if len(dados_cultivos) == 0:
        print("Nenhum dado para atualizar.")
        return
    saida_dados()
    try:
        indice = int(input("Digite o número do cultivo que deseja atualizar: ")) - 1
        if 0 <= indice < len(dados_cultivos):
            dados = dados_cultivos[indice]

            
            while True:
                try:
                    crops = int(input("Digite 1 se você deseja plantar soja ou 2 se deseja plantar cana-de-açúcar: "))
                    if crops == 1 or crops == 2:
                        print(f"Você escolheu plantar {nome_cultura(crops)}.")
                        break
                    else:
                        print("Entrada inválida! Por favor, digite 1 ou 2.")
                except ValueError:
                    print("Entrada inválida! Por favor, digite um número (1 ou 2).")

            
            print(f"Geometria recomendada para {nome_cultura(crops)}: {recomendar_geometria(crops)}")

            
            largura = float(input("Informe a largura do campo (em metros): "))
            comprimento = float(input("Informe a comprimento do campo (em metros): "))
            tamanho = largura * comprimento

            
            nitro = entrada_sim_nao("Você deseja fertilizar com nitrogênio? (sim/não): ")
            fosforo = entrada_sim_nao("Você deseja fertilizar com fósforo? (sim/não): ")
            pota = entrada_sim_nao("Você deseja fertilizar com potássio? (sim/não): ")
            cal = entrada_sim_nao("Você deseja fertilizar com cálcio? (sim/não): ")

            if crops == 1:  # Soja
                num_safras = int(input("Quantas safras de soja você pretende cultivar? (1-2 por ano): "))
            elif crops == 2:  # Cana-de-açúcar
                num_safras = int(input("Quantas safras de cana-de-açúcar você pretende cultivar? (1-2 por ano): "))

            
            min_tempo, max_tempo = estimar_tempo(crops, num_safras)

            
            espacamento = 0.5 if crops == 1 else 1.5  
            quantidade_por_metro = 500  
            numero_fileiras, quantidade_total_insumo = calcular_fileiras_e_insumos(largura, comprimento, espacamento, quantidade_por_metro)

            nitrosoja = 5
            nitrocana = 10
            fosforosoja = 10
            fosforocana = 10
            potasoja = 10
            potacana = 20
            calsoja = 3
            calcana = 6

            total_insumos = [0, 0, 0, 0]  # [Nitrogênio, Fósforo, Potássio, Cálcio]

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

            
            dados.update({
                'cultura': crops,
                'largura': largura,
                'comprimento': comprimento,
                'tamanho': tamanho,
                'num_safras': num_safras,
                'total_insumos': total_insumos.copy(),
                'numero_fileiras': numero_fileiras,
                'quantidade_total_insumo': quantidade_total_insumo,
                'min_tempo': min_tempo,
                'max_tempo': max_tempo,
                'fertilizantes': {
                    'nitro': nitro,
                    'fosforo': fosforo,
                    'pota': pota,
                    'cal': cal
                }
            })

            print("Dados atualizados com sucesso!")
            saida_dados()
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def deletar_dados():
    if len(dados_cultivos) == 0:
        print("Nenhum dado para deletar.")
        return
    saida_dados()
    try:
        indice = int(input("Digite o número do cultivo que deseja deletar: ")) - 1
        if 0 <= indice < len(dados_cultivos):
            del dados_cultivos[indice]
            print("Dados deletados com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def criar_csv():
    if len(dados_cultivos) == 0:
        print("Nenhum dado para salvar.")
        return
    try:
        with open('dados_cultivos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['Cultivo', 'Largura (m)', 'Comprimento (m)', 'Tamanho (m²)', 'Nº de safras', 'Tempo mínimo (meses)', 'Tempo máximo (meses)', 'Nº de fileiras', 'Total insumo pulverização (litros)']
            header += nomes_insumos
            writer.writerow(header)
            for dados in dados_cultivos:
                row = [
                    nome_cultura(dados['cultura']),
                    dados['largura'],
                    dados['comprimento'],
                    dados['tamanho'],
                    dados['num_safras'],
                    dados['min_tempo'],
                    dados['max_tempo'],
                    int(dados['numero_fileiras']),
                    dados['quantidade_total_insumo'] / 1000  
                ]
                row += [f"{val:.2f}" for val in dados['total_insumos']]
                writer.writerow(row)
        print("Arquivo CSV 'dados_cultivos.csv' criado com sucesso!")
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
