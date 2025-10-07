# CriarNoticia 📰

**Pipeline de Criação Automatizada de Conteúdo**

Um sistema completo que automatiza a criação de artigos jornalísticos, desde a busca de notícias até a publicação final com imagens de capa exclusivas.

## 📋 Descrição

O **CriarNoticia** é um pipeline inteligente que:

1. 🔍 **Busca notícias atuais** sobre um tópico usando IA
2. 📝 **Analisa e estrutura** as informações em um briefing aprofundado com formato JSON
3. 🎨 **Gera uma imagem de capa** exclusiva para o conteúdo
4. ✨ **Cria um artigo completo** e visualmente atraente, pronto para ser publicado

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/dronreef2/CriarNoticia.git
cd CriarNoticia
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. (Opcional) Configure as chaves de API:
```bash
cp .env.example .env
# Edite o arquivo .env com suas chaves de API
```

### Uso Básico

Execute o pipeline com um tópico:

```bash
python main.py "Inteligência Artificial"
```

Com opções personalizadas:

```bash
python main.py "Mudanças Climáticas" --max-news 10 --output meus_artigos/
```

### Parâmetros

- `topic` (obrigatório): Tópico para criar o artigo
- `--max-news`: Número máximo de notícias para buscar (padrão: 5)
- `--output`: Diretório de saída (padrão: output/)

## 📁 Estrutura do Projeto

```
CriarNoticia/
├── src/
│   ├── news_search/        # Módulo de busca de notícias
│   │   ├── __init__.py
│   │   └── search.py
│   ├── briefing_analyzer/  # Módulo de análise e estruturação
│   │   ├── __init__.py
│   │   └── analyzer.py
│   ├── image_generator/    # Módulo de geração de imagens
│   │   ├── __init__.py
│   │   └── generator.py
│   ├── __init__.py
│   └── pipeline.py         # Orquestrador principal
├── output/                 # Artigos e arquivos gerados
├── examples/               # Exemplos de uso
├── main.py                 # Script principal
├── requirements.txt        # Dependências Python
├── .env.example           # Exemplo de configuração
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Este arquivo
```

## 🔄 Fluxo do Pipeline

```
┌─────────────────┐
│  1. Busca de    │
│     Notícias    │──┐
└─────────────────┘  │
                     │
┌─────────────────┐  │
│  2. Análise e   │  │
│   Estruturação  │◄─┘
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  3. Geração de  │
│     Imagem      │
└─────────────────┘
        │
        ▼
┌─────────────────┐
│  4. Artigo      │
│     Final       │
└─────────────────┘
```

## 📦 Saída do Pipeline

Para cada execução, o pipeline gera 3 arquivos no diretório de saída:

1. **briefing_[topic]_[timestamp].json**: Briefing estruturado com análise detalhada
2. **cover_[topic]_[timestamp].svg**: Imagem de capa exclusiva
3. **article_[topic]_[timestamp].json**: Artigo completo pronto para publicação

### Exemplo de Estrutura do Artigo

```json
{
  "metadata": {
    "title": "Artigo: Inteligência Artificial",
    "created_at": "2024-01-15T10:30:00",
    "language": "pt-BR",
    "type": "automated_article"
  },
  "cover_image": {
    "path": "output/cover_Inteligencia_Artificial_20240115_103000.svg",
    "alt_text": "Imagem de capa sobre Inteligência Artificial"
  },
  "content": {
    "headline": "Inteligência Artificial",
    "summary": "Análise aprofundada...",
    "key_points": [...],
    "detailed_content": {...}
  },
  "briefing": {...}
}
```

## 🎨 Exemplos

### Exemplo 1: Artigo sobre Tecnologia

```bash
python main.py "Avanços em Inteligência Artificial" --max-news 8
```

### Exemplo 2: Artigo sobre Ciência

```bash
python main.py "Descobertas Espaciais" --output artigos_ciencia/
```

### Exemplo 3: Artigo sobre Negócios

```bash
python main.py "Tendências de Mercado 2024" --max-news 10
```

## 🔧 Configuração Avançada

### Usando APIs Reais

O sistema suporta integração com APIs reais para busca de notícias e geração de imagens:

1. **OpenAI API**: Para busca avançada e análise de notícias
2. **News API**: Para busca de notícias de fontes reais
3. **DALL-E**: Para geração de imagens exclusivas

Configure as chaves no arquivo `.env`:

```bash
OPENAI_API_KEY=sua_chave_aqui
NEWS_API_KEY=sua_chave_aqui
DALLE_API_KEY=sua_chave_aqui
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👤 Autor

**dronreef2**

- GitHub: [@dronreef2](https://github.com/dronreef2)

## 🙏 Agradecimentos

- Inspirado pela necessidade de automatizar a criação de conteúdo jornalístico
- Construído com Python e amor por tecnologia

---

**Nota**: Este é um projeto em desenvolvimento. A versão atual usa dados simulados para demonstração. Para uso em produção, configure as APIs necessárias no arquivo `.env`.