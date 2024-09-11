# Modulos Necesarios 
from fastapi import FastAPI, HTTPException# Crea la Api y maneja errores
import httpx # Peticiones

app = FastAPI() # Aplicacion en si 
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"

# Ruta general para obtener el nombre del pokemon y sus recursos de datos
@app.get("/api/general/{pokemon}")
async def get_pokemon_general(pokemon: str):
    url = f"{POKEAPI_URL}{pokemon.lower()}"
    async with httpx.AsyncClient() as client:#Cliente para peticion
        response = await client.get(url) #Solicitud get a la api
        if response.status_code != 200: #Excepcion por respuesta no exitosa
            raise HTTPException(status_code=404, detail="Pokémon not found")
        data = response.json() #respuesta en formato json
        #Diccionario 
        return {
            "name": data["name"],
            "resource": url
        }

# Ruta específica para obtener detalles del pokemon
@app.get("/api/especifico/{pokemon}")
async def get_pokemon_details(pokemon: str):
    url = f"{POKEAPI_URL}{pokemon.lower()}"
    async with httpx.AsyncClient() as client: 
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokémon not found")
        data = response.json()
        return {
            "name": data["name"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "pokedex_number": data["id"],
            "sprites": data["sprites"]["front_default"],
            "types": [t["type"]["name"] for t in data["types"]]
        }

# Ruta para editar la información de un pokemon (simulada)
@app.put("/api/editar/{pokemon}")
async def edit_pokemon(pokemon: str, updated_data: dict):
    # Aquí simulamos que editamos la información de un pokemon en un sistema externo
    # En un caso real, esto debería guardar los cambios en una base de datos o servicio externo
    return {
        "message": f"Pokémon {pokemon} updated successfully",
        "new_data": updated_data # Devolvemos los datos que el usuario envio para mostar los cambios
    }
