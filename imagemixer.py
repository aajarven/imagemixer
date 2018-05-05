import numpy as np
from scipy import misc
from optparse import OptionParser

if __name__ == "__main__":
	parser = OptionParser(usage="python [options] imagemixer.py infile1.png infile2.png"
					   + " outfile.png")
	parser.add_option("-c", "--column", dest="swap_columns", default=False,
				   action="store_true", help="Mix images column by column")
	parser.add_option("-r", "--row", dest="swap_rows", default=False,
				   action="store_true", help="Mix images row by row")
	(opts, args) = parser.parse_args()

	if len(args) < 3:
		print("\nYou must provide two input files and an output location\n")
		parser.print_help()
		exit()
	
	infile1 = args[0]
	infile2 = args[1]
	outfile = args[2]

	img1 = misc.imread(infile1)
	img2 = misc.imread(infile2)

	if img1.shape != img2.shape:
		print("\nThe images must have same dimensions. The dimensions of the" + 
		" given images were:")
		print(infile1 + ": " + str(img1.shape[1]) + " x " + str(img1.shape[0]))
		print(infile2 + ": " + str(img2.shape[1]) + " x " + str(img2.shape[0]))
		print()
		parser.print_help()
		exit()
	else:
		
		if not opts.swap_columns:
			new_image = np.empty([img1.shape[0]*2, img1.shape[1], 3])
			for row_index in range(0, len(img1)):
				new_image[row_index*2] = img1[row_index]
				new_image[row_index*2 + 1] = img2[row_index]
		elif not opts.swap_rows:
			new_image = np.empty([img1.shape[0], img1.shape[1]*2, 3])
			for col_index in range(0, img1.shape[1]):
				new_image[:, col_index*2] = img1[:, col_index]
				new_image[:, col_index*2 + 1] = img2[:, col_index]
		else:
			print("\nCannot use both row and column modes\n")
			parser.print_help()
			exit()

		misc.imsave(outfile, new_image)
