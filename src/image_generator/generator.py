"""
Image Generator - Gera imagens de capa exclusivas
"""

import os
from typing import Dict, Optional
from datetime import datetime


class ImageGenerator:
    """
    Gera uma imagem de capa exclusiva para o conteúdo
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Inicializa o ImageGenerator
        
        Args:
            api_key: Chave de API para serviços de geração de imagem (opcional)
        """
        self.api_key = api_key or os.getenv("DALLE_API_KEY")
        
    def generate_cover_image(self, briefing: Dict, output_path: str) -> str:
        """
        Gera uma imagem de capa baseada no briefing
        
        Args:
            briefing: Briefing estruturado com informações do conteúdo
            output_path: Caminho para salvar a imagem
            
        Returns:
            Caminho da imagem gerada
        """
        topic = briefing.get("metadata", {}).get("topic", "Notícia")
        print(f"🎨 Gerando imagem de capa para: {topic}")
        
        # Cria uma descrição da imagem baseada no briefing
        image_description = self._create_image_description(briefing)
        
        # Em produção, isso usaria DALL-E, Midjourney, ou Stable Diffusion
        # Por enquanto, cria um placeholder SVG
        svg_content = self._create_placeholder_image(topic, image_description)
        
        # Garante que o diretório existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva a imagem
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✅ Imagem de capa salva em: {output_path}")
        return output_path
    
    def _create_image_description(self, briefing: Dict) -> str:
        """
        Cria uma descrição detalhada para geração da imagem
        
        Args:
            briefing: Briefing estruturado
            
        Returns:
            Descrição para a imagem
        """
        topic = briefing.get("metadata", {}).get("topic", "")
        summary = briefing.get("summary", "")
        
        description = (
            f"Imagem moderna e profissional sobre {topic}. "
            f"Estilo jornalístico, cores vibrantes, composição equilibrada. "
            f"Baseado em: {summary[:100]}..."
        )
        
        return description
    
    def _create_placeholder_image(self, topic: str, description: str) -> str:
        """
        Cria uma imagem SVG placeholder
        
        Args:
            topic: Tópico principal
            description: Descrição da imagem
            
        Returns:
            Conteúdo SVG
        """
        # Cores para gradiente
        colors = ["#4F46E5", "#7C3AED", "#EC4899"]
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{colors[0]};stop-opacity:1" />
      <stop offset="50%" style="stop-color:{colors[1]};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{colors[2]};stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="1200" height="630" fill="url(#grad)"/>
  
  <!-- Decorative elements -->
  <circle cx="100" cy="100" r="80" fill="white" opacity="0.1"/>
  <circle cx="1100" cy="530" r="100" fill="white" opacity="0.1"/>
  <rect x="900" y="50" width="150" height="150" fill="white" opacity="0.05" transform="rotate(45 975 125)"/>
  
  <!-- Title background -->
  <rect x="50" y="230" width="1100" height="170" fill="white" opacity="0.95" rx="10"/>
  
  <!-- Title -->
  <text x="600" y="310" font-family="Arial, sans-serif" font-size="48" font-weight="bold" 
        fill="#1F2937" text-anchor="middle">{self._escape_xml(topic)}</text>
  
  <!-- Subtitle -->
  <text x="600" y="360" font-family="Arial, sans-serif" font-size="24" 
        fill="#6B7280" text-anchor="middle">Notícia Automatizada</text>
  
  <!-- Footer -->
  <text x="600" y="580" font-family="Arial, sans-serif" font-size="18" 
        fill="white" text-anchor="middle" opacity="0.8">CriarNoticia.com</text>
</svg>'''
        
        return svg
    
    def _escape_xml(self, text: str) -> str:
        """
        Escapa caracteres especiais para XML
        """
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        text = text.replace('"', "&quot;")
        text = text.replace("'", "&apos;")
        return text
    
    def get_image_metadata(self, image_path: str) -> Dict:
        """
        Obtém metadados da imagem gerada
        
        Args:
            image_path: Caminho da imagem
            
        Returns:
            Metadados da imagem
        """
        return {
            "path": image_path,
            "format": "SVG",
            "dimensions": "1200x630",
            "generated_at": datetime.now().isoformat()
        }
