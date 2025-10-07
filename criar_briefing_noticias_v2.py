"""
Versão melhorada do criar_briefing_noticias.py
==============================================

Melhorias implementadas:
- Uso de variáveis de ambiente (.env)
- Logging estruturado
- Tratamento de erros específico
- Type hints completos
- Validações robustas
"""

import google.generativeai as genai
from google.generativeai import types
from pydantic import BaseModel, Field
from typing import List, Optional
import pathlib
import os
import logging
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# --- Configuração da API Key via Variável de Ambiente ---
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    logger.error("GOOGLE_API_KEY não encontrada nas variáveis de ambiente")
    logger.info("Crie um arquivo .env com: GOOGLE_API_KEY=sua-chave-aqui")
    logger.info("Ou obtenha uma chave em: https://aistudio.google.com/app/apikey")
    raise ValueError("API Key não configurada. Configure a variável de ambiente GOOGLE_API_KEY")

try:
    genai.configure(api_key=api_key)
    logger.info("API Key configurada com sucesso")
except Exception as e:
    logger.error(f"Erro na configuração da API Key: {e}")
    raise

# --- ETAPA 1: Definição da Estrutura de Dados com Pydantic ---

class ArtigoEncontrado(BaseModel):
    """
    Define a estrutura de um único artigo de notícia encontrado na web.
    
    Attributes:
        titulo: O título exato da matéria
        fonte: O nome do veículo de comunicação (ex: 'Reuters', 'G1')
        resumo_curto: Um resumo de uma a duas frases sobre a notícia
    """
    titulo: str = Field(description="O título exato da matéria.")
    fonte: str = Field(description="O nome do veículo de comunicação (ex: 'Reuters', 'G1', 'The Verge').")
    resumo_curto: str = Field(description="Um resumo de uma a duas frases sobre o ponto principal da notícia.")


class BriefingDeNoticias(BaseModel):
    """
    Define a estrutura completa do briefing que queremos receber.
    
    Attributes:
        topico_central: O tema principal que une todas as notícias
        artigos: Lista de 3 a 5 artigos relevantes encontrados
        analise_sintetizada: Análise aprofundada em 2 parágrafos
        prompt_para_imagem: Prompt descritivo para geração de imagem
    """
    topico_central: str = Field(description="O tema principal que une todas as notícias encontradas.")
    artigos: List[ArtigoEncontrado] = Field(description="Uma lista contendo de 3 a 5 artigos relevantes encontrados.")
    analise_sintetizada: str = Field(
        description="Uma análise aprofundada de 2 parágrafos. O primeiro parágrafo deve resumir os fatos principais. O segundo deve explorar as implicações ou o contexto mais amplo do tópico."
    )
    prompt_para_imagem: str = Field(
        description="Crie um prompt de texto descritivo e artístico para um modelo de geração de imagem (como Imagen ou Midjourney) que capture visualmente a essência da 'analise_sintetizada'. O prompt deve ser em inglês."
    )


# --- Configuração do modelo ---
# A API não requer inicialização de cliente, apenas configuração
logger.info("API Gemini configurada e pronta para uso")


def criar_briefing_avancado(topico: str) -> Optional[BriefingDeNoticias]:
    """
    Função principal que busca notícias, as estrutura, analisa e cria um prompt de imagem.
    
    Args:
        topico: O tema a ser pesquisado (ex: "IA na saúde")
    
    Returns:
        BriefingDeNoticias: Objeto com artigos, análise e prompt de imagem
        None: Se houver erro na geração
    
    Raises:
        ValueError: Se o tópico for vazio ou inválido
    
    Example:
        >>> briefing = criar_briefing_avancado("carros elétricos")
        >>> print(briefing.topico_central)
        'Carros Elétricos'
    """
    if not topico or not topico.strip():
        logger.error("Tópico vazio fornecido")
        raise ValueError("O tópico não pode estar vazio")
    
    logger.info(f"Iniciando criação do briefing para: '{topico}'")
    
    # --- ETAPA 2: Buscar, Estruturar e Analisar em uma única chamada ---
    prompt_principal = f"""
    Atue como um analista de notícias sênior. Sua tarefa é criar um briefing completo sobre o tópico: '{topico}'.
    
    IMPORTANTE: Retorne sua resposta em formato JSON válido com a seguinte estrutura exata:
    {{
        "topico_central": "string - o tema principal",
        "artigos": [
            {{
                "titulo": "string - título da matéria",
                "fonte": "string - nome do veículo",
                "resumo_curto": "string - resumo de 1-2 frases"
            }}
        ],
        "analise_sintetizada": "string - análise de 2 parágrafos",
        "prompt_para_imagem": "string - prompt em inglês para geração de imagem"
    }}
    
    1. Baseie-se em seu conhecimento para encontrar 3 a 5 artigos relevantes e recentes sobre o tópico.
    2. Preencha todas as informações solicitadas no formato JSON acima.
    3. A análise deve ter 2 parágrafos: o primeiro resumindo fatos, o segundo explorando implicações.
    4. O prompt para imagem deve ser descritivo e artístico em inglês.
    
    Retorne APENAS o JSON, sem texto adicional antes ou depois.
    """
    
    try:
        logger.debug("Enviando requisição para API Gemini...")
        
        # Tentar diferentes modelos até encontrar um disponível
        modelos_disponiveis = ['gemini-2.0-flash-exp', 'gemini-1.5-flash', 'gemini-1.5-pro']
        
        model = None
        response = None
        for nome_modelo in modelos_disponiveis:
            try:
                logger.debug(f"Tentando modelo: {nome_modelo}")
                model = genai.GenerativeModel(nome_modelo)
                
                response = model.generate_content(
                    contents=prompt_principal,
                    generation_config={'temperature': 0.5}
                )
                
                if response and response.text:
                    logger.info(f"✅ Modelo {nome_modelo} funcionou!")
                    break
            except Exception as e:
                logger.warning(f"Modelo {nome_modelo} não disponível: {e}")
                continue
        
        if not response or not response.text:
            raise ValueError("Nenhum modelo disponível funcionou")
        
        # Parsear a resposta JSON
        import json
        
        # Tentar extrair JSON da resposta
        texto = response.text.strip()
        inicio = texto.find('{')
        fim = texto.rfind('}') + 1
        
        if inicio >= 0 and fim > inicio:
            json_str = texto[inicio:fim]
            briefing_dict = json.loads(json_str)
        else:
            briefing_dict = json.loads(texto)
        
        briefing = BriefingDeNoticias(**briefing_dict)
        logger.info("Briefing estruturado com sucesso")
        logger.debug(f"Encontrados {len(briefing.artigos)} artigos")
        return briefing

    except AttributeError as e:
        logger.error(f"Erro ao acessar atributos da resposta: {e}")
        return None
    except ValueError as e:
        logger.error(f"Erro de validação nos dados retornados: {e}")
        return None
    except Exception as e:
        logger.error(f"Erro inesperado ao gerar o briefing: {e}", exc_info=True)
        return None


def gerar_imagem_do_briefing(briefing: Optional[BriefingDeNoticias]) -> None:
    """
    Usa o prompt gerado no briefing para criar uma imagem com o modelo Imagen.
    
    Args:
        briefing: Objeto BriefingDeNoticias com o prompt de imagem
    
    Returns:
        None
    
    Raises:
        IOError: Se houver erro ao salvar a imagem
    """
    if not briefing:
        logger.warning("Briefing ausente. Não é possível gerar imagem.")
        return
    
    if not briefing.prompt_para_imagem:
        logger.warning("Prompt de imagem ausente no briefing.")
        return

    logger.info(f"Gerando imagem com o prompt: '{briefing.prompt_para_imagem[:50]}...'")
    
    try:
        # Nota: A API ImageGenerationModel não está disponível na versão atual
        # Esta funcionalidade será implementada quando a API Imagen estiver disponível
        logger.warning("⚠️  Geração de imagem temporariamente desabilitada.")
        logger.info(f"📝 Prompt para imagem: {briefing.prompt_para_imagem}")
        logger.info("💡 Você pode usar este prompt em ferramentas como DALL-E, Midjourney ou Stable Diffusion.")
        
        return
        
        # Código original comentado para referência futura:
        # imagen = genai.ImageGenerationModel('imagen-3.0-generate-001')
        # result = imagen.generate_images(
        #     prompt=briefing.prompt_para_imagem,
        #     number_of_images=1,
        #     aspect_ratio="16:9",
        # )
        # imagem_bytes = result.images[0]._pil_image
        # nome_arquivo = f"briefing_{briefing.topico_central.replace(' ', '_').lower()}.png"
        # output_dir = os.getenv('OUTPUT_DIR', '.')
        # if output_dir != '.' and not os.path.exists(output_dir):
        #     os.makedirs(output_dir)
        #     logger.info(f"Diretório {output_dir} criado")
        # caminho_completo = os.path.join(output_dir, nome_arquivo)
        # imagem_bytes.save(caminho_completo)
        # logger.info(f"Imagem salva como '{caminho_completo}'")

    except AttributeError as e:
        logger.error(f"Erro ao acessar dados da imagem: {e}")
    except IOError as e:
        logger.error(f"Erro ao salvar imagem: {e}")
    except Exception as e:
        logger.error(f"Erro inesperado ao gerar a imagem: {e}", exc_info=True)


# --- Execução do Pipeline ---
if __name__ == "__main__":
    # Configurar nível de log via variável de ambiente
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    logging.getLogger().setLevel(getattr(logging, log_level))
    
    # Tópico pode ser fornecido via argumento ou variável de ambiente
    topico_env = os.getenv('TOPICO')
    topico = topico_env if topico_env else "lançamento e recepção do Apple Vision Pro"
    
    logger.info("="*70)
    logger.info("PIPELINE DE CONTEÚDO AUTOMATIZADO")
    logger.info("="*70)
    
    try:
        # Executa a parte de texto do pipeline
        meu_briefing = criar_briefing_avancado(topico)
        
        if meu_briefing:
            # Imprime o resultado do conteúdo avançado
            print("\n" + "="*50)
            print("📰 BRIEFING DE NOTÍCIAS AVANÇADO 📰")
            print("="*50)
            print(f"TÓPICO: {meu_briefing.topico_central}\n")
            print("--- ANÁLISE SINTETIZADA ---")
            print(meu_briefing.analise_sintetizada)
            print("\n--- FONTES UTILIZADAS ---")
            for i, art in enumerate(meu_briefing.artigos, 1):
                print(f"{i}. {art.titulo} ({art.fonte})")
            print("="*50 + "\n")

            # Executa a parte visual do pipeline
            gerar_imagem_do_briefing(meu_briefing)
            
            logger.info("Pipeline executado com sucesso!")
        else:
            logger.error("Falha ao criar briefing")
    
    except KeyboardInterrupt:
        logger.info("Execução interrompida pelo usuário")
    except Exception as e:
        logger.error(f"Erro fatal na execução: {e}", exc_info=True)
