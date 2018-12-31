import music
import numpy
from scipy.io.wavfile import read

def main(args):
	"""
	Synthesize a note and covert to mono WAV file based on input sound, 
	frequency, and duration.

	Parameters
	----------
	args : array
		Array of command line arguments containing filename, input sound
		wav file, frequency, duration, and output filename.

	See Also
	--------
	In music library, functions.py -> N() and W() used
	"""
	inputSound = read(args[1])
	inputFreq = int(args[2])
	inputDuration = int(args[3])
	outputFile = args[4]


	#Convert the list of numpy-arrays into a 1D array (column-wise)
	frames = numpy.array(inputSound[1], dtype=float)
	inputTab = numpy.hstack(frames)

	note = music.functions.N(f=inputFreq, d=inputDuration, tab=inputTab)
	music.functions.W(note, filename=outputFile)


if __name__ == "__main__":
	import sys
	main(sys.argv)