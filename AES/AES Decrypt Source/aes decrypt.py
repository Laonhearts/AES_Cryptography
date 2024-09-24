from Crypto.Cipher import AES

cipher = ''

key = 
key str(key)

while len(key) <32:
    key = '0' + key

c = AES.new(key, AES.MODE_ECB)

result = c.decrypt(cipher)

print(result)
