"""
Briefing Analyzer - Analisa e estrutura informações em briefing JSON
"""

import json
from typing import List, Dict, Optional
from datetime import datetime


class BriefingAnalyzer:
    """
    Analisa notícias e estrutura as informações em um briefing aprofundado com formato JSON
    """
    
    def __init__(self):
        """
        Inicializa o BriefingAnalyzer
        """
        self.briefing_version = "1.0"
        
    def analyze_news(self, news_items: List[Dict], topic: str) -> Dict:
        """
        Analisa notícias e cria um briefing estruturado
        
        Args:
            news_items: Lista de notícias para analisar
            topic: Tópico principal
            
        Returns:
            Briefing estruturado em formato JSON
        """
        print(f"📝 Analisando {len(news_items)} notícias sobre: {topic}")
        
        # Extrai informações chave
        key_points = self._extract_key_points(news_items)
        summary = self._generate_summary(news_items, topic)
        sources = self._extract_sources(news_items)
        
        # Estrutura o briefing
        briefing = {
            "metadata": {
                "version": self.briefing_version,
                "topic": topic,
                "created_at": datetime.now().isoformat(),
                "total_sources": len(news_items),
                "language": "pt-BR"
            },
            "summary": summary,
            "key_points": key_points,
            "detailed_analysis": self._create_detailed_analysis(news_items),
            "sources": sources,
            "recommendations": self._generate_recommendations(news_items, topic),
            "statistics": {
                "total_articles": len(news_items),
                "average_relevance": self._calculate_average_relevance(news_items),
                "date_range": self._get_date_range(news_items)
            }
        }
        
        print("✅ Briefing estruturado criado com sucesso")
        return briefing
    
    def _extract_key_points(self, news_items: List[Dict]) -> List[str]:
        """
        Extrai pontos-chave das notícias
        """
        key_points = []
        for item in news_items[:5]:  # Top 5 notícias
            point = f"{item['title']} - {item['description'][:100]}..."
            key_points.append(point)
        return key_points
    
    def _generate_summary(self, news_items: List[Dict], topic: str) -> str:
        """
        Gera um resumo executivo
        """
        return (f"Análise aprofundada sobre {topic} baseada em {len(news_items)} "
                f"fontes. Os principais desenvolvimentos incluem tendências atuais, "
                f"análises de especialistas e dados relevantes do setor.")
    
    def _extract_sources(self, news_items: List[Dict]) -> List[Dict]:
        """
        Extrai e organiza as fontes
        """
        sources = []
        for item in news_items:
            source = {
                "title": item["title"],
                "source": item["source"],
                "url": item["url"],
                "date": item["published_date"],
                "relevance": item.get("relevance_score", 0)
            }
            sources.append(source)
        return sources
    
    def _create_detailed_analysis(self, news_items: List[Dict]) -> Dict:
        """
        Cria análise detalhada por categoria
        """
        return {
            "trends": "Análise das tendências identificadas nas notícias",
            "insights": "Principais insights extraídos do conteúdo",
            "context": "Contexto histórico e relevância atual",
            "impact": "Impacto potencial e implicações"
        }
    
    def _generate_recommendations(self, news_items: List[Dict], topic: str) -> List[str]:
        """
        Gera recomendações baseadas na análise
        """
        return [
            f"Acompanhar desenvolvimentos contínuos sobre {topic}",
            "Consultar fontes adicionais para aprofundamento",
            "Avaliar impacto no contexto específico de interesse"
        ]
    
    def _calculate_average_relevance(self, news_items: List[Dict]) -> float:
        """
        Calcula relevância média
        """
        if not news_items:
            return 0.0
        total = sum(item.get("relevance_score", 0) for item in news_items)
        return round(total / len(news_items), 2)
    
    def _get_date_range(self, news_items: List[Dict]) -> Dict:
        """
        Obtém intervalo de datas
        """
        if not news_items:
            return {"from": None, "to": None}
        
        dates = [item["published_date"] for item in news_items]
        return {
            "from": min(dates),
            "to": max(dates)
        }
    
    def save_briefing(self, briefing: Dict, output_path: str) -> str:
        """
        Salva o briefing em arquivo JSON
        
        Args:
            briefing: Briefing estruturado
            output_path: Caminho do arquivo de saída
            
        Returns:
            Caminho do arquivo salvo
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(briefing, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Briefing salvo em: {output_path}")
        return output_path
