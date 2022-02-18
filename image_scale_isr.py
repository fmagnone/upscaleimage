import numpy as np
from PIL import Image
from ISR.models import RDN

inputPath = 'images/duck.png'
outputPath = 'images/duck_up.png'

imagePil = Image.open(inputPath)
imageNumpy = np.array(imagePil)

model = RDN(weights='noise-cancel')
scaledNumpy = model.predict(imageNumpy)
scaledPil = Image.fromarray(scaledNumpy)

scaledPil.save(outputPath)
