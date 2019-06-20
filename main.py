from PIL import Image
import glob
import time
import numpy
import blend_modes
import cv2

size = (1920,1080)

def lightenBlend(img, index):
    bg = Image.open("out/img_%04d" % (index - 1) +".jpg")

    # img = img.resize((size))
    # bg = bg.resize((size))

    bg = numpy.array(bg)
    img = numpy.array(img)

    output = []
    output = numpy.maximum(img[:, :, :3], bg[:, :, :3])
    img_out = Image.fromarray(output).convert('RGB')
    img_out.save("out/img_%04d" % index +".jpg")


def createVideo(folderName, outputName, fps):
    index = 0

    im = Image.open(glob.glob(folderName + '/*.jpg')[0])
    width, height = im.size
    writer = cv2.VideoWriter(outputName + ".mp4", cv2.VideoWriter_fourcc(*'x264'), fps , (width, height))

    for fl in sorted(glob.glob(folderName + '/*.jpg')): 
        img = cv2.imread(fl)
        img = cv2.resize(img, (width, height))
        index = index + 1
        writer.write(img) 
        print(index)

index = 0

im = Image.open(glob.glob('photos/*.jpg')[0])
width, height = im.size
im.convert('RGB').save("out/img_%04d" % index +".jpg")
index += 1

for filename in glob.glob('photos/*.jpg'): 
    im = Image.open(filename)
    lightenBlend(im, index)
    print(index)
    index = index + 1
createVideo("photos", "timelapse", 30)
createVideo("out", "starLines", 30)