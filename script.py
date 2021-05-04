from argparse import ArgumentParser
from pwparser import search
import shutil
import os
def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name')
	parser.add_argument('-o', '--output', default='output.txt')
	parser.add_argument('-d', '--database') #default does reads from different kind of file

	args = parser.parse_args()
	print(args)
	input("Press Enter to continue...")
	shutil.copy('/var/www/html/wifeyeData.txt', os.path.abspath(args.output))
	#search(args, [username, password])
main()
