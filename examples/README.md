# Exemplos de Uso do CriarNoticia

Este diretório contém exemplos de como usar o pipeline de criação automatizada de conteúdo.

## Exemplo 1: Artigo Simples

```bash
python main.py "Inteligência Artificial"
```

Este comando cria um artigo completo sobre Inteligência Artificial usando as configurações padrão (5 notícias).

**Saída:**
- `output/article_Inteligência_Artificial_[timestamp].json`
- `output/briefing_Inteligência_Artificial_[timestamp].json`
- `output/cover_Inteligência_Artificial_[timestamp].svg`

## Exemplo 2: Artigo com Mais Fontes

```bash
python main.py "Mudanças Climáticas" --max-news 10
```

Este comando busca até 10 notícias sobre Mudanças Climáticas para criar um artigo mais aprofundado.

## Exemplo 3: Diretório de Saída Customizado

```bash
python main.py "Tecnologia 5G" --output custom_output/
```

Este comando salva os arquivos gerados em um diretório customizado.

## Exemplo 4: Script Python

Você também pode usar o pipeline diretamente no seu código Python:

```python
#!/usr/bin/env python3
import sys
sys.path.insert(0, 'src')

from pipeline import ContentPipeline

# Cria uma instância do pipeline
pipeline = ContentPipeline(output_dir='meus_artigos')

# Cria um artigo
result = pipeline.create_article(
    topic="Robótica Avançada",
    max_news=8
)

# Verifica o resultado
if result['success']:
    print(f"Artigo criado: {result['article_path']}")
    print(f"Imagem gerada: {result['image_path']}")
```

## Exemplo 5: Múltiplos Artigos

```bash
# Cria vários artigos sobre diferentes tópicos
python main.py "Inteligência Artificial" --output artigos_ia/
python main.py "Blockchain" --output artigos_blockchain/
python main.py "Computação Quântica" --output artigos_quantica/
```

## Exemplo 6: Integração com APIs Reais

Para usar APIs reais, configure o arquivo `.env`:

```bash
# Copie o exemplo
cp .env.example .env

# Edite e adicione suas chaves
nano .env
```

Adicione suas chaves:
```
OPENAI_API_KEY=sk-...
NEWS_API_KEY=...
DALLE_API_KEY=...
```

Então execute:
```bash
python main.py "Últimas Novidades em IA" --max-news 15
```

## Estrutura dos Arquivos Gerados

### Artigo (article_*.json)

```json
{
  "metadata": {
    "title": "Artigo: [Tópico]",
    "created_at": "2024-01-15T10:30:00",
    "language": "pt-BR",
    "type": "automated_article"
  },
  "cover_image": {
    "path": "output/cover_*.svg",
    "alt_text": "Imagem de capa sobre [Tópico]"
  },
  "content": {
    "headline": "[Tópico]",
    "summary": "Análise aprofundada...",
    "key_points": [...],
    "detailed_content": {...}
  }
}
```

### Briefing (briefing_*.json)

Contém análise detalhada, fontes, estatísticas e recomendações.

### Imagem (cover_*.svg)

Imagem de capa em formato SVG com design moderno e profissional.

## Dicas

1. **Use tópicos específicos** para melhores resultados
2. **Ajuste max-news** baseado na profundidade desejada
3. **Organize por diretórios** usando o parâmetro `--output`
4. **Revise os arquivos JSON** antes de publicar
5. **Personalize a imagem SVG** se necessário

## Ajuda

Para ver todas as opções disponíveis:

```bash
python main.py --help
```
