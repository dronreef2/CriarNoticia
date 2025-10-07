#!/usr/bin/env python3
"""
Exemplo de uso programático do CriarNoticia
"""

import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pipeline import ContentPipeline


def main():
    """
    Demonstra como usar o pipeline programaticamente
    """
    print("=== Exemplo de Uso Programático do CriarNoticia ===\n")
    
    # Cria uma instância do pipeline
    pipeline = ContentPipeline(output_dir='examples/output')
    
    # Lista de tópicos para criar artigos
    topics = [
        "Inteligência Artificial",
        "Blockchain",
        "Energia Renovável"
    ]
    
    results = []
    
    # Cria um artigo para cada tópico
    for topic in topics:
        print(f"\n{'='*60}")
        print(f"Processando: {topic}")
        print(f"{'='*60}\n")
        
        result = pipeline.create_article(
            topic=topic,
            max_news=5
        )
        
        results.append(result)
    
    # Resumo final
    print("\n\n" + "="*60)
    print("RESUMO FINAL")
    print("="*60)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['topic']}")
        print(f"   Status: {'✅ Sucesso' if result['success'] else '❌ Falha'}")
        print(f"   Artigo: {result['article_path']}")
        print(f"   Notícias analisadas: {result['statistics']['news_analyzed']}")
    
    print("\n" + "="*60)
    print(f"Total de artigos criados: {len(results)}")
    print("="*60)


if __name__ == "__main__":
    main()
