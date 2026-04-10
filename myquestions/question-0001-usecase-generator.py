import numpy as np

def generar_caso_de_uso():
    # Datos aleatorios: cargas entre 100 y 500 kN
    cargas_random = np.random.uniform(100, 500, 10)
def generar_caso_de_uso():
    # Datos aleatorios: cargas entre 100 y 500 kN
    cargas_random = np.random.uniform(100, 500, 10)
    limite_random = np.random.uniform(250, 350)
    
    # Lógica interna para obtener el resultado esperado
    resultado = bool(np.mean(cargas_random) > limite_random)
    
    input_data = {
        "cargas": cargas_random,
        "limite_seguridad": limite_random
    }
    output_data = resultado
    
    return input_data, output_data
