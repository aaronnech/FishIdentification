import os
import sys
import glob

import dlib
from skimage import io
from skimage import transform

if len(sys.argv) < 2:
    print(
        "Give the path to the examples/faces directory as the argument to this "
        "program. For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./filter.py ../examples/faces")
    exit()
folder = sys.argv[1]

detector = dlib.simple_object_detector("detector.svm")

onlyFiles = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

for f in onlyFiles:
    print("Processing file: {}".format(f))
    try:
        img = io.imread(f)
        dets = detector(img)
        if len(dets) < 1:
            print 'Nothing found.. trying to flip..'
            flipTransform = transform.SimilarityTransform(scale=[-1.0, 1.0])
            imgFlipped = transform.warp(img, flipTransform)
            dets = detector(imgFlipped)

            if len(dets) < 1:
                print 'Nothing found again. Deleting..'
                os.remove(f)
    except:
        print 'Error! Deleting..'
        os.remove(f)