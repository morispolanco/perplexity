import streamlit as st
import requests

def make_api_call(question, api_key):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "mistral-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "Responde preguntas sobre las leyes de Guatemala, citando las fuentes."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {api_key}"  # Incluye la API key en los encabezados
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

def main():
    st.title("Preguntas sobre las leyes de Guatemala")

    question = st.text_input("Haz tu pregunta:")
    api_key = "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"  # Reemplaza con tu clave real

    if st.button("Obtener respuesta"):
        if question:
            answer = make_api_call(question, api_key)
            st.write("Respuesta:", answer)
        else:
            st.warning("Por favor, ingresa una pregunta.")

if __name__ == "__main__":
    main()
