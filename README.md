# cs378-final-project
cs378-final-project

# Prereqs

-running in kali as root

-wlan0 interface with nl80211 driver (such as ALFA card)

-apt-get install hostapd dnsmasq


# for capturing packets, 
we can do 
- sudo tcpdump -D : find available interfaces for capture
- sudo tcpdump --interface $interface -w output.pcap

Let me know if we need to filter anything
