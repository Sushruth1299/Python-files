from PIL import Image

def show(url):
    image = Image.open(url)
    image.show()
    