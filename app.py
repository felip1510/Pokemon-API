import requests

nome = input("Digite o nome do Pokémon: ")

url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    print(f"Pokémon: {dados['name'].capitalize()}")
    print(f"Altura: {dados['height']}")
    print(f"Peso: {dados['weight']}")

    tipos = dados['types']

    print("Tipo(s):")
    for tipo in tipos:
        print(f"- {tipo['type']['name'].capitalize()}")

else:
    print("Não foi possível consultar o Pokémon.")
