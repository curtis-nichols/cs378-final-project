from argparse import ArgumentParser

def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name')
	parser.add_argument('-o', '--output', default='output')
	parser.add_argument('-d', '--database', default='database')

	args = parser.parse_args()
	print(args)

main()
