#!/bin/bash
# Script de Deploy para CriarNoticia
# ===================================

set -e  # Sair se houver erro

echo "🚀 Iniciando processo de deploy..."
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para mensagens
info() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# 1. Verificar se está na branch correta
echo "1️⃣  Verificando branch..."
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    warning "Você está na branch '$CURRENT_BRANCH', não 'main'"
    read -p "Continuar mesmo assim? (s/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi
info "Branch verificada: $CURRENT_BRANCH"

# 2. Verificar se há mudanças não commitadas
echo ""
echo "2️⃣  Verificando mudanças não commitadas..."
if ! git diff-index --quiet HEAD --; then
    warning "Há mudanças não commitadas"
    git status --short
    read -p "Continuar mesmo assim? (s/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        exit 1
    fi
fi
info "Verificação de mudanças concluída"

# 3. Executar testes
echo ""
echo "3️⃣  Executando testes..."
if python -m pytest tests/ -v --tb=short; then
    info "Todos os testes passaram"
else
    error "Testes falharam! Corrija antes de fazer deploy."
    exit 1
fi

# 4. Verificar cobertura de testes
echo ""
echo "4️⃣  Verificando cobertura de testes..."
python -m pytest tests/ --cov=. --cov-report=term-missing --cov-report=html | grep "TOTAL"
info "Relatório de cobertura gerado"

# 5. Lint do código
echo ""
echo "5️⃣  Verificando qualidade do código..."
if python -m pylint criar_briefing_noticias_v2.py --exit-zero | grep "Your code has been rated"; then
    info "Verificação de qualidade concluída"
fi

# 6. Verificar se .env não será commitado
echo ""
echo "6️⃣  Verificando arquivos sensíveis..."
if git ls-files | grep -q "\.env$"; then
    error "Arquivo .env está sendo rastreado pelo git!"
    error "Execute: git rm --cached .env"
    exit 1
fi
info "Nenhum arquivo sensível detectado"

# 7. Atualizar versão (opcional)
echo ""
echo "7️⃣  Versão atual:"
if [ -f "VERSION" ]; then
    cat VERSION
else
    echo "2.0.0" > VERSION
fi

read -p "Deseja atualizar a versão? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    read -p "Nova versão (ex: 2.0.1): " NEW_VERSION
    echo "$NEW_VERSION" > VERSION
    git add VERSION
    git commit -m "chore: bump version to $NEW_VERSION"
    info "Versão atualizada para $NEW_VERSION"
fi

# 8. Push para repositório
echo ""
echo "8️⃣  Fazendo push para repositório..."
read -p "Fazer push para origin/$CURRENT_BRANCH? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    git push origin "$CURRENT_BRANCH"
    info "Push realizado com sucesso"
else
    warning "Push cancelado"
fi

# 9. Criar tag (opcional)
echo ""
echo "9️⃣  Criar tag de release?"
read -p "Criar tag? (s/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    VERSION=$(cat VERSION 2>/dev/null || echo "2.0.0")
    TAG="v$VERSION"
    read -p "Tag name (padrão: $TAG): " CUSTOM_TAG
    TAG=${CUSTOM_TAG:-$TAG}
    
    git tag -a "$TAG" -m "Release $TAG"
    git push origin "$TAG"
    info "Tag $TAG criada e enviada"
fi

# 10. Deploy finalizado
echo ""
echo "="*60
echo -e "${GREEN}🎉 DEPLOY CONCLUÍDO COM SUCESSO! 🎉${NC}"
echo "="*60
echo ""
echo "Próximos passos:"
echo "  1. Verificar GitHub Actions"
echo "  2. Monitorar logs de produção"
echo "  3. Atualizar documentação se necessário"
echo ""
