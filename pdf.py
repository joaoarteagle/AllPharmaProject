import win32com.client


def excel_to_pdf(arquivo_excel, arquivo_pdf):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    wb = excel.Workbooks.Open(arquivo_excel)
    ws = wb.Worksheets[0]

    wb.ExportAsFixedFormat(0, arquivo_pdf)
    wb.Close(SaveChanges=False)
    excel.Quit()



excel_to_pdf("backups_allpharma.xlsx", "teste.pdf")