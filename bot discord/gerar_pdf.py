from pypdf import PdfReader, PdfWriter
import os

def gerar_pdf(dados):
    reader = PdfReader("ficha_ordem.pdf")
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        dados
    )

    try:
        nome = dados["untitled1"]
        caminho = f"{nome}.pdf"

        os.makedirs("pdfs", exist_ok=True)

        with open(f"pdfs/{caminho}", "wb") as f:
            writer.write(f)

        print("PDF gerado com sucesso!")
    except Exception as e:
        print(f"PDF não foi gerado, erro: {e}")
