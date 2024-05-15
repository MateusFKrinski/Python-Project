import google.generativeai as genai

genai.configure(api_key="AIzaSyB9LTQSR0DgOUXRhSwmymTV0gj1CRJDr2E")

model = genai.GenerativeModel("gemini-pro")

# TODO Fazer a integração de temas para busca de assuntos

response = model.generate_content("Diga 1 tema do mundo animal, com no máximo 40 caracteres", stream=True)

for chunk in response:
    print(chunk.text)

# TODO Associar a geração de pubicações no X com os assuntos gerados com base no tema
# TODO Salvar os temas em banco de dados com as datas
# TODO Fazer a junção da API do X no código e integrar funções
