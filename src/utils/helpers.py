from PIL import Image
from io import BytesIO

def resize_image(image_content, size=(300, 300)):
    image = Image.open(BytesIO(image_content))
    return image.resize(size)
