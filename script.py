from argparse import ArgumentParser
import os
def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name')
	parser.add_argument('-o', '--output', default='output')
	parser.add_argument('-d', '--database', default='database')

	args = parser.parse_args()
	print(args)
	#writing the output path to a tmp file for website to read
	with open('/tmp/wifeyePath.txt', 'w') as f:
		f.write(os.path.abspath(args.output))

main()
