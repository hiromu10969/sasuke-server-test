from PIL import Image
import os

for f in os.listdir("."):

    if f.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):

        img = Image.open(f)

        print(
            f,
            img.width,
            img.height
        )