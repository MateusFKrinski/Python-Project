import google.generativeai as genai

genai.configure(api_key="AIzaSyB9LTQSR0DgOUXRhSwmymTV0gj1CRJDr2E")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Cite animais azuis", stream=True)

for chunk in response:
    print(chunk.text)
    print("_"*80)
