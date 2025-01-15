import sys

from PIL import Image

if len(sys.argv) != 3:
    sys.exit("usage: costumes.py <image1.gif> <image2.gif>.")

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)