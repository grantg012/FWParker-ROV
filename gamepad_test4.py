import hid

vid = 0x0110	# Change it for your device
pid = 0x0001	# Change it for your device

with hid.Device(vid, pid) as h:
	print(f'Device manufacturer: {h.manufacturer}')
	print(f'Product: {h.product}')
	print(f'Serial Number: {h.serial}')
