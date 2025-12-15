import requests

B_URL = "https://pokeapi.co/api/v2/pokemon/"

# obtener datos del pokemon

def obtenerDatos(nombre_o_id):
    url = f"{B_URL}{nombre_o_id}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200: 
        datos_pokemon = respuesta.json()

        return datos_pokemon
    else:
        print(f"No se encontro el pokemon: {respuesta.status_code}")
        return None
    

pokemon = input("digite el pokemon a buscar: ")

datos = obtenerDatos(pokemon)

if datos:
    print(f"Nombre: {datos['name']}")
    print(f"Altura: {datos['height']}")

    tipo = datos['types'][0]['type']['name']
    print(f"Tipo: {tipo}")