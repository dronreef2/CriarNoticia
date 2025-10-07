"""
Script auxiliar para executar o projeto com facilidade
======================================================

Este script facilita a execução do projeto com diferentes opções.
"""

import argparse
import sys
import os


def verificar_ambiente():
    """Verifica se o ambiente está configurado corretamente."""
    print("🔍 Verificando ambiente...")
    
    # Verificar .env
    if not os.path.exists('.env'):
        print("❌ Arquivo .env não encontrado")
        print("💡 Execute: python setup.py")
        return False
    
    # Verificar se .env tem conteúdo
    with open('.env', 'r') as f:
        conteudo = f.read()
        if 'sua-chave-api-aqui' in conteudo or len(conteudo) < 50:
            print("⚠️  Arquivo .env parece não ter API key configurada")
            print("💡 Edite o arquivo .env e adicione sua API key")
            return False
    
    print("✅ Ambiente configurado corretamente")
    return True


def executar_testes(verbose=False, cobertura=False):
    """Executa a suite de testes."""
    import subprocess
    
    print("\n🧪 Executando testes...")
    
    cmd = ["pytest", "tests/", "-v" if verbose else ""]
    
    if cobertura:
        cmd.extend(["--cov=.", "--cov-report=html", "--cov-report=term"])
    
    cmd = [c for c in cmd if c]  # Remover strings vazias
    
    result = subprocess.run(cmd)
    return result.returncode == 0


def executar_projeto(topico=None, versao=2):
    """Executa o projeto."""
    import subprocess
    
    script = f"criar_briefing_noticias_v{versao}.py" if versao == 2 else "criar_briefing_noticias.py"
    
    if not os.path.exists(script):
        print(f"❌ Arquivo {script} não encontrado")
        return False
    
    print(f"\n🚀 Executando {script}...")
    
    env = os.environ.copy()
    if topico:
        env['TOPICO'] = topico
    
    result = subprocess.run(["python", script], env=env)
    return result.returncode == 0


def gerar_documentacao():
    """Gera documentação do projeto."""
    print("\n📚 Gerando documentação...")
    print("Os seguintes arquivos de documentação estão disponíveis:")
    print("  - START_HERE.md")
    print("  - README.md")
    print("  - QUICKSTART.md")
    print("  - RELATORIO_FINAL.md")
    print("  - ANALISE_PROJETO.md")
    print("  - PLANO_IMPLEMENTACAO.md")
    print("  - CONTRIBUTING.md")
    print("\n✅ Documentação já está gerada!")


def main():
    """Função principal."""
    parser = argparse.ArgumentParser(
        description="Script auxiliar para CriarNoticia",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python run.py --check          # Verificar ambiente
  python run.py --test           # Executar testes
  python run.py --test --cov     # Testes com cobertura
  python run.py --run            # Executar projeto
  python run.py --run --topico "IA na medicina"  # Com tópico personalizado
  python run.py --docs           # Ver documentação disponível
        """
    )
    
    parser.add_argument('--check', action='store_true',
                       help='Verificar configuração do ambiente')
    parser.add_argument('--test', action='store_true',
                       help='Executar testes')
    parser.add_argument('--cov', action='store_true',
                       help='Gerar relatório de cobertura (use com --test)')
    parser.add_argument('--run', action='store_true',
                       help='Executar o projeto')
    parser.add_argument('--topico', type=str,
                       help='Tópico para pesquisar (use com --run)')
    parser.add_argument('--versao', type=int, choices=[1, 2], default=2,
                       help='Versão do script a executar (1 ou 2, padrão: 2)')
    parser.add_argument('--docs', action='store_true',
                       help='Listar documentação disponível')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Saída detalhada')
    
    args = parser.parse_args()
    
    # Se nenhum argumento, mostrar ajuda
    if not any([args.check, args.test, args.run, args.docs]):
        parser.print_help()
        return
    
    print("="*60)
    print("CriarNoticia - Script Auxiliar")
    print("="*60)
    
    sucesso = True
    
    if args.check:
        sucesso = verificar_ambiente()
    
    if args.test:
        sucesso = executar_testes(verbose=args.verbose, cobertura=args.cov)
    
    if args.run:
        if not verificar_ambiente():
            print("\n❌ Ambiente não configurado. Execute primeiro: python setup.py")
            sucesso = False
        else:
            sucesso = executar_projeto(topico=args.topico, versao=args.versao)
    
    if args.docs:
        gerar_documentacao()
    
    print("\n" + "="*60)
    if sucesso:
        print("✅ Operação concluída com sucesso!")
    else:
        print("❌ Operação concluída com erros.")
    print("="*60)
    
    sys.exit(0 if sucesso else 1)


if __name__ == "__main__":
    main()
