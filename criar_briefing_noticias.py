import google.generativeai as genai
from google.generativeai import types
from pydantic import BaseModel, Field
from typing import List
import pathlib

# --- Configuração da API Key ---
# Lembre-se de substituir "SUA_API_KEY_AQUI" pela sua chave real.
# Em projetos sérios, use variáveis de ambiente ou gerenciadores de segredos.
try:
    genai.configure(api_key="SUA_API_KEY_AQUI")
except Exception as e:
    print(f"Erro na configuração da API Key: {e}. Certifique-se de que a chave está correta.")
    exit()

# --- ETAPA 1: Definição da Estrutura de Dados com Pydantic ---
# O modelo será forçado a preencher essa estrutura, garantindo um JSON limpo.

class ArtigoEncontrado(BaseModel):
    """Define a estrutura de um único artigo de notícia encontrado na web."""
    titulo: str = Field(description="O título exato da matéria.")
    fonte: str = Field(description="O nome do veículo de comunicação (ex: 'Reuters', 'G1', 'The Verge').")
    resumo_curto: str = Field(description="Um resumo de uma a duas frases sobre o ponto principal da notícia.")

class BriefingDeNoticias(BaseModel):
    """Define a estrutura completa do briefing que queremos receber."""
    topico_central: str = Field(description="O tema principal que une todas as notícias encontradas.")
    artigos: List[ArtigoEncontrado] = Field(description="Uma lista contendo de 3 a 5 artigos relevantes encontrados.")
    analise_sintetizada: str = Field(
        description="Uma análise aprofundada de 2 parágrafos. O primeiro parágrafo deve resumir os fatos principais. O segundo deve explorar as implicações ou o contexto mais amplo do tópico."
    )
    prompt_para_imagem: str = Field(
        description="Crie um prompt de texto descritivo e artístico para um modelo de geração de imagem (como Imagen ou Midjourney) que capture visualmente a essência da 'analise_sintetizada'. O prompt deve ser em inglês."
    )

# --- Inicialização do Cliente (novo padrão) ---
client = genai.Client()

def criar_briefing_avancado(topico: str):
    """
    Função principal que busca notícias, as estrutura, analisa e cria um prompt de imagem.
    """
    print(f"🚀 Iniciando a criação do briefing para: '{topico}'")
    
    # --- ETAPA 2: Buscar, Estruturar e Analisar em uma única chamada ---
    prompt_principal = f"""
    Atue como um analista de notícias sênior. Sua tarefa é criar um briefing completo sobre o tópico: '{topico}'.
    1.  Use a ferramenta de busca para encontrar as notícias mais recentes e relevantes.
    2.  Selecione os 3 a 5 artigos mais importantes.
    3.  Preencha todas as informações solicitadas no formato JSON, incluindo uma análise aprofundada e um prompt criativo para gerar uma imagem.
    """
    
    try:
        print("🔎 Buscando e analisando notícias...")
        response = client.models.generate_content(
            model='gemini-1.5-pro-latest',
            contents=prompt_principal,
            # Habilitando a busca na web (novo padrão)
            tools=[types.Tool(google_search=types.GoogleSearch())],
            generation_config=types.GenerateContentConfig(
                # Forçando a saída em JSON com o schema Pydantic (novo padrão)
                response_mime_type='application/json',
                response_schema=BriefingDeNoticias,
                temperature=0.5 # Um pouco de criatividade na análise
            )
        )
        
        # O novo SDK já faz o parse do JSON para um objeto Pydantic
        briefing = response.parsed
        print("✅ Briefing estruturado com sucesso!")
        return briefing

    except Exception as e:
        print(f"❌ Erro ao gerar o briefing: {e}")
        # A resposta pode conter informações úteis para depuração
        # print("Resposta Bruta:", response.text)
        return None

# --- ETAPA 3: Gerar a Imagem ---
def gerar_imagem_do_briefing(briefing: BriefingDeNoticias):
    """
    Usa o prompt gerado no briefing para criar uma imagem com o modelo Imagen.
    """
    if not briefing or not briefing.prompt_para_imagem:
        print("⚠️ Briefing ou prompt de imagem ausente. Não é possível gerar imagem.")
        return

    print(f"🎨 Gerando imagem com o prompt: '{briefing.prompt_para_imagem}'...")
    
    try:
        gen_images = client.models.generate_images(
            model='imagen-3.0-generate-001', # Usando o modelo mais recente
            prompt=briefing.prompt_para_imagem,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9", # Ótimo para blogs e redes sociais
            )
        )
        
        # Salvando a imagem
        imagem_bytes = gen_images.generated_images[0].image.image_bytes
        nome_arquivo = f"briefing_{briefing.topico_central.replace(' ', '_').lower()}.png"
        pathlib.Path(nome_arquivo).write_bytes(imagem_bytes)
        print(f"✅ Imagem salva como '{nome_arquivo}'")

    except Exception as e:
        print(f"❌ Erro ao gerar a imagem: {e}")

# --- Execução do Pipeline ---
if __name__ == "__main__":
    # tópico = "o impacto da inteligência artificial na indústria de games"
    tópico = "lançamento e recepção do Apple Vision Pro"
    
    # Executa a parte de texto do pipeline
    meu_briefing = criar_briefing_avancado(tópico)
    
    if meu_briefing:
        # Imprime o resultado do conteúdo avançado
        print("\n" + "="*50)
        print("📰 BRIEFING DE NOTÍCIAS AVANÇADO 📰")
        print("="*50)
        print(f"TÓPICO: {meu_briefing.topico_central}\n")
        print("--- ANÁLISE SINTETIZADA ---")
        print(meu_briefing.analise_sintetizada)
        print("\n--- FONTES UTILIZADAS ---")
        for art in meu_briefing.artigos:
            print(f"- {art.titulo} ({art.fonte})")
        print("="*50 + "\n")

        # Executa a parte visual do pipeline
        gerar_imagem_do_briefing(meu_briefing)
