# Automação de Registro de Caixa --- Plano do Projeto

## Objetivo

Criar um sistema em Python, com fins educativos, capaz de automatizar o
preenchimento do registro de caixa das empresas a partir de extratos
bancários mensais em PDF, sem alterar o modelo de planilha Excel já
utilizado pela empresa.

O foco principal é aprendizado prático de Python, não a criação de um
produto comercial final.

------------------------------------------------------------------------

## Problema Resolvido

O processo manual atual envolve: - leitura de extratos bancários em
PDF - digitação manual das movimentações - alto risco de erros e perda
de tempo

O sistema atuará como um pré-preenchimento inteligente, mantendo revisão
humana.

------------------------------------------------------------------------

## Funcionamento do Sistema

1.  Receber extratos bancários em PDF (priorizando PDFs gerados pelo
    banco)
2.  Extrair informações relevantes:
    -   data
    -   descrição/histórico
    -   valor
    -   identificação de débito ou crédito
3.  Tratar e organizar os dados:
    -   ordenação por data
    -   normalização de valores
4.  Abrir o Excel modelo da empresa
5.  Preencher automaticamente o registro de caixa:
    -   respeitando layout, fórmulas e estrutura existentes
6.  Salvar uma nova cópia preenchida

------------------------------------------------------------------------

## Escopo do Projeto

-   Foco inicial em um banco e um formato de extrato
-   Execução via terminal
-   Código simples, legível e didático

Não inclui: - interface gráfica - banco de dados - aplicação web -
automação total sem conferência

------------------------------------------------------------------------

## Objetivo Educacional

-   Consolidar fundamentos de Python
-   Trabalhar com bibliotecas reais
-   Aprender automação aplicada ao mundo real
-   Criar projeto de portfólio

------------------------------------------------------------------------

## Filosofia

-   Começar simples
-   Evoluir por etapas
-   Validar cada fase
-   Priorizar entendimento do código
