import requests

# URL de tu endpoint
url = "http://localhost:8000/api/search/"

# Datos de la consulta
params = {
    "prompt": "Explorar inteligencia artificial"
}

try:
    # Realizar la solicitud GET
    response = requests.get(url, params=params)
    
    # Verificar el estado de la respuesta
    if response.status_code == 200:
        print("Respuesta exitosa:")
        print(response.json())  # Imprimir resultados
    else:
        print(f"Error: {response.status_code}")
        print(response.json())  # Imprimir mensaje de error

except Exception as e:
    print(f"Error durante la solicitud: {str(e)}")
