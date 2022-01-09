from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCrypt():
    def encrypt(text, key, BLOCK_SIZE=32) -> bytes:
        key = bytes(key, 'utf-8')
        cipher = AES.new(key, AES.MODE_ECB)
        cipherText = cipher.encrypt(pad(bytes(text, 'utf-8'), BLOCK_SIZE))
        return cipherText


    def decrypt(cipherText, key, BLOCK_SIZE=32) -> str:
        key = bytes(key, 'utf-8')
        decipher = AES.new(key, AES.MODE_ECB)
        try:
            text = unpad(decipher.decrypt(cipherText), BLOCK_SIZE)
        except:
            return None
        return str(text.decode('utf-8'))
