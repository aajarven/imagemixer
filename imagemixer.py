import numpy as np
from scipy import misc
from optparse import OptionParser

if __name__ == "__main__":
	parser = OptionParser()
	(options, args) = parser.parse_args()

	if len(args) < 3:
		print("You must provide two input files and an output location, e.g." +
		"\npython imagemixer.py inPic1.png inPic2.png output.png")
		exit()
	
	infile1 = args[0]
	infile2 = args[1]
	outfile = args[2]

	img1 = misc.imread(infile1)
	img2 = misc.imread(infile2)

	if img1.shape != img2.shape:
		print("The images must have same dimensions. The dimensions of the" + 
		" given images were:")
		print(infile1 + ": " + str(img1.shape[1]) + " x " + str(img1.shape[0]))
		print(infile2 + ": " + str(img2.shape[1]) + " x " + str(img2.shape[0]))
		exit()
	else:
		new_image = np.empty([img1.shape[0]*2, img1.shape[1], 3])
		for col_index in range(0, len(img1)):
			new_image[col_index*2] = img1[col_index]
			new_image[col_index*2 + 1] = img2[col_index]
		misc.imsave(outfile, new_image)
