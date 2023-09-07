from PyPDF2 import PdfReader
from fpdf import FPDF
from io import BytesIO


def txt2pdf(txt_content: str, output_pdf_path: str) -> None:

    """
    Convert a txt file to pdf file.

    Parameters
    ----------
    txt_content : str
        content of txt file

    output_pdf_path : str
        path to save the pdf file

    Returns
    -------
    None
    """

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 10, txt_content)
    name_pdf = output_pdf_path.split(".")[0] + ".pdf"
    pdf.output(name_pdf)

    return None


def get_text_from_pdf(pdf):

    """
    Take the text from a pdf file

    Parameters
    ----------
    pdf : str
        path to the pdf file

    Returns
    -------
    text : str
        text from pdf
    """

    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text
