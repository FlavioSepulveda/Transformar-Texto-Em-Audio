# Transformando Texto em Audio
from PyPDF2 import PdfReader
from gtts import gTTS

# Função que converte PDF em Audio:
def pdf_to_audio(pdf):
    # Abrindo o arquivo -
    reader = PdfReader(pdf)
    text_total = ''
    
    # Extraindo os textos de cada pagina -
    for pages in reader.pages:
        text_total += pages.extract_text() + ' '
        
    # Convertendo texto para audio
    tts = gTTS(text=text_total, lang='pt')
    tts.save('Audio.mp3')
    
if __name__=='__main__':
    path_pdf = 'Caminho do Arquivo.'
    pdf_to_audio(path_pdf)