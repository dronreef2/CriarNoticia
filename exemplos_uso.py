"""
Exemplos de Uso do Pipeline de Conteúdo Automatizado
=====================================================

Este arquivo contém exemplos de como personalizar e utilizar o pipeline
para diferentes casos de uso.
"""

import os
from criar_briefing_noticias import criar_briefing_avancado, gerar_imagem_do_briefing

# ============================================================================
# EXEMPLO 1: Configurando a API Key via Variável de Ambiente (Recomendado)
# ============================================================================
# Ao invés de colocar a chave diretamente no código, use variáveis de ambiente:
#
# No Linux/Mac:
#   export GOOGLE_API_KEY="sua-chave-aqui"
#
# No Windows (PowerShell):
#   $env:GOOGLE_API_KEY="sua-chave-aqui"
#
# No código:
#   import google.generativeai as genai
#   genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


# ============================================================================
# EXEMPLO 2: Análise de Múltiplos Tópicos
# ============================================================================
def analisar_multiplos_topicos():
    """
    Cria briefings para vários tópicos de interesse.
    """
    topicos = [
        "impacto da inteligência artificial na saúde",
        "sustentabilidade e energia renovável",
        "avanços em computação quântica",
        "tendências em cibersegurança 2024"
    ]
    
    briefings = []
    for topico in topicos:
        print(f"\n{'='*60}")
        print(f"Processando: {topico}")
        print('='*60)
        
        briefing = criar_briefing_avancado(topico)
        if briefing:
            briefings.append(briefing)
            # Opcionalmente, gerar imagem para cada um
            # gerar_imagem_do_briefing(briefing)
    
    return briefings


# ============================================================================
# EXEMPLO 3: Salvando Resultado em Arquivo
# ============================================================================
def salvar_briefing_em_arquivo(briefing, formato='txt'):
    """
    Salva o briefing gerado em um arquivo de texto ou JSON.
    """
    import json
    from datetime import datetime
    
    if not briefing:
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_base = f"briefing_{timestamp}"
    
    if formato == 'txt':
        # Salvar como texto formatado
        with open(f"{nome_base}.txt", 'w', encoding='utf-8') as f:
            f.write("="*70 + "\n")
            f.write("BRIEFING DE NOTÍCIAS AVANÇADO\n")
            f.write("="*70 + "\n\n")
            f.write(f"TÓPICO: {briefing.topico_central}\n\n")
            f.write("ANÁLISE SINTETIZADA\n")
            f.write("-"*70 + "\n")
            f.write(briefing.analise_sintetizada + "\n\n")
            f.write("FONTES UTILIZADAS\n")
            f.write("-"*70 + "\n")
            for i, art in enumerate(briefing.artigos, 1):
                f.write(f"{i}. {art.titulo}\n")
                f.write(f"   Fonte: {art.fonte}\n")
                f.write(f"   Resumo: {art.resumo_curto}\n\n")
        print(f"✅ Briefing salvo em: {nome_base}.txt")
    
    elif formato == 'json':
        # Salvar como JSON
        with open(f"{nome_base}.json", 'w', encoding='utf-8') as f:
            json.dump(briefing.model_dump(), f, ensure_ascii=False, indent=2)
        print(f"✅ Briefing salvo em: {nome_base}.json")


# ============================================================================
# EXEMPLO 4: Pipeline Completo com Tratamento de Erros
# ============================================================================
def pipeline_robusto(topico: str):
    """
    Executa o pipeline completo com tratamento de erros adequado.
    """
    import time
    
    tentativas_maximas = 3
    
    for tentativa in range(1, tentativas_maximas + 1):
        try:
            print(f"\n🔄 Tentativa {tentativa}/{tentativas_maximas}")
            
            # Criar briefing
            briefing = criar_briefing_avancado(topico)
            
            if not briefing:
                raise Exception("Falha ao criar briefing")
            
            # Exibir resultado
            print("\n" + "="*70)
            print("📰 BRIEFING GERADO COM SUCESSO")
            print("="*70)
            print(f"Tópico: {briefing.topico_central}")
            print(f"Artigos encontrados: {len(briefing.artigos)}")
            print(f"Tamanho da análise: {len(briefing.analise_sintetizada)} caracteres")
            
            # Salvar em arquivo
            salvar_briefing_em_arquivo(briefing, formato='txt')
            salvar_briefing_em_arquivo(briefing, formato='json')
            
            # Gerar imagem
            gerar_imagem_do_briefing(briefing)
            
            print("\n✅ Pipeline executado com sucesso!")
            return briefing
            
        except Exception as e:
            print(f"❌ Erro na tentativa {tentativa}: {e}")
            if tentativa < tentativas_maximas:
                tempo_espera = 5 * tentativa
                print(f"⏳ Aguardando {tempo_espera} segundos antes de tentar novamente...")
                time.sleep(tempo_espera)
            else:
                print("❌ Todas as tentativas falharam")
                return None


# ============================================================================
# EXEMPLO 5: Análise Comparativa
# ============================================================================
def analise_comparativa(topico1: str, topico2: str):
    """
    Cria briefings para dois tópicos relacionados e os compara.
    """
    print(f"📊 Iniciando análise comparativa")
    print(f"   Tópico 1: {topico1}")
    print(f"   Tópico 2: {topico2}")
    
    briefing1 = criar_briefing_avancado(topico1)
    briefing2 = criar_briefing_avancado(topico2)
    
    if briefing1 and briefing2:
        print("\n" + "="*70)
        print("COMPARAÇÃO DE TÓPICOS")
        print("="*70)
        print(f"\nTópico 1: {briefing1.topico_central}")
        print(f"   Artigos: {len(briefing1.artigos)}")
        print(f"\nTópico 2: {briefing2.topico_central}")
        print(f"   Artigos: {len(briefing2.artigos)}")
        
        # Você pode adicionar lógica adicional de comparação aqui
        return briefing1, briefing2
    
    return None, None


# ============================================================================
# EXEMPLO 6: Filtrar por Data
# ============================================================================
def criar_briefing_com_filtro_temporal(topico: str, periodo: str = "última semana"):
    """
    Cria um briefing focando em notícias de um período específico.
    """
    prompt_customizado = f"""
    Atue como um analista de notícias sênior. Sua tarefa é criar um briefing completo sobre o tópico: '{topico}'.
    
    IMPORTANTE: Foque especialmente em notícias da {periodo}.
    
    1. Use a ferramenta de busca para encontrar as notícias mais recentes.
    2. Selecione os 3 a 5 artigos mais importantes do período especificado.
    3. Preencha todas as informações solicitadas no formato JSON, incluindo uma análise aprofundada.
    """
    
    # Nota: Você precisaria modificar a função criar_briefing_avancado para aceitar
    # um prompt customizado como parâmetro
    print(f"💡 Para implementar filtros temporais, customize o prompt no arquivo principal")


# ============================================================================
# EXEMPLO DE EXECUÇÃO
# ============================================================================
if __name__ == "__main__":
    # Descomente o exemplo que deseja executar:
    
    # Exemplo 2: Múltiplos tópicos
    # analisar_multiplos_topicos()
    
    # Exemplo 4: Pipeline robusto
    # pipeline_robusto("tendências em inteligência artificial 2024")
    
    # Exemplo 5: Análise comparativa
    # analise_comparativa(
    #     "energia solar no Brasil",
    #     "energia eólica no Brasil"
    # )
    
    print("\n" + "="*70)
    print("EXEMPLOS DE USO")
    print("="*70)
    print("\nEste arquivo contém vários exemplos de como usar o pipeline.")
    print("Descomente os exemplos no código para executá-los.")
    print("\nDicas:")
    print("1. Configure a API key via variável de ambiente")
    print("2. Use pipeline_robusto() para maior confiabilidade")
    print("3. Salve os resultados em arquivos para análise posterior")
    print("4. Customize os prompts para casos de uso específicos")
    print("="*70)
