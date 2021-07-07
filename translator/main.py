#
# 
#
from docx import Document
from docx.shared import Length, Pt, RGBColor
from googletrans import Translator
translator = Translator()

def translate(doc, dstLang):
    for p in doc.paragraphs:
        data = translator.translate(p.text,dest=dstLang)
        p.text = data.text
        for run in p.runs:
            data = translator.translate(run.text,dest=dstLang)
            run.text = data.text

document = Document('d:/璃ArtBook.docx')
translate(document, "en")

document.save('demo.docx')