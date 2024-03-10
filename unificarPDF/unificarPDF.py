import streamlit as st
import pyPDF2


def merge_pdfs(output_path, pdf_documents):
    pdf_merger = pyPDF2.PdfMerger()

    for pdf_documents in pdf_documents:
      
        pdf_merger.append(pdf_documents)

    with open(output_path, 'ub') as output_file:
        pdf_merger.write(output_file)

    




def main():
    st.image('assets/pdf.png')
    st.header('Fusion de PDF')
    st.subheader('Adjunte archivos PDF para combinar')

    attached_pdfs = st.file_uploader(label='', accept_multiple_files=True)

    merge_button = st.button(label='Fusionar archivos PDF')

    if merge_button:

        if len(attached_pdfs <= 1):
            st.warning('Ajunta más de un archivo PDF, para fusionarlos')
        else:
            output_pdf = 'assets/PDF-fu-fin.pdf'
            merge_pdfs(output_pdf, attached_pdfs)
            st.success('Los archivos se han fucionado correctamente')

            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label='Descargar PDF fusionado', data=pdf_data, file_name='PDF-fu-fin.pdf')

if __name__ =='__main__':

    main()
