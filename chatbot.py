import json
import tkinter as tk

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

def abrir_ventana_aprendizaje(ventana, pregunta, conocimiento):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Aprender nueva respuesta")

    pregunta_label = tk.Label(nueva_ventana, text="Pregunta:")
    pregunta_label.pack()
    pregunta_entry = tk.Entry(nueva_ventana)
    pregunta_entry.insert(tk.END, pregunta)
    pregunta_entry.pack()

    respuesta_label = tk.Label(nueva_ventana, text="Escribe tu respuesta:")
    respuesta_label.pack()
    respuesta_entry = tk.Entry(nueva_ventana)
    respuesta_entry.pack()

    guardar_button = tk.Button(nueva_ventana, text="Guardar", command=lambda: guardar_respuesta(pregunta_entry.get(), respuesta_entry.get(), conocimiento, nueva_ventana))
    guardar_button.pack()

def guardar_respuesta(pregunta, respuesta, conocimiento, ventana):
    conocimiento['preguntas'].append(pregunta.lower())
    conocimiento['respuestas'].append(respuesta)
    guardar_conocimiento(conocimiento)
    ventana.destroy()

def aprender_respuesta(ventana, entrada, respuesta_label, conocimiento, si_button, no_button):
    respuesta_label.config(text="No se qué responder, ¿quieres agregar una respuesta? (Si/No)")
    si_button.pack()
    no_button.pack()

def ocultar_botones(si_button, no_button):
    si_button.pack_forget()
    no_button.pack_forget()

def mostrar_respuesta(ventana, entrada, respuesta_label, conocimiento, si_button, no_button):
    entrada_usuario = entrada.get().lower()

    if entrada_usuario in conocimiento['preguntas']:
        respuesta = conocimiento['respuestas'][conocimiento['preguntas'].index(entrada_usuario)]
    else:
        respuesta = "No se qué responder, ¿quieres agregar una respuesta? (Si/No)"
        aprender_respuesta(ventana, entrada, respuesta_label, conocimiento, si_button, no_button)

    respuesta_label.config(text=respuesta)

def chatbot():
    conocimiento = cargar_conocimiento()

    ventana = tk.Tk()
    ventana.title("Chatbot")

    bienvenida_label = tk.Label(ventana, text="¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?")
    entrada = tk.Entry(ventana)
    si_button = tk.Button(ventana, text="Si", command=lambda: abrir_ventana_aprendizaje(ventana, entrada.get(), conocimiento))
    no_button = tk.Button(ventana, text="No", command=lambda: [respuesta_label.config(text="Entendido, en qué más puedo ayudarte?"), ocultar_botones(si_button, no_button)])
    enviar_button = tk.Button(ventana, text="Enviar", command=lambda: mostrar_respuesta(ventana, entrada, respuesta_label, conocimiento, si_button, no_button))
    respuesta_label = tk.Label(ventana, text="")

    bienvenida_label.pack()
    entrada.pack()
    enviar_button.pack()
    respuesta_label.pack()

    ventana.mainloop()

if __name__ == "__main__":
    chatbot()
