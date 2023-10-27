from fpdf import FPDF
from pathlib import Path
import glob

filepaths = glob.glob("Text_Files/*.txt*")

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # extract filename
    filename = Path(filepath).stem
    pfd_file_name = filename.split()[0].capitalize()
    
    # write the name as header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=12, txt=f"{pfd_file_name}", align="L", ln=1)
    # pdf.line(0,20,250,20)
    
    # read the file and write into pdf file 
    with open(filepath, '+r') as file:
        content = file.read()
    
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(w=0, h=7, txt=content)

    # output the pdf file
    pdf.output(f"pdf_files/{pfd_file_name}.pdf")

    
