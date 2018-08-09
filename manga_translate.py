import os

import cv2
from PIL import Image

import locate_bubbles
import translate
import typeset


def main():

    imgPath = 'img'
    transPath = 'translated'

    images  = load_images_from_folder(imgPath)
    print ('Processing images:')
    names = load_names_from_folder(imgPath)
    print ('JAPANESE' + ' ' + '->' + ' ' + 'VIETNAMESE')

    transImg = []
    i = 0

    for img in images:
            blurbs = locate_bubbles.get_blurbs(img)
            needTransImg = Image.fromarray(img.copy())

            for blurb in blurbs:
                translated = translate.translate_blurb(blurb)
                typeset.typeset_blurb(needTransImg, translated)

            transImg.append(needTransImg)

    for trans in transImg:
            saveFile = os.path.join(transPath, names[i])
            trans.save(saveFile)
            i = i + 1

    print ('Statistic:')
    print transImg
    print ('Number of translated pages:' + str(i))


def load_images_from_folder(folder):
    images = []

    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)

    return images


def load_names_from_folder(folder):
    names = []

    for filename in os.listdir(folder):
        if filename is not None:
            names.append(filename)
            print filename

    return names


if __name__ == "__main__":
    main()
