"""
Script to convert output/SQE_A3_Submission_UmairHassan.docx to output/A3_24i-3137_UmairHassan.pdf
using native Microsoft Word COM automation.
"""

import os
import win32com.client

docx_path = os.path.abspath("output/SQE_A3_Submission_UmairHassan.docx")
pdf_path = os.path.abspath("output/A3_24i-3137_UmairHassan.pdf")

print(f"Converting DOCX: {docx_path}")
print(f"Target PDF: {pdf_path}")

word = win32com.client.Dispatch("Word.Application")
word.Visible = False

try:
    doc = word.Documents.Open(docx_path)
    # 17 represents wdExportFormatPDF in Word COM
    doc.SaveAs(pdf_path, FileFormat=17)
    doc.Close()
    print("PDF export completed successfully!")
except Exception as e:
    print(f"Export error: {e}")
    raise
finally:
    word.Quit()

if os.path.exists(pdf_path):
    size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
    print(f"PDF verified on disk. File size: {size_mb:.2f} MB")
