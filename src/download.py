import requests
import os

output_dir = 'data'
filename = 'pages_export.xml'

def download_pages() -> None:
    """Acquires the Minecraft Wiki XML document from our stable copy on Google Drive."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    google_drive_id = '1B7yYd3CJ-thCR0Vz20ntrO22O-XdSwGM'
    at = 'AENtkXbaW7tsgo45QPe6aOtgqDIk:1730764628760'
    uuid = 'b5aedbda-6d22-42aa-aeaa-2b228137cfd9'
    url = f"https://drive.usercontent.google.com/download?id={google_drive_id}&export=download&authuser=0&confirm=t&uuid={uuid}&at={at}"
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(f'{output_dir}/{filename}', 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk: # filter out keep-alive chunks
                    file.write(chunk)
        
        print(f'Downloaded to {output_dir}/{filename}')
    else:
        print(f'Download request failed: {response.status_code}')


if __name__ == '__main__':
    download_pages()