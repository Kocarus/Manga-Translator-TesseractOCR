import argparse

import cv2
from PIL import Image

import locate_bubbles
import translate
import typeset


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("img")
    parser.add_argument("out")
    args = parser.parse_args()

    img = cv2.imread(args.img)
    blurbs = locate_bubbles.get_blurbs(img)
    to_typeset = Image.fromarray(img.copy())

    for blurb in blurbs:
        translated = translate.translate_blurb(blurb)
#        translated = blurb
        typeset.typeset_blurb(to_typeset, translated)

    to_typeset.save(args.out)

if __name__ == "__main__":
    main()
