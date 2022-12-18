import app.config as config
import app.utils as utils
import fpdf


def switchExportType(fileType: str, data: list):
    match fileType:
        case 'TXT':
            exportTXT(data)
        case 'PDF':
            exportPDF(data)
        case 'HTML':
            exportHTML(data)
        case _:
            print('\nFile type not supported.')


def exportPDF(data: list):
    directory = f'{config.exportsPath}data_PDF.pdf'
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)
    colWidth = pdf.w / 4.5
    rowHeight = pdf.font_size
    def format(text): return pdf.cell(colWidth, rowHeight, txt=text, border=1)
    for row in data:
        for text in row:
            format(text)
        pdf.ln(rowHeight)
    pdf.output(directory)
    utils.logger(f'Generated PDF file, directory: {directory}')


def exportHTML(data: list):
    directory = f'{config.exportsPath}data_HTML.html'
    htmlPage = '<table><tbody>'
    for row in data:
        htmlPage += '<tr>'
        for text in row:
            htmlPage += f'<td>{text}</td>'
        htmlPage += '</tr>'
    htmlPage += '</table></tbody>'
    with open(directory, 'w') as htmlData:
        htmlData.write(htmlPage)
    utils.logger(f'Generated HTML file, directory: {directory}')


def exportTXT(data: list):
    directory = f'{config.exportsPath}data_TXT.txt'
    with open(directory, 'w') as txtData:
        for row in data:
            txtData.write(' '.join(text.ljust(17) for text in row) + '\n')
    utils.logger(f'Generated TXT file, directory: {directory}')
