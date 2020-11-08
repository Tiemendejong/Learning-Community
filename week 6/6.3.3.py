from PIL import Image
def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

aaa = (change_contrast(Image.open('fruit_fade.png'), 100))
aaa.show()