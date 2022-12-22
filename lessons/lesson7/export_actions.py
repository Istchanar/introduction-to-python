import data_actions
import utils
import fpdf

def data_and_path(file_name: str) -> dict:
    contacts = data_actions.get_all_contacts()
    directory = f'{utils.exports_path}{file_name}'
    utils.delete_file(directory)
    return {'contacts': contacts, 'directory': directory}


def export_PDF():
    data = data_and_path('data_PDF.pdf')

    pdf_file = fpdf.FPDF()
    pdf_file.add_page()
    pdf_file.set_font('helvetica', size=12)
    column_w = pdf_file.w / 4.5
    row_h = pdf_file.font_size
    
    def format(contact): return pdf_file.cell(column_w, row_h, txt = contact, border = 1)
    for row in data['contacts']:
        for text in row:
            format(text)
        pdf_file.ln(row_h)
    pdf_file.output(data['directory'])
    utils.logger('Generated PDF file, directory: {}'.format(data['directory']))


def export_HTML():
    data = data_and_path('data_HTML.html')

    html = '<table><tbody>'
    for row in data['contacts']:
        html += '<tr>'
        for text in row:
            html += f'<td>{text}</td>'
        html += '</tr>'
    html += '</table></tbody>'
    
    with open(data['directory'], 'w') as html_file:
        html_file.write(html)
    utils.logger('Generated HTML file, directory: {}'.format(data['directory']))


def export_TXT():
    data = data_and_path('data_TXT.txt') 
    with open(data['directory'], 'w') as txt_file:
        for row in data['contacts']:
            txt_file.write(' '.join(text.ljust(17) for text in row) + '\n')
    utils.logger('Generated TXT file, directory: {}'.format(data['directory']))
