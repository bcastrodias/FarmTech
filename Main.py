def calcular_insumos(cultura, tamanho, tempo_fertilizante):
    fertisoja = 5 
    ferticana = 10  

    if cultura == "1":
        insumos = (tamanho * tempo_fertilizante * fertisoja) / 1000
    elif cultura == "2":
        insumos = (tamanho * tempo_fertilizante * ferticana) / 1000
    else:
        insumos = 0
    return insumos

def estimar_tempo(cultura, ciclos):
    if cultura == "1":  # Soja
        return ciclos * 4, ciclos * 6  # Soja leva de 4 a 6 meses por safra
    elif cultura == "2":  # Cana-de-açúcar
        return ciclos * 12, ciclos * 18  # Cana leva de 12 a 18 meses por safra

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

# Vetores para armazenar os dados de culturas e tamanhos
culturas = []
tamanhos = []
tempos_fertilizante = []

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
        tamanho = float(input("Quantos hectares você pretende plantar? "))
        tempo_fertilizante = int(input("Para quantos ciclos de cultivo (safras) você deseja calcular os insumos? "))

        # Armazenar dados nos vetores
        culturas.append(cultura)
        tamanhos.append(tamanho)
        tempos_fertilizante.append(tempo_fertilizante)

        # Calcular insumos e estimar tempo
        insumos = calcular_insumos(cultura, tamanho, tempo_fertilizante)
        min_tempo, max_tempo = estimar_tempo(cultura, tempo_fertilizante)
        print(f"\nVocê terá {tamanho:.2f} hectares de {nome_cultura(cultura)}, o que demandará {insumos:.2f} quilogramas de nitrogênio.")
        print(f"O tempo estimado de cultivo será entre {min_tempo} e {max_tempo} meses para completar os {tempo_fertilizante} ciclos.\n")

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
                print(f"{i+1}. Cultura: {nome_cultura(culturas[i])}, Tamanho: {tamanhos[i]} hectares, Ciclos de cultivo: {tempos_fertilizante[i]}")

    elif opcao == '3':  # Atualizar dados
        if len(culturas) == 0:
            print("Nenhum dado para atualizar.")
        else:
            index = int(input("Digite o número do dado que deseja atualizar (ex.: 1 para o primeiro dado): ")) - 1
            if 0 <= index < len(culturas):
                cultura = input("Digite '1' para soja ou '2' para cana-de-açúcar para atualizar a cultura: ").lower()
                tamanho = float(input("Atualize o tamanho da área em hectares: "))
                tempo_fertilizante = int(input("Atualize os ciclos de cultivo (safras): "))
                
                culturas[index] = cultura
                tamanhos[index] = tamanho
                tempos_fertilizante[index] = tempo_fertilizante
                
                insumos = calcular_insumos(cultura, tamanho, tempo_fertilizante)
                min_tempo, max_tempo = estimar_tempo(cultura, tempo_fertilizante)
                print(f"\nDado atualizado: {tamanho:.2f} hectares de {nome_cultura(cultura)}, com {insumos:.2f} quilogramas de nitrogênio.")
                print(f"O tempo estimado de cultivo será entre {min_tempo} e {max_tempo} meses para {tempo_fertilizante} ciclos.\n")
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
                print("Dado deletado com sucesso!")
            else:
                print("Número inválido.")

    elif opcao == '5':  # Sair do programa
        print("Encerrando o programa. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")

