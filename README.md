próximos Passos Sugeridos:
Atualizar testes para nova API (5 testes pendentes)
Adicionar Imagen quando API estiver disponível
Integrar APIs de notícias reais (NewsAPI, etc.)
Criar interface web (Flask/FastAPI)
Deploy em produção usando o deploy.sh criado

# 📰 CriarNoticia - Geração Automática de Briefings

[![Status](https://img.shields.io/badge/status-✅_funcionando-success)](.)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-2.0--flash-orange.svg)](https://ai.google.dev/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> Sistema automatizado para criar briefings completos de notícias usando IA Google Gemini

## ✨ Características

- 🤖 **Geração Automática**: Cria briefings completos sobre qualquer tópico
- 📊 **Análise Profissional**: 2 parágrafos com fatos e implicações
- 📚 **Fontes Verificadas**: 3-5 artigos relevantes com resumos
- 🎨 **Prompts Artísticos**: Descrições para geradores de imagem (DALL-E, Midjourney, etc.)
- 🔒 **Seguro**: Usa variáveis de ambiente (.env)
- 📝 **Logging Completo**: Rastreamento detalhado de operações
- 🔄 **Fallback Inteligente**: Tenta múltiplos modelos automaticamente
- ✅ **Validado**: Estrutura de dados robusta com Pydantic

## 🚀 Início Rápido

```bash
# 1. Clone o repositório
git clone https://github.com/dronreef2/CriarNoticia.git
cd CriarNoticia

# 2. Instale dependências
pip install -r requirements.txt

# 3. Configure sua API key do Google
cp config.env.example .env
# Edite .env e adicione: GOOGLE_API_KEY=sua_chave_aqui

# 4. Execute!
python criar_briefing_noticias_v2.py
```

### Obter API Key

1. Acesse: https://aistudio.google.com/app/apikey
2. Crie uma nova API key
3. Copie e cole no arquivo `.env`

## 📖 Exemplo de Uso

### Entrada
```python
topico = "lançamento e recepção do Apple Vision Pro"
```

### Saída
```
==================================================
📰 BRIEFING DE NOTÍCIAS AVANÇADO 📰
==================================================
TÓPICO: Lançamento e Recepção do Apple Vision Pro

--- ANÁLISE SINTETIZADA ---
O lançamento do Apple Vision Pro gerou grande expectativa 
e uma onda de análises detalhadas. A maioria dos reviews 
concorda que o dispositivo representa um avanço significativo 
em computação espacial, oferecendo experiências imersivas 
e uma integração inovadora entre o mundo digital e físico...

--- FONTES UTILIZADAS ---
1. Apple Vision Pro review (The Verge)
2. What the reviews say (BBC News)
3. Reviews Are In (The New York Times)
4. magic, until it's not (Engadget)
5. A Glimpse of the Future (Wall Street Journal)

--- PROMPT PARA IMAGEM ---
A futuristic cityscape viewed through the lens of an Apple 
Vision Pro, with augmented reality elements seamlessly 
integrated into the urban environment...
==================================================
```

## 📁 Estrutura do Projeto

```
CriarNoticia/
├── criar_briefing_noticias_v2.py  ⭐ Versão melhorada (USE ESTA!)
├── criar_briefing_simples.py      📝 Versão simplificada
├── criar_briefing_noticias.py     📄 Versão original (referência)
├── requirements.txt               📦 Dependências
├── config.env.example             🔧 Template de configuração
├── .env                          🔒 Sua configuração (não commitar!)
├── tests/                        🧪 Testes automatizados
├── docs/                         📚 Documentação completa
└── output/                       💾 Briefings gerados
```

## 🔧 Arquivos Principais

### `criar_briefing_noticias_v2.py` ⭐ **[RECOMENDADO]**
- ✅ Versão melhorada e totalmente funcional
- ✅ Usa modelo gemini-2.0-flash-exp (com fallbacks automáticos)
- ✅ Logging detalhado, type hints, validação Pydantic
- ✅ Tratamento robusto de erros
- ✅ Configuração via .env

### `criar_briefing_simples.py`
- Versão minimalista para testes rápidos
- Código limpo e direto
- Bom para entender o funcionamento básico

### `criar_briefing_noticias.py`
- Versão original do projeto
- Mantido para referência histórica
- Requer adaptações para uso

## 🛠️ Comandos Úteis

```bash
# Verificar configuração
python run.py --check

# Executar testes
python run.py --test

# Gerar briefing
python run.py --run

# Versão simplificada
python criar_briefing_simples.py
```

## 📊 Modelos Disponíveis

| Modelo | Status | Performance |
|--------|--------|-------------|
| `gemini-2.0-flash-exp` | ✅ FUNCIONA | Excelente |
| `gemini-1.5-flash` | ✅ Disponível | Muito Boa |
| `gemini-1.5-pro` | 🟡 Limitado | Boa |
| `gemini-pro` | ❌ Deprecated | - |

O sistema tenta automaticamente cada modelo até encontrar um disponível.

## 🧪 Testes

```bash
# Instalar dependências de teste
pip install pytest pytest-cov

# Executar todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=. --cov-report=html

# Teste específico
pytest tests/test_criar_briefing.py -v
```

**Status Atual**: 5/10 testes passando (modelos de dados validados)

## 📚 Documentação Completa

- [START_HERE.md](docs/START_HERE.md) - Comece aqui!
- [ANALISE_PROJETO.md](docs/ANALISE_PROJETO.md) - Análise técnica detalhada
- [QUICKSTART.md](QUICKSTART.md) - Guia rápido de uso
- [CONTRIBUTING.md](CONTRIBUTING.md) - Como contribuir
- [CHANGELOG.md](CHANGELOG.md) - Histórico de versões
- [RESULTADO_FINAL.md](RESULTADO_FINAL.md) - Resumo completo do projeto

## 🔒 Segurança

⚠️ **NUNCA commite sua API key!**

```bash
# Arquivo .env já está no .gitignore
echo ".env" >> .gitignore

# Use sempre variáveis de ambiente
GOOGLE_API_KEY=sua_chave_aqui python criar_briefing_noticias_v2.py
```

## 🐛 Troubleshooting

### Erro: "module 'google.generativeai' has no attribute 'Client'"
- **Causa**: API antiga (genai.Client() não existe mais)
- **Solução**: Use `criar_briefing_noticias_v2.py`

### Erro: "404 models/gemini-pro is not found"
- **Causa**: Modelo não disponível
- **Solução**: O sistema usa fallback automático para gemini-2.0-flash-exp

### Erro: "GOOGLE_API_KEY não encontrada"
- **Causa**: API key não configurada
- **Solução**: Crie arquivo `.env` com sua chave

## 🎯 Roadmap

- [x] ✅ Geração de briefings funcionando
- [x] ✅ Análise e síntese de informações
- [x] ✅ Prompts para geração de imagens
- [x] ✅ Logging e tratamento de erros
- [x] ✅ Testes automatizados (básicos)
- [ ] 🔄 Geração de imagens (aguardando API Imagen)
- [ ] 🔄 Integração com APIs de notícias reais
- [ ] 🔄 Interface web (Flask/FastAPI)
- [ ] 🔄 Exportação para PDF/Word
- [ ] 🔄 Agendamento automático

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -am 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes.

## 🙏 Agradecimentos

- [Google Gemini](https://ai.google.dev/) - API de IA generativa
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validação de dados
- [GitHub Copilot](https://github.com/features/copilot) - Assistente de desenvolvimento

## 📧 Contato

- **Repositório**: [github.com/dronreef2/CriarNoticia](https://github.com/dronreef2/CriarNoticia)
- **Issues**: [github.com/dronreef2/CriarNoticia/issues](https://github.com/dronreef2/CriarNoticia/issues)

---

**Desenvolvido com ❤️ usando GitHub Copilot**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made with Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange.svg)](https://ai.google.dev/)
