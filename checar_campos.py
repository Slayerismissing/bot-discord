from pypdf import PdfReader

reader = PdfReader("bot_discord/heroi_foda.pdf")
fields = reader.get_fields()

for name, field in fields.items():
    print(name, "=>", field.get("/V"))