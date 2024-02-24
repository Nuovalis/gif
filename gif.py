import imageio.v3 as iio

#Image locations
filenames = ['SonicBase.png', 'SonicBaseInverse.png']
images = [ ]

#for loop
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('sonic.gif', images, duration = 200, loop = 0)