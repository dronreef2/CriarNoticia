"""
Pipeline Principal - Orquestra o processo de criação de conteúdo
"""

import os
import json
from typing import Dict, Optional
from datetime import datetime

from news_search import NewsSearcher
from briefing_analyzer import BriefingAnalyzer
from image_generator import ImageGenerator


class ContentPipeline:
    """
    Pipeline que automatiza a criação de conteúdo completo
    """
    
    def __init__(self, output_dir: str = "output"):
        """
        Inicializa o pipeline
        
        Args:
            output_dir: Diretório para salvar os arquivos gerados
        """
        self.output_dir = output_dir
        self.news_searcher = NewsSearcher()
        self.briefing_analyzer = BriefingAnalyzer()
        self.image_generator = ImageGenerator()
        
        # Garante que o diretório de saída existe
        os.makedirs(output_dir, exist_ok=True)
        
    def create_article(self, topic: str, max_news: int = 5) -> Dict:
        """
        Cria um artigo completo sobre um tópico
        
        Args:
            topic: Tópico para criar o artigo
            max_news: Número máximo de notícias para buscar
            
        Returns:
            Informações do artigo criado
        """
        print(f"\n{'='*60}")
        print(f"🚀 Iniciando pipeline de criação de conteúdo")
        print(f"📌 Tópico: {topic}")
        print(f"{'='*60}\n")
        
        # 1. Buscar notícias
        print("ETAPA 1: Busca de Notícias")
        print("-" * 60)
        news_items = self.news_searcher.search_news(topic, max_news)
        filtered_news = self.news_searcher.filter_relevant_news(news_items)
        
        # 2. Analisar e criar briefing
        print(f"\nETAPA 2: Análise e Estruturação")
        print("-" * 60)
        briefing = self.briefing_analyzer.analyze_news(filtered_news, topic)
        
        # 3. Salvar briefing
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        briefing_filename = f"briefing_{self._sanitize_filename(topic)}_{timestamp}.json"
        briefing_path = os.path.join(self.output_dir, briefing_filename)
        self.briefing_analyzer.save_briefing(briefing, briefing_path)
        
        # 4. Gerar imagem de capa
        print(f"\nETAPA 3: Geração de Imagem")
        print("-" * 60)
        image_filename = f"cover_{self._sanitize_filename(topic)}_{timestamp}.svg"
        image_path = os.path.join(self.output_dir, image_filename)
        self.image_generator.generate_cover_image(briefing, image_path)
        
        # 5. Criar artigo final
        print(f"\nETAPA 4: Criação do Artigo Final")
        print("-" * 60)
        article = self._create_final_article(briefing, image_path)
        article_filename = f"article_{self._sanitize_filename(topic)}_{timestamp}.json"
        article_path = os.path.join(self.output_dir, article_filename)
        
        with open(article_path, 'w', encoding='utf-8') as f:
            json.dump(article, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Artigo completo salvo em: {article_path}")
        
        # Resultado final
        result = {
            "success": True,
            "topic": topic,
            "article_path": article_path,
            "briefing_path": briefing_path,
            "image_path": image_path,
            "created_at": datetime.now().isoformat(),
            "statistics": {
                "news_found": len(news_items),
                "news_analyzed": len(filtered_news)
            }
        }
        
        print(f"\n{'='*60}")
        print(f"✨ Pipeline concluído com sucesso!")
        print(f"{'='*60}\n")
        
        self._print_summary(result)
        
        return result
    
    def _create_final_article(self, briefing: Dict, image_path: str) -> Dict:
        """
        Cria o artigo final combinando briefing e imagem
        
        Args:
            briefing: Briefing estruturado
            image_path: Caminho da imagem de capa
            
        Returns:
            Artigo completo estruturado
        """
        article = {
            "metadata": {
                "title": f"Artigo: {briefing['metadata']['topic']}",
                "created_at": datetime.now().isoformat(),
                "language": "pt-BR",
                "type": "automated_article",
                "version": "1.0"
            },
            "cover_image": {
                "path": image_path,
                "alt_text": f"Imagem de capa sobre {briefing['metadata']['topic']}"
            },
            "content": {
                "headline": briefing['metadata']['topic'],
                "summary": briefing['summary'],
                "key_points": briefing['key_points'],
                "detailed_content": briefing['detailed_analysis'],
                "sources_count": len(briefing['sources'])
            },
            "briefing": briefing,
            "publication_ready": True
        }
        
        return article
    
    def _sanitize_filename(self, text: str) -> str:
        """
        Sanitiza texto para usar em nomes de arquivo
        """
        # Remove caracteres especiais e substitui espaços
        safe_text = "".join(
            c if c.isalnum() or c in (' ', '-', '_') else '_' 
            for c in text
        )
        safe_text = safe_text.replace(' ', '_')
        return safe_text[:50]  # Limita tamanho
    
    def _print_summary(self, result: Dict):
        """
        Imprime um resumo dos resultados
        """
        print("📊 RESUMO:")
        print(f"   • Tópico: {result['topic']}")
        print(f"   • Notícias encontradas: {result['statistics']['news_found']}")
        print(f"   • Notícias analisadas: {result['statistics']['news_analyzed']}")
        print(f"   • Artigo: {result['article_path']}")
        print(f"   • Briefing: {result['briefing_path']}")
        print(f"   • Imagem: {result['image_path']}")
        print(f"   • Data: {result['created_at']}")
