from download_images import download_images
from remove_duplicate_images import remove_duplicate_images


def main():
    csv_path = '/Users/Ziyu/OneDrive - Clarivate Analytics/Desktop/panasonic/trimmers.csv'
    directory_path = '/Users/Ziyu/OneDrive - Clarivate Analytics/Desktop/panasonic/trimmer_images/'
    image_url_column = 'Thumbnail'
    file_name_columns = ['Product', 'Indicator Code', 'Item ID']
    # download_images(csv_path, directory_path, image_url_column, file_name_columns)
    remove_duplicate_images(directory_path)

if __name__ == '__main__':
    main()