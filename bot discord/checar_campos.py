from pypdf import PdfReader

from pypdf import PdfReader

reader = PdfReader("heroi_foda.pdf")
fields = reader.get_fields()

for name, field in fields.items():
    print(name, "=>", field.get("/V"))