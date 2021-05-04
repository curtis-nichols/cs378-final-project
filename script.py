from argparse import ArgumentParser
import shutil
import os
def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name')
	parser.add_argument('-o', '--output', default='output')
	parser.add_argument('-d', '--database', default='database')

	args = parser.parse_args()
	print(args)
	input("Press Enter to continue...")
	shutil.copy('/var/www/html/wifeyeData.txt', os.path.abspath(args.output))
main()
