# Encrypt password
caesarMove = 2
def encrypt(password):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listChars = list(chars)

  listPassword = list(password)

  for i in range(len(listPassword)):
    indexChar = listChars.index(listPassword[i])
    changeChar = (indexChar + caesarMove) % len(chars)
    listPassword[i] = listChars[changeChar]
  return "".join(listPassword)


# Decrypt password
def decrypt(password):
  chars = "abcdefghijklmnopqrstuvwxyz0123456789"
  listChars = list(chars)

  listPassword = list(password)

  for i in range(len(listPassword)):
    indexChar = listChars.index(listPassword[i])
    changeChar = (indexChar - caesarMove) % len(chars)
    listPassword[i] = listChars[changeChar]
  return "".join(listPassword)