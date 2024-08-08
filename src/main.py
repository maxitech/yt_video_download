import os
import sys
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError, VideoUnavailable

def download_video():
    try:
        save_path = input('Bitte geben Sie den Pfad an, in dem das Video gespeichert werden soll.\nTipp: Kopieren Sie den Pfad aus Ihrem Dateibrowser und fügen Sie ihn hier ein: ')
        save_path = save_path.strip('"')
        
        if not os.path.exists(save_path):
            print(f'Der angegebene Pfad "{save_path}" existiert nicht. Bitte überprüfen Sie den Pfad und versuchen Sie es erneut.')
            return 
        
        url = input('Geben Sie die YouTube-URL des Videos ein, das Sie herunterladen möchten: ')
        
        yt = YouTube(url, on_progress_callback=progress_func, on_complete_callback=complete_func)
        stream = yt.streams.get_highest_resolution()
        print(f'Starte den Download des Videos: "{yt.title}"...')
        stream.download(output_path=save_path)
        
    except RegexMatchError:
        print(f'Ungültige URL! Bitte überprüfen Sie die eingegebene URL und versuchen Sie es erneut.')
        
    except VideoUnavailable:
        print(f'Das Video "{url}" ist derzeit nicht verfügbar. Bitte versuchen Sie es mit einer anderen URL oder später erneut.')

    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")    

def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write(f'\rDownload-Fortschritt: {percentage_of_completion:.2f}%')
    sys.stdout.flush()

def complete_func(stream, file_path):
    print(f'\nDer Download wurde erfolgreich abgeschlossen! \nDie Datei wurde gespeichert unter: {file_path}')

# init
download_video()
