print("Olá, bem-vindo ao seu assistente virtual de plantação!")

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

fertisoja = 5  
ferticana = 10 

tamanho = int(input("Quantos metros quadrados você pretende plantar? "))
tempofertilizante = int(input("Por quantos anos pretende fertilizar? "))

if crops == 1:
    insumos = (tamanho * tempofertilizante * fertisoja) / 1000  
elif crops == 2:
    insumos = (tamanho * tempofertilizante * ferticana) / 1000  

print(f"Você terá {tamanho} metros quadrados de {'soja' if crops == 1 else 'cana-de-açúcar'}, o que demandará {insumos:.2f} quilogramas de nitrogênio para atender o período escolhido.")
