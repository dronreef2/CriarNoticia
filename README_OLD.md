# CriarNoticia

Pipeline de Conteúdo Automatizado com Google Gemini API

## 📋 Descrição

Este projeto implementa um pipeline automatizado de criação de conteúdo avançado que combina as capacidades mais recentes da API do Google Gemini, incluindo:

- **Busca na Web em Tempo Real** (`GoogleSearch`)
- **Estruturação de Dados com Pydantic** (`response_schema`)
- **Geração de Conteúdo Multimodal** (texto e imagens)
- **Análise e Síntese Inteligente** de informações

## 🚀 Funcionalidades

### Pipeline de 4 Etapas

1. **Busca e Coleta**: Utiliza `GoogleSearch` para encontrar informações relevantes e atuais sobre qualquer tópico
2. **Estruturação**: Força o modelo a retornar dados em formato JSON limpo e previsível usando Pydantic
3. **Análise e Síntese**: O modelo atua como analista, criando análises coesas e aprofundadas
4. **Enriquecimento Visual**: Gera imagens de capa usando o modelo Imagen 3.0

## 📦 Instalação

### Requisitos

- Python 3.8 ou superior
- Chave de API do Google AI Studio

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/dronreef2/CriarNoticia.git
cd CriarNoticia
```

2. Instale as dependências:
```bash
pip install -q -r requirements.txt
```

3. Configure sua API Key:
   - Obtenha sua chave em: https://aistudio.google.com/app/apikey
   - Edite o arquivo `criar_briefing_noticias.py` e substitua `"SUA_API_KEY_AQUI"` pela sua chave real
   - **Nota de Segurança**: Em ambientes de produção, use variáveis de ambiente ou gerenciadores de segredos

## 💻 Uso

### Exemplo Básico

```python
python criar_briefing_noticias.py
```

O script irá:
1. Buscar notícias sobre o tópico configurado
2. Estruturar as informações encontradas
3. Gerar uma análise sintetizada
4. Criar uma imagem visual representativa
5. Salvar a imagem como `briefing_[topico].png`

### Personalizar o Tópico

Edite o arquivo `criar_briefing_noticias.py` e modifique a variável `tópico`:

```python
if __name__ == "__main__":
    tópico = "seu tópico de interesse aqui"
    meu_briefing = criar_briefing_avancado(tópico)
    # ...
```

## 📊 Estrutura de Dados

### ArtigoEncontrado

```python
class ArtigoEncontrado(BaseModel):
    titulo: str          # Título exato da matéria
    fonte: str           # Veículo de comunicação
    resumo_curto: str    # Resumo de 1-2 frases
```

### BriefingDeNoticias

```python
class BriefingDeNoticias(BaseModel):
    topico_central: str         # Tema principal
    artigos: List[ArtigoEncontrado]  # 3-5 artigos relevantes
    analise_sintetizada: str    # Análise aprofundada em 2 parágrafos
    prompt_para_imagem: str     # Prompt para geração de imagem
```

## 🎯 Por que esta Abordagem é "Avançada"?

1. **Confiabilidade e Previsibilidade**: Graças ao `response_schema`, você recebe objetos Python limpos e estruturados
2. **Conteúdo Atualizado**: Integração com `GoogleSearch` garante dados em tempo real
3. **Eficiência**: Múltiplas tarefas em uma única chamada (pesquisar, filtrar, resumir, analisar)
4. **Multimodalidade**: Combinação de geração de texto e imagens para conteúdo profissional
5. **Código Limpo**: Novo SDK `genai.Client()` organiza tudo de forma lógica

## 🔧 Funcionalidades Opcionais (Futuras)

- **Análise de Documentos Internos**: Upload de PDFs ou arquivos de texto usando `client.files.upload()`
- **Otimização de Custos**: Uso de `Context Caching` para documentos longos reutilizados
- **Múltiplos Idiomas**: Suporte para análise em diferentes línguas
- **Publicação Automática**: Integração com plataformas de blog e redes sociais

## 📝 Exemplo de Saída

```
🚀 Iniciando a criação do briefing para: 'lançamento e recepção do Apple Vision Pro'
🔎 Buscando e analisando notícias...
✅ Briefing estruturado com sucesso!

==================================================
📰 BRIEFING DE NOTÍCIAS AVANÇADO 📰
==================================================
TÓPICO: Lançamento do Apple Vision Pro

--- ANÁLISE SINTETIZADA ---
[Análise gerada pelo modelo...]

--- FONTES UTILIZADAS ---
- Artigo 1 (Fonte 1)
- Artigo 2 (Fonte 2)
- Artigo 3 (Fonte 3)
==================================================

🎨 Gerando imagem com o prompt: '[prompt gerado]'...
✅ Imagem salva como 'briefing_lançamento_do_apple_vision_pro.png'
```

## 🔒 Segurança

- **Nunca** compartilhe sua API Key publicamente
- Use variáveis de ambiente em produção: `os.getenv('GOOGLE_API_KEY')`
- Adicione `.env` ao `.gitignore` se usar arquivo de configuração
- Monitore o uso da API para evitar custos inesperados

## 📄 Licença

Este projeto é fornecido como exemplo educacional. Use-o livremente para aprender e adaptar às suas necessidades.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## 📚 Recursos Adicionais

- [Documentação do Google Gemini API](https://ai.google.dev/docs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Google AI Studio](https://aistudio.google.com/)

## ✨ Créditos

Desenvolvido utilizando as mais recentes funcionalidades da API do Google Gemini, incluindo:
- Gemini 1.5 Pro para geração de texto
- Imagen 3.0 para geração de imagens
- Google Search integration para dados em tempo real