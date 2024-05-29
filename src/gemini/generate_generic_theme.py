import google.generativeai as genai

genai.configure(api_key="AIzaSyB9LTQSR0DgOUXRhSwmymTV0gj1CRJDr2E")
model = genai.GenerativeModel("gemini-pro")


def generate_generic_theme():
    response = model.generate_content(
        f"Defina um tema global para fundar curiosidades"
        f"Ele deve ser palavra chave."
        f"Uma única frase, que se complemente, com máximo de três palavras"
        f"Pode ser qualquer tema genérico"
        f"Não repita a palavra mundo e conhecimento, foque em temas",
        stream=True)
    for chunk in response:
        return chunk.text


generic_theme = generate_generic_theme()
