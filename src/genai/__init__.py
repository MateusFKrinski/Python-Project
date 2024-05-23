import google.generativeai as genai

genai.configure(api_key="AIzaSyB9LTQSR0DgOUXRhSwmymTV0gj1CRJDr2E")
model = genai.GenerativeModel("gemini-pro")


class Genai:
    def __init__(self, generic_theme):
        self.generic_theme = generic_theme

    def generate_theme_base(self):
        response = model.generate_content(
            f"Gere um tema: {self.generic_theme}."
            f" Com no máximo 30 caracteres. Maximizar resultados. Não repetir a palavra."
            f" Entre uma e três palavras",
            stream=True)
        for chunk in response:
            return chunk.text

    def generate_themes(self, theme):
        response = model.generate_content(
            f"Gere um tema mais profundo sobre: {theme}."
            f"Não retita o tema pai: {self.generic_theme}."
            f"Resposta com até 60 caracteres."
            f"Focar em uma área específica."
            f"Não se repetir."
            f"Frase composta bem estruturada",
            stream=True)
        for chunk in response:
            return chunk.text

