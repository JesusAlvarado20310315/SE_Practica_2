import json

def cargar_conocimiento():
    try:
        with open('conocimiento.json', 'r') as archivo:
            conocimiento = json.load(archivo)
    except FileNotFoundError:
        conocimiento = {'preguntas': [], 'respuestas': []}
    return conocimiento

def guardar_conocimiento(conocimiento):
    with open('conocimiento.json', 'w') as archivo:
        json.dump(conocimiento, archivo)

def chatbot():
    conocimiento = cargar_conocimiento()

    print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?")
    while True:
        entrada_usuario = input("> ").lower()  # Convertir la entrada del usuario a minúsculas

        if entrada_usuario in ["adios", "salir"]:
            print("¡Hasta luego!")
            break

        respuesta = None
        for i, pregunta in enumerate(conocimiento['preguntas']):
            if entrada_usuario in pregunta.lower():  # Convertir la pregunta almacenada a minúsculas para la comparación
                respuesta = conocimiento['respuestas'][i]
                print(respuesta)
                break

        if respuesta is None:
            print("Lo siento, no entiendo. ¿Me podrías enseñar cómo responder a eso? (Si/No)")
            respuesta_aprender = input("> ").lower()
            if respuesta_aprender == "si":
                print("Claro, ¿cuál debería ser mi respuesta?")
                nueva_respuesta = input("> ")
                conocimiento['preguntas'].append(entrada_usuario)
                conocimiento['respuestas'].append(nueva_respuesta)
                guardar_conocimiento(conocimiento)
                print("¡Entendido! Aprendí algo nuevo.")
            else:
                print("De acuerdo, en qué te puedo ayudar?")

if __name__ == "__main__":
    chatbot()