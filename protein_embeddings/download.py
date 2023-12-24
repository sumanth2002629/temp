#script to download the data provided by Edward et al.
import gdown

url = "https://drive.google.com/drive/folders/1xNoA6dxkN4jzVNCg_7YNjdPZzl51Jo9M"
gdown.download_folder(url, quiet=True)