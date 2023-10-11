from dotenv import load_dotenv
import os
from pyunpack import Archive
from mega import Mega
import requests

# Load the environment variables from .env
load_dotenv()
import os


rar_links="""https://42.download.real-debrid.com/d/GWV5SWTWK757O/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part02.rar
https://42.download.real-debrid.com/d/I34XTTFLKH4KU/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part04.rar
https://42.download.real-debrid.com/d/EG34T6VLMNRLI/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part06.rar
https://42.download.real-debrid.com/d/4BQUWEMQSEYQK/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part08.rar
https://42.download.real-debrid.com/d/4KU5BDNU3O5DG/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part10.rar
https://42.download.real-debrid.com/d/EHVKLSKXPFACY/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part12.rar
https://42.download.real-debrid.com/d/GZMU5PH24NNME/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part14.rar
https://42.download.real-debrid.com/d/JATOELDILX4ZK/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part16.rar
https://42.download.real-debrid.com/d/6KOQWIRCIC46A/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part18.rar
https://42.download.real-debrid.com/d/CYEV7SRWPGNQO/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part20.rar
https://42.download.real-debrid.com/d/H6X76KHCPQLWW/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part22.rar
https://42.download.real-debrid.com/d/VHQ4E4QWVNNZA/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part24.rar
https://42.download.real-debrid.com/d/KBUDNCZSM43CC/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part26.rar
https://42.download.real-debrid.com/d/C5S22EJA3EEGA/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part28.rar
https://42.download.real-debrid.com/d/KUGQ3LQNCWNDG/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part30.rar
https://42.download.real-debrid.com/d/QOSCW4ULFG57A/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part32.rar
https://42.download.real-debrid.com/d/UTB2M5HDBNNNK/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part01.rar
https://42.download.real-debrid.com/d/HJMKVORJRGM5K/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part03.rar
https://42.download.real-debrid.com/d/3VV5FSOEIB72G/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part05.rar
https://42.download.real-debrid.com/d/OTFOZGHNXVW7O/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part07.rar
https://42.download.real-debrid.com/d/7V5YZYUBO2R4K/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part09.rar
https://42.download.real-debrid.com/d/6V2QYPGZGYO4O/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part11.rar
https://42.download.real-debrid.com/d/5UGNCLKVWCB7Q/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part13.rar
https://42.download.real-debrid.com/d/TTIGQHLXX5Q24/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part15.rar
https://42.download.real-debrid.com/d/KTIPJDGKERYSK/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part17.rar
https://42.download.real-debrid.com/d/5GNAMVHODFRSW/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part19.rar
https://42.download.real-debrid.com/d/4IH3LEFRWJ3VA/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part21.rar
https://42.download.real-debrid.com/d/QDKTT7F2Q3IT6/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part23.rar
https://42.download.real-debrid.com/d/EWQXD2HCH4JOY/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part25.rar
https://42.download.real-debrid.com/d/HZTSRDXZYR23M/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part27.rar
https://42.download.real-debrid.com/d/5QP7I3NOXIT7A/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part29.rar
https://42.download.real-debrid.com/d/IPQSLLMSDQEDA/Stefan.Georgi.Justin.Goff.Copy.Accelerator.Virtual.Mastermind.02.19.part31.rar""".splitlines()



mega = Mega()

m = mega.login(os.getenv('user'), os.getenv("pass"))

details = m.get_user()

# Directory to save downloaded and extracted files
download_dir = "downloaded_files/"

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Loop through the RAR download links
for link in rar_links:
    # Download the RAR file (you may need to use a download manager or similar)
    # Extract the filename from the URL
    filename = link.split('/')[-1]
    # Set the path where you want to save the downloaded file
    download_path = os.path.join(download_dir, filename)

    # Download the RAR file
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

    # Unrar the downloaded file
    Archive(link).extractall(download_dir)

# Upload the extracted files to Mega
for root, dirs, files in os.walk(download_dir):
    for file in files:
        local_file_path = os.path.join(root, file)
        remote_path = f"/{os.path.relpath(local_file_path, download_dir)}"
        m.upload(local_file_path, remote_path)

# Clean up: delete the downloaded and extracted files
for root, dirs, files in os.walk(download_dir):
    for file in files:
        local_file_path = os.path.join(root, file)
        os.remove(local_file_path)

# Optionally, you can also delete the empty directories
for root, dirs, files in os.walk(download_dir, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if not os.listdir(dir_path):
            os.rmdir(dir_path)

# Clean up: delete the downloaded files
if os.path.exists(download_dir):
    os.rmdir(download_dir)

print("Files uploaded to Mega successfully.")