from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


def conta_tokens(prompt, modelo):
  model_info = genai.get_model(f"models/{modelo}")
  max_input_tokens = model_info.input_token_limit
  max_output_tokens = model_info.output_token_limit

  cliente = genai.GenerativeModel(model_name = modelo)
  contagem_tokens = cliente.count_tokens(prompt)
  return max_input_tokens, max_output_tokens, contagem_tokens

prompt = "Você é um categorizador de produtos."

modelo = "gemini-1.5-flash"
max_input, max_output, contagem = conta_tokens(prompt, modelo)
print(f"{max_input}") # 1048576
print(f"{max_output}") # 8192
print(f"Quantos tokens temos para o modelo {modelo}: ", contagem)
