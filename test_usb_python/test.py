import hid

h = hid.device()
h.open(1155, 22352)
print("Manufacturer: %s" % h.get_manufacturer_string())
print("Product: %s" % h.get_product_string())
print("Serial No: %s" % h.get_serial_number_string())
h.set_nonblocking(1)
while True:
    d = h.read(64, 5000)
    if d:
        print(d)
    else:
        break