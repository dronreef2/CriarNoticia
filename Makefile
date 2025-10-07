# CriarNoticia - Makefile

.PHONY: help install test test-cov clean run setup format lint docs

help:
	@echo "CriarNoticia - Comandos Disponíveis"
	@echo "===================================="
	@echo ""
	@echo "  make install    - Instalar dependências"
	@echo "  make setup      - Configurar ambiente"
	@echo "  make test       - Executar testes"
	@echo "  make test-cov   - Testes com cobertura"
	@echo "  make run        - Executar projeto"
	@echo "  make format     - Formatar código"
	@echo "  make lint       - Verificar qualidade"
	@echo "  make clean      - Limpar arquivos temporários"
	@echo "  make docs       - Ver documentação"
	@echo ""

install:
	@echo "📦 Instalando dependências..."
	pip install -r requirements.txt
	pip install pytest pytest-cov pylint black
	@echo "✅ Dependências instaladas!"

setup:
	@echo "⚙️  Configurando ambiente..."
	python setup.py
	@echo "✅ Setup concluído!"

test:
	@echo "🧪 Executando testes..."
	pytest tests/ -v
	@echo "✅ Testes concluídos!"

test-cov:
	@echo "🧪 Executando testes com cobertura..."
	pytest tests/ -v --cov=. --cov-report=html --cov-report=term
	@echo "✅ Relatório de cobertura gerado em htmlcov/index.html"

run:
	@echo "🚀 Executando projeto..."
	python criar_briefing_noticias_v2.py
	@echo "✅ Execução concluída!"

format:
	@echo "🎨 Formatando código..."
	black *.py tests/*.py
	@echo "✅ Código formatado!"

lint:
	@echo "🔍 Verificando qualidade do código..."
	pylint criar_briefing_noticias_v2.py --exit-zero
	@echo "✅ Verificação concluída!"

clean:
	@echo "🧹 Limpando arquivos temporários..."
	rm -rf __pycache__ tests/__pycache__ .pytest_cache
	rm -rf htmlcov .coverage
	rm -rf *.pyc tests/*.pyc
	rm -rf output/*.png
	@echo "✅ Limpeza concluída!"

docs:
	@echo "📚 Documentação disponível:"
	@echo "  - START_HERE.md          (ponto de entrada)"
	@echo "  - README.md              (documentação técnica)"
	@echo "  - QUICKSTART.md          (guia rápido)"
	@echo "  - RELATORIO_FINAL.md     (resumo executivo)"
	@echo "  - ANALISE_PROJETO.md     (análise técnica)"
	@echo "  - PLANO_IMPLEMENTACAO.md (plano de ação)"
	@echo "  - CONTRIBUTING.md        (guia de contribuição)"
	@echo "  - CHANGELOG.md           (histórico de mudanças)"

all: install setup test run
	@echo "🎉 Todas as tarefas concluídas!"
