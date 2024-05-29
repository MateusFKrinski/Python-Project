import google.generativeai as genai

genai.configure(api_key="AIzaSyB9LTQSR0DgOUXRhSwmymTV0gj1CRJDr2E")
model = genai.GenerativeModel("gemini-pro")


def description_theme(theme):
    response = model.generate_content(
        f"Explorar o Tema: {theme}" +
        f"Descrever o {theme}" +
        "Escrever um Texto Perspicaz" +
        "Criar um Texto Sólido" +
        "Preparar-se para uma Publicação em Rede Social" +
        "Sem cortar o texto em sua explicação",
        stream=True)
    for chunk in response:
        return chunk.text


def generate_text_by_theme(theme):
    response = model.generate_content(
        f"Escreva Um Texto Sobre: {theme}" +
        "Ele Deve Denvendar, Descobrir Algo" +
        "Caso Haja Falta de Informações, Pode Fazer Sua Inferência" +
        "Sem cortar o texto em sua explicação" +
        "O Texto Precisa Ter No Mínimo 250 palavras",
        stream=True)
    for chunk in response:
        return chunk.text
