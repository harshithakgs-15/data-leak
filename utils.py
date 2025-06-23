from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
import os

def watermark_pdf(path, watermark_text):
    reader = PdfReader(path)
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_text(
            watermark_text,  # not a real method—simulate watermark logic here or use external lib
            10, 10
        )
        writer.add_page(page)
    
    output_path = f'temp/{os.path.basename(path)}'
    with open(output_path, 'wb') as f:
        writer.write(f)
    
    return output_path

def log_access(email, ip):
    with open("access_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {email} from {ip}\n")
