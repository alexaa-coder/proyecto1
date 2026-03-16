import os
import requests

DOCS_PATH = "./docs"
MAX_CHARS = 8000
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def cargar_documentos(ruta):
    contenido = []
    for root, _, files in os.walk(ruta):
        for f in files:
            if f.endswith(".md"):
                filepath = os.path.join(root, f)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                    texto = fh.read()
                    contenido.append(f"### Archivo: {filepath}\n{texto}")
    return "\n\n".join(contenido)[:MAX_CHARS]

def consultar(pregunta):
    contexto = cargar_documentos(DOCS_PATH)
    prompt = (
        f"Eres un asistente experto en normativa ISO. "
        f"Responde siempre en español. "
        f"A continuación tienes el contenido de un repositorio normativo:\n\n"
        f"{contexto}\n\n"
        f"Pregunta: {pregunta}"
    )
    respuesta = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    return respuesta.json()["response"]

if __name__ == "__main__":
    preguntas = [
        "¿Qué requisitos de control de documentos aparecen en el repositorio?",
        "¿Qué diferencias encuentras entre los controles de ISO-27001 e ISO-13485 en estos documentos?",
        "¿Qué secciones del repositorio cubren la gestión de riesgos?"
    ]

    for p in preguntas:
        print(f"\n🔍 Pregunta: {p}")
        print(f"💬 Respuesta: {consultar(p)}")
        print("-" * 60)
