def encrypt(str):
  arr = []
  str = cesarEncrypt(str)
  
  for char in str:
    arr.append(hex(ord(char))[2:])
  
  return cesarEncrypt(''.join(arr))

def decrypt(str):
  arr = []
  str = cesarDecrypt(str)
  
  for i in range(0, len(str), 2):
    arr.append(chr(int(str[i:i+2], 16)))
  
  return cesarDecrypt(''.join(arr))
  
def cesarEncrypt(str):
  resultat = ""
  gap = 15

  for char in str:
    if char.isalpha():
      # Décalage uniquement pour les lettres de l'alphabet
      newChar = (ord(char) + gap - ord('A')) % 26 + ord('A') if char.isupper() else (ord(char) + gap - ord('a')) % 26 + ord('a')
      resultat += chr(newChar)
    else:
      # Ne pas décaler les caractères non alphabétiques
      resultat += char

  return resultat

def cesarDecrypt(str):
  resultat = ""
  gap = 15

  for char in str:
    if char.isalpha():
      # Décalage uniquement pour les lettres de l'alphabet
      newChar = (ord(char) - gap - ord('A')) % 26 + ord('A') if char.isupper() else (ord(char) - gap - ord('a')) % 26 + ord('a')
      resultat += chr(newChar)
    else:
      # Ne pas décaler les caractères non alphabétiques
      resultat += char

  return resultat