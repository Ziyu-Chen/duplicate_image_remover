import pandas as pd
import requests
from download_image import download_image


def download_images(csv_path, directory_path, image_url_column, file_name_columns):
    data = pd.read_csv(csv_path)
    for i in range(len(data)):
        image_url = data.iloc[i][image_url_column]
        if type(image_url) == str:
            try:
                file_name = '-'.join([str(data.iloc[i][file_name_column]) for file_name_column in file_name_columns]) + '.jpg'
                file_path = directory_path + file_name
                download_image(image_url, file_path)
                print('Finished downloading No. %d' % i)
            except Exception as e:
                print(e)

