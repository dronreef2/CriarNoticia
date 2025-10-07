"""
Versão Funcional Simplificada do CriarNoticia
============================================

Esta versão usa a API atual do Google Generative AI de forma simplificada.
"""

import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar API
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ GOOGLE_API_KEY não encontrada no arquivo .env")
    exit(1)

genai.configure(api_key=api_key)
print("✅ API configurada com sucesso!")

# Tópico
topico = "lançamento e recepção do Apple Vision Pro"

# Prompt
prompt = f"""
Atue como um analista de notícias. Crie um briefing sobre: '{topico}'.

Retorne um JSON com esta estrutura EXATA:
{{
    "topico_central": "o tema principal",
    "artigos": [
        {{
            "titulo": "título da matéria",
            "fonte": "veículo de comunicação",
            "resumo_curto": "resumo de 1-2 frases"
        }}
    ],
    "analise_sintetizada": "análise em 2 parágrafos",
    "prompt_para_imagem": "prompt em inglês para geração de imagem"
}}

Inclua 3-5 artigos relevantes. Retorne APENAS o JSON, sem texto adicional.
"""

print(f"\n🚀 Gerando briefing sobre: {topico}\n")

try:
    # Tentar diferentes modelos até encontrar um disponível
    modelos_para_tentar = ['gemini-2.0-flash-exp', 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    modelo_funcionou = None
    for nome_modelo in modelos_para_tentar:
        try:
            print(f"Tentando modelo: {nome_modelo}...")
            model = genai.GenerativeModel(nome_modelo)
            response = model.generate_content(prompt)
            modelo_funcionou = nome_modelo
            print(f"✅ Modelo {nome_modelo} funcionou!\n")
            break
        except Exception as e:
            print(f"⚠️  {nome_modelo} não disponível: {str(e)[:100]}")
            continue
    
    if not modelo_funcionou:
        print("❌ Nenhum modelo disponível funcionou.")
        exit(1)
    
    # Extrair JSON da resposta
    texto_resposta = response.text
    
    # Tentar encontrar o JSON na resposta
    inicio_json = texto_resposta.find('{')
    fim_json = texto_resposta.rfind('}') + 1
    
    if inicio_json >= 0 and fim_json > inicio_json:
        json_str = texto_resposta[inicio_json:fim_json]
        briefing = json.loads(json_str)
        
        # Exibir resultado
        print("="*70)
        print("📰 BRIEFING DE NOTÍCIAS")
        print("="*70)
        print(f"\n🎯 TÓPICO: {briefing.get('topico_central', topico)}\n")
        
        print("📋 ANÁLISE:")
        print("-"*70)
        print(briefing.get('analise_sintetizada', 'N/A'))
        
        print("\n\n📚 FONTES:")
        print("-"*70)
        artigos = briefing.get('artigos', [])
        for i, artigo in enumerate(artigos, 1):
            print(f"\n{i}. {artigo.get('titulo', 'N/A')}")
            print(f"   Fonte: {artigo.get('fonte', 'N/A')}")
            print(f"   {artigo.get('resumo_curto', 'N/A')}")
        
        print("\n\n🎨 PROMPT PARA IMAGEM:")
        print("-"*70)
        print(briefing.get('prompt_para_imagem', 'N/A'))
        
        print("\n" + "="*70)
        print("✅ Briefing gerado com sucesso!")
        print("="*70)
        
    else:
        print("⚠️  Resposta recebida, mas não em formato JSON:")
        print(texto_resposta[:500])
        
except Exception as e:
    print(f"❌ Erro ao gerar briefing: {e}")
    import traceback
    traceback.print_exc()
