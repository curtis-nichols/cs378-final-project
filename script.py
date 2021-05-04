from argparse import ArgumentParser
from pwparser import search, read_cp_output_lines
import shutil
import os
def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name')
	parser.add_argument('-o', '--output', default='output')
	parser.add_argument('-d', '--database') #default reads from different kind of file

	args = parser.parse_args()
	print(args)
	input("Press Enter to continue...")
	shutil.copy('/var/www/html/wifeyeData.txt', os.path.abspath(args.output))

	users = read_cp_output_lines(os.path.abspath(args.output))
	for user in users:
		info = user.split()
		print("considering user, password pair: " + info[1] + ", " + info[2])
		search(args, [info[1],info[2]])
	print("Done!")
main()
