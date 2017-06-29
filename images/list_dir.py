import os
import argparse
from PIL import Image
from resizeimage import resizeimage

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--inputdir',
  action="store", dest="inputdir",
  help="inputdir to be parsed")
parser.add_argument('-o', '--outputdir',
  action="store", dest="outputdir",
  help="outputdir where to store thumbnails")
parser.add_argument('-w', '--width',
  help="resize to width", default=200, type=int)

opts = parser.parse_args()

# path = os.path.dirname(os.path.realpath(__file__)) + '\\'

for filename in os.listdir( opts.inputdir):
    # print( opts.inputdir + '\\' + filename)
    image = Image.open(os.path.join(opts.inputdir ,filename))

    # print(image)
    name, ext = os.path.splitext(os.path.join(opts.inputdir, filename))
    print (name,ext)
    if image.size[0] > opts.width:
        image_small = resizeimage.resize_width(image, opts.width)
        image_small.save(name + '_small' + ext, image_small.format)
        image_small.close()
    image.close()
