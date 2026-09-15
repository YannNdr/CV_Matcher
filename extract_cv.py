from pathlib import Path
from docx import Document
from pypdf import PdfReader

def extract_docx(cv,candidat):
    cv = "cv_examples/" + cv
    document = Document(cv)
    text = ""
    for elements in document.paragraphs:
        text += elements.text+"\n"
    return text


def extract_pdf(cv, candidat):

    reader = PdfReader('cv_examples/'+cv)
    text = ""
    for elements in reader.pages:
        text += elements.extract_text()+"\n"
    return text



def export_cv(file,candidat):

    if Path(file).suffix ==".docx":
        extracted_txt = extract_docx(file,candidat)
    else:
        extracted_txt = extract_pdf(file,candidat)

    with open(f"{candidat}_metadata.txt", "w", encoding="utf-8") as fichier:
        fichier.write(extracted_txt)

if __name__ == "__main__":
    print("File is exectuded directly")
    export_cv('cv-yann-ndour.pdf','yannNdour')