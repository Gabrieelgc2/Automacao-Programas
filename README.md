# Windows Setup Automation with Python

Este projeto consiste em uma **automação completa para configuração inicial de sistemas Windows**, desenvolvida em Python.  
Seu objetivo é **automatizar tarefas repetitivas e demoradas** que normalmente são realizadas manualmente após a instalação do Windows.

O script combina **PowerShell, Chocolatey e automação gráfica** para instalar softwares essenciais, remover aplicativos desnecessários e executar comandos administrativos de forma padronizada.

---

## 🎯 Objetivo do Projeto

O projeto foi criado para:

- Automatizar a configuração de novos computadores
- Reduzir o tempo gasto em instalações manuais
- Padronizar ambientes Windows
- Demonstrar o uso de automação de sistemas com Python
- Servir como base para setups corporativos ou pessoais

---

## ⚙️ Visão Geral do Funcionamento

O fluxo do projeto segue uma sequência bem definida:

1. Verificação de permissões administrativas
2. Execução de comandos PowerShell
3. Instalação automática de softwares
4. Remoção de aplicações nativas do Windows
5. Automação de interface gráfica quando necessário
6. Empacotamento do script em um executável (.exe)

---

## 🔐 Execução como Administrador

Ao iniciar, o script verifica se está sendo executado com **permissões de Administrador**.  
Caso não esteja, o processo é interrompido, pois muitas das operações exigem acesso elevado ao sistema, como:

- Instalação de pacotes
- Execução de comandos PowerShell
- Remoção de aplicativos do Windows

---

## 🧩 Uso de PowerShell

O projeto utiliza **PowerShell** para executar comandos diretamente no sistema operacional, incluindo:

- Instalação do **Chocolatey**
- Execução de scripts administrativos
- Gerenciamento de pacotes
- Remoção de aplicativos nativos (bloatware)

O PowerShell é invocado a partir do Python usando módulos como `subprocess`, garantindo maior controle e automação do ambiente.

---

## 📦 Chocolatey – Gerenciador de Pacotes

Após a verificação inicial, o script instala automaticamente o **Chocolatey**, um gerenciador de pacotes para Windows.

Com o Chocolatey, o projeto realiza a instalação silenciosa de softwares essenciais, como:

- Google Chrome
- Adobe Reader
- WinRAR

Isso elimina a necessidade de downloads manuais e cliques durante a instalação.

---

## 🧹 Remoção de Aplicativos Nativos (Bloatware)

O script remove aplicativos padrão do Windows que geralmente não são necessários em ambientes profissionais, utilizando comandos PowerShell.

Essa etapa ajuda a:

- Melhorar o desempenho do sistema
- Reduzir consumo de recursos
- Deixar o ambiente mais limpo e organizado

---

## 🖱️ Automação Gráfica com PyAutoGUI

Para cenários onde a automação via terminal não é suficiente, o projeto utiliza **PyAutoGUI** para:

- Simular cliques do mouse
- Enviar comandos de teclado
- Interagir com janelas e menus
- Reconhecer elementos visuais através de imagens (.png)

As imagens presentes no projeto são usadas como referência para localizar elementos na tela durante a automação.

---

## 🧪 Geração de Executável (.exe)

O projeto é empacotado utilizando **PyInstaller**, permitindo a geração de um arquivo executável (`.exe`).

Isso possibilita:

- Executar o projeto sem instalar Python
- Usar o script em qualquer computador Windows
- Facilitar a distribuição da automação

---

## 📂 Estrutura do Projeto

Automacao-Programas/
├── Automacao.py # Script principal de automação
├── Automacao.spec # Configuração do PyInstaller
├── *.png # Imagens usadas na automação gráfica
├── build/ # Arquivos temporários de compilação
├── dist/
│ └── Automacao.exe # Executável final


---

## ⚠️ Observações Importantes

- Compatível apenas com **Windows**
- Deve ser executado como **Administrador**
- Algumas automações dependem da resolução da tela e idioma do sistema
- Recomenda-se revisar e adaptar o código antes de uso em produção

---
