from scapy.all import *
from colorama import Fore, Style, init
from datetime import datetime

# Initialize colors
init(autoreset=True)

# Enable pcap mode
conf.use_pcap = True

# Show interfaces
print(Fore.YELLOW + "\n[+] Available Interfaces:\n")
show_interfaces()

# User input
iface = input(Fore.CYAN + "\nEnter interface name: ")

print(Fore.GREEN + f"\n[+] Sniffing on {iface}...\n")

# Packet counter
packet_count = 0

# Header
print(
    Fore.WHITE + Style.BRIGHT +
    f"{'No':<6}{'Time':<15}{'Source IP':<20}"
    f"{'Destination IP':<20}{'Proto':<10}{'Length':<10}"
)

print("-" * 90)


def process_packet(packet):
    global packet_count

    packet_count += 1

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        proto = "OTHER"
        color = Fore.WHITE

        if packet.haslayer(TCP):
            proto = "TCP"
            color = Fore.GREEN

        elif packet.haslayer(UDP):
            proto = "UDP"
            color = Fore.CYAN

        elif packet.haslayer(ICMP):
            proto = "ICMP"
            color = Fore.YELLOW

        length = len(packet)

        current_time = datetime.now().strftime("%H:%M:%S")

        print(
            color +
            f"{packet_count:<6}"
            f"{current_time:<15}"
            f"{src_ip:<20}"
            f"{dst_ip:<20}"
            f"{proto:<10}"
            f"{length:<10}"
        )

        # Show payload preview
        try:
            raw_data = bytes(packet.payload)
            payload = raw_data.decode(errors="ignore")

            if payload.strip():
                print(Fore.MAGENTA + "Payload Preview:")
                print(payload[:120])

        except:
            pass

        print(Fore.WHITE + "-" * 90)


# Start sniffing
sniff(
    iface=iface,
    prn=process_packet,
    store=False
)