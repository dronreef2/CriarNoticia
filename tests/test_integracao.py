"""
Testes de Integração para CriarNoticia
======================================

Testes end-to-end do pipeline completo.
"""

import pytest
import os
from unittest.mock import patch, Mock
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestIntegracaoCompleta:
    """Testes de integração do pipeline completo."""
    
    @patch('criar_briefing_noticias_v2.client')
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test-key'})
    def test_pipeline_completo_sucesso(self, mock_client):
        """Testa execução completa do pipeline com sucesso."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado, BriefingDeNoticias, ArtigoEncontrado
        
        # Mock da resposta da API
        mock_briefing = BriefingDeNoticias(
            topico_central="Inteligência Artificial",
            artigos=[
                ArtigoEncontrado(
                    titulo="IA revoluciona medicina",
                    fonte="TechNews",
                    resumo_curto="Novo algoritmo melhora diagnósticos."
                ),
                ArtigoEncontrado(
                    titulo="IA na educação",
                    fonte="EduTech",
                    resumo_curto="Plataformas adaptativas usam IA."
                ),
                ArtigoEncontrado(
                    titulo="Ética em IA",
                    fonte="Ethics Today",
                    resumo_curto="Debate sobre regulamentação de IA."
                )
            ],
            analise_sintetizada="A inteligência artificial está transformando diversos setores. Na medicina, algoritmos melhoram diagnósticos.",
            prompt_para_imagem="Futuristic AI technology visualization"
        )
        
        mock_response = Mock()
        mock_response.parsed = mock_briefing
        mock_client.models.generate_content.return_value = mock_response
        
        # Executar pipeline
        resultado = criar_briefing_avancado("Inteligência Artificial")
        
        # Verificações
        assert resultado is not None
        assert resultado.topico_central == "Inteligência Artificial"
        assert len(resultado.artigos) == 3
        assert all(isinstance(art.titulo, str) for art in resultado.artigos)
        assert len(resultado.analise_sintetizada) > 0
        assert len(resultado.prompt_para_imagem) > 0
    
    @patch('criar_briefing_noticias_v2.client')
    @patch('criar_briefing_noticias_v2.pathlib.Path')
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test-key'})
    def test_pipeline_com_geracao_imagem(self, mock_path, mock_client):
        """Testa pipeline incluindo geração de imagem."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado, gerar_imagem_do_briefing
        from criar_briefing_noticias_v2 import BriefingDeNoticias, ArtigoEncontrado
        
        # Mock do briefing
        mock_briefing = BriefingDeNoticias(
            topico_central="Teste",
            artigos=[
                ArtigoEncontrado(
                    titulo="Artigo Teste",
                    fonte="Fonte Teste",
                    resumo_curto="Resumo de teste"
                )
            ],
            analise_sintetizada="Análise de teste",
            prompt_para_imagem="Test image prompt"
        )
        
        mock_response = Mock()
        mock_response.parsed = mock_briefing
        mock_client.models.generate_content.return_value = mock_response
        
        # Mock da geração de imagem
        mock_image = Mock()
        mock_image.image.image_bytes = b"fake_image_data"
        mock_gen_images = Mock()
        mock_gen_images.generated_images = [mock_image]
        mock_client.models.generate_images.return_value = mock_gen_images
        
        # Executar
        briefing = criar_briefing_avancado("Teste")
        assert briefing is not None
        
        # Gerar imagem (não deve lançar exceção)
        gerar_imagem_do_briefing(briefing)
        
        # Verificar que a API de imagem foi chamada
        mock_client.models.generate_images.assert_called_once()


class TestValidacaoEntradaSaida:
    """Testes de validação de entrada e saída."""
    
    def test_topico_vazio(self):
        """Testa que tópico vazio lança exceção."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado
        
        with pytest.raises(ValueError, match="não pode estar vazio"):
            criar_briefing_avancado("")
    
    def test_topico_apenas_espacos(self):
        """Testa que tópico com apenas espaços lança exceção."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado
        
        with pytest.raises(ValueError, match="não pode estar vazio"):
            criar_briefing_avancado("   ")
    
    @patch('criar_briefing_noticias_v2.client')
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test-key'})
    def test_formato_saida_correto(self, mock_client):
        """Testa que a saída tem o formato esperado."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado, BriefingDeNoticias, ArtigoEncontrado
        
        mock_briefing = BriefingDeNoticias(
            topico_central="Teste",
            artigos=[
                ArtigoEncontrado(
                    titulo="T1",
                    fonte="F1",
                    resumo_curto="R1"
                )
            ],
            analise_sintetizada="Análise",
            prompt_para_imagem="Prompt"
        )
        
        mock_response = Mock()
        mock_response.parsed = mock_briefing
        mock_client.models.generate_content.return_value = mock_response
        
        resultado = criar_briefing_avancado("Teste")
        
        # Verificar estrutura
        assert hasattr(resultado, 'topico_central')
        assert hasattr(resultado, 'artigos')
        assert hasattr(resultado, 'analise_sintetizada')
        assert hasattr(resultado, 'prompt_para_imagem')
        
        # Verificar tipos
        assert isinstance(resultado.topico_central, str)
        assert isinstance(resultado.artigos, list)
        assert isinstance(resultado.analise_sintetizada, str)
        assert isinstance(resultado.prompt_para_imagem, str)


class TestTratamentoErros:
    """Testes de tratamento de erros."""
    
    @patch('criar_briefing_noticias_v2.client')
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test-key'})
    def test_erro_api_retorna_none(self, mock_client):
        """Testa que erro na API retorna None."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado
        
        mock_client.models.generate_content.side_effect = Exception("API Error")
        
        resultado = criar_briefing_avancado("Teste")
        assert resultado is None
    
    @patch('criar_briefing_noticias_v2.client')
    @patch.dict(os.environ, {'GOOGLE_API_KEY': 'test-key'})
    def test_erro_attribute_retorna_none(self, mock_client):
        """Testa que AttributeError é tratado corretamente."""
        from criar_briefing_noticias_v2 import criar_briefing_avancado
        
        mock_response = Mock()
        del mock_response.parsed  # Simular ausência do atributo
        mock_client.models.generate_content.return_value = mock_response
        
        resultado = criar_briefing_avancado("Teste")
        assert resultado is None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
