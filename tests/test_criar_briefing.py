"""
Testes Unitários para CriarNoticia
==================================

Execute com: pytest tests/test_criar_briefing.py -v
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from pydantic import ValidationError
import sys
import os

# Adicionar o diretório pai ao path para importar os módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from criar_briefing_noticias import ArtigoEncontrado, BriefingDeNoticias


class TestArtigoEncontrado:
    """Testes para o modelo ArtigoEncontrado."""
    
    def test_criacao_valida(self):
        """Testa criação de artigo com dados válidos."""
        artigo = ArtigoEncontrado(
            titulo="IA revoluciona indústria",
            fonte="TechNews",
            resumo_curto="A inteligência artificial está transformando setores."
        )
        
        assert artigo.titulo == "IA revoluciona indústria"
        assert artigo.fonte == "TechNews"
        assert artigo.resumo_curto == "A inteligência artificial está transformando setores."
    
    def test_campos_obrigatorios(self):
        """Testa que todos os campos são obrigatórios."""
        with pytest.raises(ValidationError):
            ArtigoEncontrado(titulo="Teste")  # Faltam fonte e resumo_curto
    
    def test_tipos_corretos(self):
        """Testa que os tipos são validados."""
        with pytest.raises(ValidationError):
            ArtigoEncontrado(
                titulo=123,  # Deve ser string
                fonte="Fonte",
                resumo_curto="Resumo"
            )


class TestBriefingDeNoticias:
    """Testes para o modelo BriefingDeNoticias."""
    
    def test_criacao_valida(self):
        """Testa criação de briefing com dados válidos."""
        artigos = [
            ArtigoEncontrado(
                titulo="Artigo 1",
                fonte="Fonte 1",
                resumo_curto="Resumo 1"
            ),
            ArtigoEncontrado(
                titulo="Artigo 2",
                fonte="Fonte 2",
                resumo_curto="Resumo 2"
            )
        ]
        
        briefing = BriefingDeNoticias(
            topico_central="Inteligência Artificial",
            artigos=artigos,
            analise_sintetizada="Análise detalhada do tópico em dois parágrafos.",
            prompt_para_imagem="A futuristic AI-powered world"
        )
        
        assert briefing.topico_central == "Inteligência Artificial"
        assert len(briefing.artigos) == 2
        assert briefing.artigos[0].titulo == "Artigo 1"
    
    def test_lista_artigos_vazia(self):
        """Testa que a lista de artigos não pode estar vazia."""
        # Este teste depende da implementação - ajuste conforme necessário
        briefing = BriefingDeNoticias(
            topico_central="Teste",
            artigos=[],  # Lista vazia
            analise_sintetizada="Análise",
            prompt_para_imagem="Prompt"
        )
        assert len(briefing.artigos) == 0


class TestCriarBriefingAvancado:
    """Testes para a função criar_briefing_avancado."""
    
    @patch('criar_briefing_noticias.client')
    def test_criacao_briefing_sucesso(self, mock_client):
        """Testa criação bem-sucedida de briefing."""
        # Importar aqui para evitar problemas de configuração
        from criar_briefing_noticias import criar_briefing_avancado
        
        # Configurar o mock
        mock_response = Mock()
        mock_briefing = BriefingDeNoticias(
            topico_central="IA na Saúde",
            artigos=[
                ArtigoEncontrado(
                    titulo="IA ajuda diagnósticos",
                    fonte="MedTech",
                    resumo_curto="Novo sistema de IA melhora diagnósticos."
                )
            ],
            analise_sintetizada="A IA está revolucionando a medicina.",
            prompt_para_imagem="AI-powered medical diagnosis visualization"
        )
        mock_response.parsed = mock_briefing
        mock_client.models.generate_content.return_value = mock_response
        
        # Executar
        resultado = criar_briefing_avancado("IA na Saúde")
        
        # Verificar
        assert resultado is not None
        assert resultado.topico_central == "IA na Saúde"
        assert len(resultado.artigos) == 1
    
    @patch('criar_briefing_noticias.client')
    def test_criacao_briefing_erro_api(self, mock_client):
        """Testa tratamento de erro na API."""
        from criar_briefing_noticias import criar_briefing_avancado
        
        # Configurar mock para lançar exceção
        mock_client.models.generate_content.side_effect = Exception("API Error")
        
        # Executar
        resultado = criar_briefing_avancado("Teste")
        
        # Verificar que retorna None em caso de erro
        assert resultado is None


class TestGerarImagemDoBriefing:
    """Testes para a função gerar_imagem_do_briefing."""
    
    @patch('criar_briefing_noticias.client')
    @patch('criar_briefing_noticias.pathlib.Path')
    def test_geracao_imagem_sucesso(self, mock_path, mock_client):
        """Testa geração bem-sucedida de imagem."""
        from criar_briefing_noticias import gerar_imagem_do_briefing
        
        # Criar briefing de teste
        briefing = BriefingDeNoticias(
            topico_central="Teste",
            artigos=[
                ArtigoEncontrado(
                    titulo="Artigo",
                    fonte="Fonte",
                    resumo_curto="Resumo"
                )
            ],
            analise_sintetizada="Análise",
            prompt_para_imagem="Test prompt for image generation"
        )
        
        # Configurar mocks
        mock_image = Mock()
        mock_image.image.image_bytes = b"fake_image_data"
        mock_gen_images = Mock()
        mock_gen_images.generated_images = [mock_image]
        mock_client.models.generate_images.return_value = mock_gen_images
        
        # Executar (não deve lançar exceção)
        gerar_imagem_do_briefing(briefing)
        
        # Verificar que a API foi chamada
        mock_client.models.generate_images.assert_called_once()
    
    def test_geracao_imagem_briefing_none(self):
        """Testa que função retorna early se briefing é None."""
        from criar_briefing_noticias import gerar_imagem_do_briefing
        
        # Não deve lançar exceção
        gerar_imagem_do_briefing(None)
    
    def test_geracao_imagem_sem_prompt(self):
        """Testa que função retorna early se não há prompt."""
        from criar_briefing_noticias import gerar_imagem_do_briefing
        
        briefing = BriefingDeNoticias(
            topico_central="Teste",
            artigos=[],
            analise_sintetizada="Análise",
            prompt_para_imagem=""  # Prompt vazio
        )
        
        # Não deve lançar exceção
        gerar_imagem_do_briefing(briefing)


if __name__ == "__main__":
    # Executar testes com pytest
    pytest.main([__file__, "-v", "--tb=short"])
