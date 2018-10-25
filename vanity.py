from bit import Key, PrivateKeyTestnet

key_address = ""
while "HSBC" not in key_address:
    key = PrivateKeyTestnet()
    key_hex = key.to_hex()
    key_wif = key.to_wif()
    key_address = key.address
    print("key_address: ", key_address)

print("\n------------------------------\n")
print("key_hex: ", key_hex)
print("key_wif: ", key_wif)
print("key_address: ", key_address)
print("\n------------------------------\n")
