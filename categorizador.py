from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 0,
  # "top_p": 0.95,
  # "top_k": 64,
  "max_output_tokens": 300,
  # "response_mime_type": "text/plain",
}

modelo = "gemini-1.5-flash"

def categoriza_produtos(nome_produto):
  prompt_sistema = f"""
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas

      Moda ética
      Roupas feitas de materiais reciclados
      Roupas orgânicas
      Calçados ecológicos
      Bolsas e mochilas sustentáveis
      Cosméticos naturais e orgânicos
      Produtos de higiene sem plástico
      Produtos de skincare sustentáveis
      Cuidados capilares naturais
      Móveis sustentáveis
      Decoração ecológica
      Utensílios de cozinha recicláveis
      Produtos de limpeza ecológicos
      Alimentos orgânicos e locais
      Produtos a granel e sem embalagem
      Bebidas naturais e artesanais
      Snacks saudáveis e sustentáveis
      Eletrônicos sustentáveis
      Gadgets de energia solar
      Carregadores ecológicos
      Dispositivos de economia de energia
      Roupas infantis orgânicas
      Brinquedos de madeira e sustentáveis
      Fraldas reutilizáveis
      Produtos de higiene natural para bebês
      Equipamentos esportivos sustentáveis
      Roupas esportivas ecológicas
      Produtos para atividades ao ar livre
      Kits de jardinagem ecológica
      Ferramentas sustentáveis para jardinagem
      Compostagem e vermicompostagem
      Rações naturais e orgânicas
      Acessórios ecológicos para pets
      Produtos de higiene naturais para pets
      Papel reciclado e FSC
      Canetas e lápis ecológicos
      Materiais de escritório sem plástico

    # Formato da Saída
      Produto: Nome do Produto
      Categoria: apresente a categoria do produto

    # Exemplo de Saída
      Produto: Escova elétrica com recarga solar
      Categoria: Eletrônicos Verdes
    """
  
  cliente = genai.GenerativeModel(
    model_name = modelo,
    generation_config=generation_config,
    system_instruction = prompt_sistema
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
  )


  resposta = cliente.generate_content(nome_produto)

  return resposta.text

while(True):
  nome_produto = input("Digite o nome de um produto (ou sair): ")
  if nome_produto == "sair":
    break
  resposta_categorizacao = categoriza_produtos(nome_produto)
  print(f"\n{resposta_categorizacao}\n")