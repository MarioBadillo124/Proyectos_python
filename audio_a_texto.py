import speech_recognition as sr

# Configuración del reconocimiento de audio
recognizer = sr.Recognizer()

# Abrir el micrófono
with sr.Microphone() as source:
    print("Ajustando ruido de fondo... por favor espera.")
    recognizer.adjust_for_ambient_noise(source)
    print("Puedes comenzar a hablar...")

    while True:
        try:
            # Escuchar el audio, esperando indefinidamente hasta detectar algo
            print("Escuchando... (se detendrá si no hay sonido durante 10 segundos)")
            audio = recognizer.listen(source, timeout=10)  # Timeout de 10 segundos sin detectar nada
            print("Audio detectado, procesando...")

            # Intentar reconocer el audio y convertirlo a texto
            text = recognizer.recognize_google(audio, language="es-ES")
            print(f"Texto reconocido: {text}")

            # Guardar el texto en un archivo
            with open("transcripcion.txt", "a") as file:
                file.write(text + "\n")
            print("Texto guardado en 'transcripcion.txt'.")

        except sr.WaitTimeoutError:
            # Si no se detecta nada por 10 segundos, reinicia el ciclo
            print("No se detectó audio en 10 segundos, reiniciando...")

        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError as e:
            print(f"Error al conectar con el servicio de reconocimiento: {e}")
