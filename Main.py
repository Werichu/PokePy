import requests

B_URL = "https://pokeapi.co/api/v2/pokemon/"
S_URL = "https://pokeapi.co/api/v2/pokemon-species/"

pokemon = input("digite el pokemon a buscar: ") # el usuario digita el pokemon que quiere encontrar 

# obtener datos del pokemon
def obtenerDatos(nombre_o_id):
    url = f"{B_URL}{nombre_o_id}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200: # si los datos se encuentran en la base de datos de la API, entonces esos datos se retornaran 
        datos_pokemon = respuesta.json()

        return datos_pokemon
    else:# si no, manda un error y el programa termina
        print(f"No se encontro el pokemon: {respuesta.status_code}")
        return None
    
# obtener descripcion de pokemon
def obtenerDescripcion(nombre_o_id):
    url = f"{S_URL}{nombre_o_id}/"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_species = respuesta.json()

        for entry in datos_species["flavor_text_entries"]: # Hace un ciclo en todo el json que capture
        #flavor es una lista de los tipos
            if entry["language"]["name"] == "es":
                return entry["flavor_text"].replace("\n"," ").replace("\f"," ") #Quita espacios inecesarios de json
    return None

datos = obtenerDatos(pokemon) # el nombre se pasa a la funcion y se almacena en la variable "datos"
descripcion = obtenerDescripcion(pokemon) # la descripcion de pokemon se guarda en esta variable

if datos: # si se encuentran datos entonces se muestra la informacion
    print(f"Nombre: {datos['name']}")
    print(f"Altura: {datos['height']}")

    '''Obtencion de el tipo del pokemon'''
    tipo = datos['types'][0]['type']['name'] #obtenemos en tipo del pokemon en este caso sera el primero

    try: 
        segTipo = datos['types'][1]['type']['name'] #obtenemos el segundo tipo del pokemon
    except:
        segTipo = "-" # en caso de que no exista se remplaza por un caracter nulo
    
    print(f"Tipo: {tipo} {segTipo}") # se imprime el tipo

print(f"Descripcion: {descripcion}") # muestra la descripcion