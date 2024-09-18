def calcular_insumos(cultura, tamanho, tempo_fertilizante):
    # Taxas de fertilizante por metro quadrado (em kg/m² por safra)
    fertisoja = 0.04  # Soja: 400 kg por hectare = 0,04 kg/m²
    ferticana = 0.1   # Cana-de-açúcar: 1000 kg por hectare = 0,1 kg/m²

    if cultura == "1":
        # Insumos para soja em metros quadrados e ciclos de safra
        insumos = (tamanho * tempo_fertilizante * fertisoja)
    elif cultura == "2":
        # Insumos para cana em metros quadrados e ciclos de safra
        insumos = (tamanho * tempo_fertilizante * ferticana)
    else:
        insumos = 0
    return insumos

def estimar_tempo(cultura, ciclos):
    if cultura == "1":  # Soja
        return ciclos * 4, ciclos * 6  # Soja leva de 4 a 6 meses por safra
    elif cultura == "2":  # Cana-de-açúcar
        return ciclos * 12, ciclos * 18  # Cana leva de 12 a 18 meses por safra

def calcular_fileiras_e_insumos(largura_campo, comprimento_fileira, espacamento, quantidade_por_metro):
    numero_fileiras = largura_campo / espacamento
    total_metros_pulverizar = numero_fileiras * comprimento_fileira  # Total de metros a serem pulverizados
    quantidade_total_insumo = total_metros_pulverizar * quantidade_por_metro
    return numero_fileiras, quantidade_total_insumo

def menu():
    print("\n=====================")
    print("  Menu de Opções  ")
    print("=====================")
    print("1. Entrada de dados")
    print("2. Exibir dados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair do programa")
    print("=====================\n")

# Função para exibir o nome correto da cultura
def nome_cultura(cultura):
    if cultura == "1":
        return "soja"
    elif cultura == "2":
        return "cana-de-açúcar"
    else:
        return "desconhecida"

# Função para recomendar a geometria com base na cultura
def recomendar_geometria(cultura):
    if cultura == "1":  # Soja
        return "Quadrado ou Retângulo (preferencial para o manejo de máquinas)"
    elif cultura == "2":  # Cana-de-açúcar
        return "Retângulo longo e estreito (ótimo para fileiras longas)"
    else:
        return "desconhecida"

# Vetores para armazenar os dados de culturas e tamanhos
culturas = []
tamanhos = []
tempos_fertilizante = []
fileiras = []
insumos_totais = []

# Loop principal
while True:
    print("\nOlá, bem-vindo ao seu assistente virtual de plantação!")
    menu()
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':  # Entrada de dados
        cultura = input("Digite '1' para plantar soja ou '2' para plantar cana-de-açúcar: ").lower()
        if cultura not in ["1", "2"]:
            print("Cultura inválida! Tente novamente.")
            continue
        
        # Recomendação de geometria com base na cultura
        print(f"Geometria recomendada para {nome_cultura(cultura)}: {recomendar_geometria(cultura)}")
        
        largura = float(input("Informe a largura do campo (em metros): "))
        comprimento = float(input("Informe o comprimento do campo (em metros): "))
        tamanho = largura * comprimento
        
        tempo_fertilizante = int(input("Para quantos ciclos de cultivo (safras) você deseja calcular os insumos? "))

        # Armazenar dados nos vetores
        culturas.append(cultura)
        tamanhos.append(tamanho)
        tempos_fertilizante.append(tempo_fertilizante)

        # Calcular insumos e estimar tempo
        insumos = calcular_insumos(cultura, tamanho, tempo_fertilizante)
        min_tempo, max_tempo = estimar_tempo(cultura, tempo_fertilizante)
        
        # Cálculo do número de fileiras e insumos por fileira
        espacamento = 0.5 if cultura == "1" else 1.5  # 0,5m para soja, 1,5m para cana
        quantidade_por_metro = 500  # mL/m de pulverização
        numero_fileiras, quantidade_total_insumo = calcular_fileiras_e_insumos(largura, comprimento, espacamento, quantidade_por_metro)

        # Armazenar informações de fileiras e insumos totais
        fileiras.append(numero_fileiras)
        insumos_totais.append(quantidade_total_insumo)

        # Exibir resultados
        print(f"\nVocê terá {tamanho:.2f} metros quadrados de {nome_cultura(cultura)}.")
        print(f"Isso demandará {insumos:.2f} quilogramas de fertilizante para os {tempo_fertilizante} ciclos.")
        print(f"O tempo estimado de cultivo será entre {min_tempo} e {max_tempo} meses.")
        print(f"Serão {numero_fileiras:.0f} fileiras de plantio e {quantidade_total_insumo / 1000:.2f} litros de insumo para pulverização por metro.\n")

        # Perguntar se deseja voltar ao menu ou encerrar
        continuar = input("Deseja voltar ao menu ou encerrar o programa? Digite '1' para voltar ao menu e '2' para encerrar: ")
        if continuar == '2':
            print("Encerrando o programa. Até logo!")
            break

    elif opcao == '2':  # Exibir dados
        if len(culturas) == 0:
            print("Nenhum dado inserido.")
        else:
            print("\nDados atuais:")
            for i in range(len(culturas)):
                print(f"\n--- Dados da cultura {i+1} ---")
                print(f"Cultura: {nome_cultura(culturas[i])}")
                print(f"Tamanho do campo: {tamanhos[i]:.2f} m²")
                print(f"Número de fileiras: {fileiras[i]:.0f}")
                print(f"Total de insumos para pulverização: {insumos_totais[i] / 1000:.2f} litros")
                print(f"Tempo de fertilizante: {tempos_fertilizante[i]} ciclos")
    
    elif opcao == '3':  # Atualizar dados
        if len(culturas) == 0:
            print("Nenhum dado para atualizar.")
        else:
            index = int(input("Digite o número do dado que deseja atualizar (ex.: 1 para o primeiro dado): ")) - 1
            if 0 <= index < len(culturas):
                cultura = input("Digite '1' para soja ou '2' para cana-de-açúcar para atualizar a cultura: ").lower()
                largura = float(input("Atualize a largura do campo (em metros): "))
                comprimento = float(input("Atualize o comprimento do campo (em metros): "))
                tamanho = largura * comprimento
                tempo_fertilizante = int(input("Atualize os ciclos de cultivo (safras): "))
                
                culturas[index] = cultura
                tamanhos[index] = tamanho
                tempos_fertilizante[index] = tempo_fertilizante
                
                insumos = calcular_insumos(cultura, tamanho, tempo_fertilizante)
                min_tempo, max_tempo = estimar_tempo(cultura, tempo_fertilizante)
                espacamento = 0.5 if cultura == "1" else 1.5
                numero_fileiras, quantidade_total_insumo = calcular_fileiras_e_insumos(largura, comprimento, espacamento, quantidade_por_metro)
                
                fileiras[index] = numero_fileiras
                insumos_totais[index] = quantidade_total_insumo

                print(f"\nDado atualizado: {tamanho:.2f} metros quadrados de {nome_cultura(cultura)}.")
                print(f"Isso demandará {insumos:.2f} quilogramas de fertilizante para os {tempo_fertilizante} ciclos.")
                print(f"O tempo estimado de cultivo será entre {min_tempo} e {max_tempo} meses.")
                print(f"Serão {numero_fileiras:.0f} fileiras de plantio e {quantidade_total_insumo / 1000:.2f} litros de insumo para pulverização por metro.\n")
            else:
                print("Número inválido.")

    elif opcao == '4':  # Deletar dados
        if len(culturas) == 0:
            print("Nenhum dado para deletar.")
        else:
            index = int(input("Digite o número do dado que deseja deletar (ex.: 1 para o primeiro dado): ")) - 1
            if 0 <= index < len(culturas):
                del culturas[index]
                del tamanhos[index]
                del tempos_fertilizante[index]
                del fileiras[index]
                del insumos_totais[index]
                print("Dado deletado com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == '5':  # Sair do programa
        print("Encerrando o programa. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
