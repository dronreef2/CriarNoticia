# Guia de Início Rápido - CriarNoticia

Este guia irá ajudá-lo a começar a usar o pipeline de conteúdo automatizado em poucos minutos.

## 🚀 Configuração Inicial (5 minutos)

### Passo 1: Clone o Repositório
```bash
git clone https://github.com/dronreef2/CriarNoticia.git
cd CriarNoticia
```

### Passo 2: Instale as Dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Obtenha sua API Key
1. Acesse: https://aistudio.google.com/app/apikey
2. Faça login com sua conta Google
3. Clique em "Create API Key"
4. Copie a chave gerada

### Passo 4: Configure a API Key

**Opção A: Direto no Código (mais simples, menos seguro)**
```python
# Edite o arquivo criar_briefing_noticias.py
# Linha 13: Substitua "SUA_API_KEY_AQUI" pela sua chave
genai.configure(api_key="sua-chave-real-aqui")
```

**Opção B: Via Variável de Ambiente (recomendado)**
```bash
# Linux/Mac
export GOOGLE_API_KEY="sua-chave-aqui"

# Windows (PowerShell)
$env:GOOGLE_API_KEY="sua-chave-aqui"
```

Depois, modifique o arquivo `criar_briefing_noticias.py`:
```python
import os
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
```

## 🎯 Primeiro Uso

### Execute o Script Padrão
```bash
python criar_briefing_noticias.py
```

Isso irá:
1. Buscar notícias sobre "lançamento e recepção do Apple Vision Pro"
2. Estruturar as informações em JSON
3. Gerar uma análise sintetizada
4. Criar uma imagem representativa

### Personalize o Tópico

Edite o arquivo `criar_briefing_noticias.py`:
```python
if __name__ == "__main__":
    # Mude esta linha:
    tópico = "seu tópico de interesse aqui"
    
    meu_briefing = criar_briefing_avancado(tópico)
    # ...
```

Exemplos de tópicos:
- "inteligência artificial na saúde"
- "carros elétricos no Brasil"
- "games mais aguardados de 2024"
- "mudanças climáticas e tecnologia"

## 📊 Resultados Esperados

Após executar, você verá no terminal:
```
🚀 Iniciando a criação do briefing para: '[seu tópico]'
🔎 Buscando e analisando notícias...
✅ Briefing estruturado com sucesso!

==================================================
📰 BRIEFING DE NOTÍCIAS AVANÇADO 📰
==================================================
TÓPICO: [Tópico Central]

--- ANÁLISE SINTETIZADA ---
[Análise gerada pelo modelo]

--- FONTES UTILIZADAS ---
- Artigo 1 (Fonte 1)
- Artigo 2 (Fonte 2)
...
==================================================

🎨 Gerando imagem com o prompt: '[prompt]'...
✅ Imagem salva como 'briefing_[topico].png'
```

E será criado um arquivo PNG com a imagem gerada.

## 🔧 Exemplos Avançados

Veja o arquivo `exemplos_uso.py` para casos de uso avançados:
```bash
python exemplos_uso.py
```

Recursos disponíveis:
- Análise de múltiplos tópicos
- Salvamento em arquivos (TXT/JSON)
- Tratamento robusto de erros
- Análise comparativa
- E muito mais!

## ❓ Solução de Problemas

### Erro: "API Key inválida"
- Verifique se copiou a chave completa
- Certifique-se de que não há espaços extras
- Confirme que a chave está ativa no Google AI Studio

### Erro: "Módulo não encontrado"
```bash
pip install google-generativeai pydantic
```

### Erro de Conexão
- Verifique sua conexão com a internet
- Alguns países podem ter restrições de acesso à API

### Imagem não é gerada
- Verifique se tem créditos suficientes na API
- O modelo Imagen pode não estar disponível em todas as regiões

## 💡 Dicas de Uso

1. **Custos**: Monitore o uso da API em https://aistudio.google.com/
2. **Tópicos Específicos**: Quanto mais específico o tópico, melhores os resultados
3. **Idioma**: O pipeline funciona em português, mas o prompt para imagem é gerado em inglês
4. **Tempo**: A primeira execução pode demorar 30-60 segundos
5. **Cache**: Reutilize briefings salvos para economizar chamadas de API

## 📚 Próximos Passos

- Explore os exemplos em `exemplos_uso.py`
- Leia a documentação completa em `README.md`
- Customize o código para suas necessidades
- Integre com outras ferramentas (blogs, redes sociais, etc.)

## 🆘 Precisa de Ajuda?

- Documentação oficial: https://ai.google.dev/docs
- Issues no GitHub: https://github.com/dronreef2/CriarNoticia/issues
- Pydantic Docs: https://docs.pydantic.dev/

---

**Boa sorte criando conteúdo avançado! 🎉**
