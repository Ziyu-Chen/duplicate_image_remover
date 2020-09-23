import requests
from PIL import Image
from choose_headers_randomly import choose_headers_randomly


def simplify_image_url(image_url):
    if '.jpg' in image_url:
        jpg_position = image_url.find('.jpg')
        return image_url[:jpg_position+4]
    if '.png' in image_url:
        png_position = image_url.find('.png')
        return image_url[:png_position+4]
    return image_url


def download_image(image_url, file_path):
    # Save the image
    image_url = simplify_image_url(image_url)
    response = requests.get(image_url, stream=True, headers=choose_headers_randomly())
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            f.write(response.content)
    # Convert the image if its type is webp.
    if file_path.endswith('.webp'):
        img = Image.open(file_path).convert('RGB')
        file_path = file_path.replace('.webp', '.jpg')
        img.save(file_path, 'jpeg')
