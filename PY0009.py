palabras = ["python", "java   ", "javascript", "go", "rust", "", ""]

diccionario = {palabra.strip(): len(palabra.strip()) for palabra in palabras}

print(diccionario)