from src.extrator_pdf import extrair_dados_pdf
from src.tratamento import tratar_dados
from src.excel_writer import preencher_excel

def main():
    pdf = "data/pdfs/extrato.pdf"
    modelo = "models/modelo_caixa.xlsx"
    saida = "data/output/caixa_preenchido.xl"


    dados = extrair_dados_pdf(pdf)
    dados_tratados = tratar_dados(dados)
    preencher_excel(modelo, dados_tratados,saida)

    print("Fluxo executado com")

    if __name__ == "__main__":
        main()s
