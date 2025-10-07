#!/usr/bin/env python3
"""
Script de Setup para CriarNoticia
================================

Este script automatiza a configuração inicial do projeto.
"""

import os
import shutil
import sys

def criar_arquivo_env():
    """Cria o arquivo .env se não existir."""
    if os.path.exists('.env'):
        print("⚠️  Arquivo .env já existe. Pulando criação.")
        return False
    
    if not os.path.exists('config.env.example'):
        print("❌ Arquivo config.env.example não encontrado!")
        return False
    
    shutil.copy('config.env.example', '.env')
    print("✅ Arquivo .env criado com sucesso!")
    print("📝 Edite o arquivo .env e adicione sua API key do Google AI Studio")
    print("   Obtenha em: https://aistudio.google.com/app/apikey")
    return True

def verificar_dependencias():
    """Verifica se as dependências estão instaladas."""
    dependencias = {
        'google.generativeai': 'google-generativeai',
        'pydantic': 'pydantic',
        'dotenv': 'python-dotenv'
    }
    
    faltando = []
    for modulo, pacote in dependencias.items():
        try:
            __import__(modulo)
            print(f"✅ {pacote} instalado")
        except ImportError:
            print(f"❌ {pacote} não encontrado")
            faltando.append(pacote)
    
    if faltando:
        print("\n⚠️  Dependências faltando. Instale com:")
        print(f"   pip install {' '.join(faltando)}")
        return False
    
    return True

def criar_diretorios():
    """Cria diretórios necessários."""
    diretorios = ['output', 'tests']
    
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"✅ Diretório '{diretorio}/' criado")
        else:
            print(f"⚠️  Diretório '{diretorio}/' já existe")

def main():
    """Função principal do setup."""
    print("="*70)
    print("SETUP - CriarNoticia")
    print("="*70)
    print()
    
    print("1️⃣  Verificando dependências...")
    if not verificar_dependencias():
        print("\n❌ Instale as dependências antes de continuar:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    print("\n2️⃣  Criando arquivo de configuração...")
    arquivo_criado = criar_arquivo_env()
    
    print("\n3️⃣  Criando diretórios...")
    criar_diretorios()
    
    print("\n" + "="*70)
    print("✅ SETUP CONCLUÍDO!")
    print("="*70)
    
    if arquivo_criado:
        print("\n📝 PRÓXIMOS PASSOS:")
        print("   1. Edite o arquivo .env e adicione sua API key")
        print("   2. Execute: python criar_briefing_noticias.py")
    else:
        print("\n✅ Projeto já configurado. Execute:")
        print("   python criar_briefing_noticias.py")
    
    print()

if __name__ == "__main__":
    main()
