from flask import Flask, render_template, request, jsonify
from pdf2image import convert_from_path
import pytesseract
import openai
import os

app = Flask(__name__)

# Configuração da chave API da OpenAI
openai.api_key = ''

# Definir o caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Funções auxiliares
def extrair_texto_do_pdf(pdf_path):
    imagens = convert_from_path(pdf_path)
    texto_extraido = ''
    for imagem in imagens:
        texto = pytesseract.image_to_string(imagem, lang='por')
        texto_extraido += texto
    return texto_extraido

def dividir_texto(texto, max_tokens=2048):
    partes = []
    palavras = texto.split()
    parte = ''
    for palavra in palavras:
        if len(parte) + len(palavra) + 1 > max_tokens:
            partes.append(parte)
            parte = palavra
        else:
            parte += ' ' + palavra
    if parte:
        partes.append(parte)
    return partes

def analisar_exame_por_partes(partes):
    resultados = []
    for parte in partes:
        prompt = (
            "Analise o seguinte exame de sangue e diga se todos os testes estão em dia, "
            "se o paciente tem algum problema ou está saudável e caso tenha algo fora do comum fale qual problema ele pode desenvolver. Exame:\n\n"
            f"{parte}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente médico."},
                {"role": "user", "content": prompt},
            ],
        )
        resultados.append(response['choices'][0]['message']['content'])
    return '\n'.join(resultados)

# Rotas do Flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def upload():
    if 'pdfFile' not in request.files:
        return jsonify({'error': 'No PDF file provided'}), 400

    pdf_file = request.files['pdfFile']
    pdf_path = os.path.join('uploads', pdf_file.filename)
    pdf_file.save(pdf_path)

    texto_exame = extrair_texto_do_pdf(pdf_path)
    partes = dividir_texto(texto_exame)
    resultado = analisar_exame_por_partes(partes)

    return jsonify({'result': resultado})

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
