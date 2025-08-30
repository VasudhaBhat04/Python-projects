import imageio.v3 as iio

filenames = ['duck1.jpeg', 'duck2.jpeg'] #same size images are expected
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('duck.gif', images, duration = 500, loop = 0)
