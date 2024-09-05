# easy_crypt
def easy_crypt(text):
  print(''.join(chr((ord(x) - ord('0') + 44) % (ord('}') - ord('0') + 1) + ord('0')) for x in text))
