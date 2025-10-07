#!/usr/bin/env python3
"""
CriarNoticia - Pipeline de Criação Automatizada de Conteúdo

Este script é o ponto de entrada principal para o pipeline que:
1. Busca notícias atuais sobre um tópico usando IA
2. Analisa e estrutura as informações em um briefing aprofundado (JSON)
3. Gera uma imagem de capa exclusiva
4. Cria um artigo completo pronto para publicação
"""

import argparse
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from pipeline import ContentPipeline


def main():
    """
    Função principal
    """
    parser = argparse.ArgumentParser(
        description='Pipeline de criação automatizada de conteúdo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  python main.py "Inteligência Artificial"
  python main.py "Mudanças Climáticas" --max-news 10
  python main.py "Tecnologia 5G" --output custom_output/
        '''
    )
    
    parser.add_argument(
        'topic',
        type=str,
        help='Tópico para criar o artigo'
    )
    
    parser.add_argument(
        '--max-news',
        type=int,
        default=5,
        help='Número máximo de notícias para buscar (padrão: 5)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='Diretório de saída (padrão: output/)'
    )
    
    args = parser.parse_args()
    
    try:
        # Inicializa o pipeline
        pipeline = ContentPipeline(output_dir=args.output)
        
        # Executa o pipeline
        result = pipeline.create_article(
            topic=args.topic,
            max_news=args.max_news
        )
        
        if result['success']:
            print("\n✅ Processo concluído com sucesso!")
            print(f"\n📁 Arquivos gerados:")
            print(f"   • {result['article_path']}")
            print(f"   • {result['briefing_path']}")
            print(f"   • {result['image_path']}")
            return 0
        else:
            print("\n❌ Erro ao processar o conteúdo")
            return 1
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Processo interrompido pelo usuário")
        return 130
    except Exception as e:
        print(f"\n❌ Erro: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
