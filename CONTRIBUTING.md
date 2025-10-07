# Contributing to CriarNoticia

Obrigado por considerar contribuir para o CriarNoticia! Este documento fornece diretrizes para contribuições.

## 🤝 Como Contribuir

### Reportando Bugs

Se você encontrar um bug, por favor crie uma issue incluindo:

1. **Descrição clara do problema**
2. **Passos para reproduzir**
3. **Comportamento esperado vs atual**
4. **Versão do Python e dependências**
5. **Logs de erro (se aplicável)**

### Sugerindo Melhorias

Para sugerir melhorias:

1. **Verifique se já não existe uma issue similar**
2. **Descreva claramente a melhoria proposta**
3. **Explique o caso de uso**
4. **Forneça exemplos, se possível**

## 🔧 Desenvolvimento

### Configuração do Ambiente

1. **Fork e clone o repositório:**
```bash
git clone https://github.com/seu-usuario/CriarNoticia.git
cd CriarNoticia
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale dependências de desenvolvimento:**
```bash
pip install -r requirements.txt
pip install pytest pytest-cov pylint black
```

4. **Configure o ambiente:**
```bash
python setup.py
```

### Padrões de Código

- **Formatação**: Use `black` para formatação automática
  ```bash
  black *.py
  ```

- **Linting**: Use `pylint` para verificar qualidade
  ```bash
  pylint criar_briefing_noticias.py
  ```

- **Type Hints**: Use type hints em todas as funções
  ```python
  def funcao(parametro: str) -> Optional[Dict]:
      ...
  ```

- **Docstrings**: Use docstrings no formato Google
  ```python
  def funcao(parametro: str) -> bool:
      """
      Descrição breve da função.
      
      Args:
          parametro: Descrição do parâmetro
      
      Returns:
          bool: Descrição do retorno
      
      Raises:
          ValueError: Quando parametro é inválido
      """
  ```

### Executando Testes

```bash
# Executar todos os testes
pytest

# Com cobertura
pytest --cov=. --cov-report=html

# Testes específicos
pytest tests/test_criar_briefing.py -v
```

### Workflow de Contribuição

1. **Crie uma branch:**
```bash
git checkout -b feature/minha-feature
# ou
git checkout -b fix/meu-bugfix
```

2. **Faça suas alterações:**
   - Escreva código limpo e documentado
   - Adicione testes para novas funcionalidades
   - Mantenha commits atômicos e descritivos

3. **Commit suas mudanças:**
```bash
git add .
git commit -m "feat: adiciona nova funcionalidade X"
```

**Padrões de commit:**
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `test:` Adicionar ou modificar testes
- `refactor:` Refatoração de código
- `style:` Formatação, ponto e vírgula, etc
- `chore:` Tarefas de manutenção

4. **Push para seu fork:**
```bash
git push origin feature/minha-feature
```

5. **Abra um Pull Request:**
   - Descreva claramente as mudanças
   - Referencie issues relacionadas
   - Aguarde review

## 📋 Checklist para Pull Requests

Antes de submeter um PR, verifique:

- [ ] Código segue os padrões do projeto
- [ ] Testes adicionados/atualizados
- [ ] Todos os testes passam
- [ ] Documentação atualizada
- [ ] Commits seguem o padrão
- [ ] Não há conflitos com a branch main
- [ ] Code review solicitado

## 🧪 Escrevendo Testes

Exemplo de teste:

```python
import pytest
from criar_briefing_noticias import ArtigoEncontrado

def test_artigo_valido():
    """Testa criação de artigo válido."""
    artigo = ArtigoEncontrado(
        titulo="Teste",
        fonte="Fonte Teste",
        resumo_curto="Resumo"
    )
    assert artigo.titulo == "Teste"

def test_artigo_invalido():
    """Testa validação de dados inválidos."""
    with pytest.raises(ValidationError):
        ArtigoEncontrado(titulo="Teste")  # Faltam campos
```

## 🎯 Áreas que Precisam de Contribuição

- [ ] Testes unitários adicionais
- [ ] Suporte a múltiplos idiomas
- [ ] Integração com mais fontes de dados
- [ ] Melhorias na geração de imagens
- [ ] Otimização de performance
- [ ] Documentação e exemplos
- [ ] CI/CD pipeline

## 📞 Dúvidas?

Se tiver dúvidas:

1. Consulte a [documentação](README.md)
2. Verifique as [issues existentes](https://github.com/dronreef2/CriarNoticia/issues)
3. Abra uma nova issue com a tag `question`

## 📜 Código de Conduta

- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros

Obrigado por contribuir! 🎉
