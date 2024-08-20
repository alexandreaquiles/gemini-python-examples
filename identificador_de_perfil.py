from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
generation_config = {
  "temperature": 0
}

modelo = "gemini-1.5-flash"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")


prompt_sistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

prompt_usuario = carrega("./dados/lista_de_compras_100_clientes.csv")

cliente = genai.GenerativeModel(
    model_name = modelo,
    generation_config=generation_config,
    system_instruction = prompt_sistema )

resposta = cliente.generate_content(prompt_usuario)
print(resposta.text)
