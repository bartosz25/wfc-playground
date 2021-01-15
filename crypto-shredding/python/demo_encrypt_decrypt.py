import base64
from Crypto.Cipher import AES



def pad(input: str) -> str:
    required_input_length_multiple = 16
    return input + (required_input_length_multiple - len(input) % required_input_length_multiple) * \
           chr(required_input_length_multiple - len(input) % required_input_length_multiple)


def unpad(input: str) -> str:
    return input[0:-ord(input[-1])]


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        raw = cipher.encrypt(raw)
        encrypt_val = base64.b64encode(raw)
        return encrypt_val

    def decrypt(self, raw):
        raw = base64.b64decode(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        raw = cipher.decrypt(raw)
        raw = unpad(raw.decode("UTF-8"))
        return raw


if __name__ == '__main__':
    key = 'userkey1userkey1'
    birth_date = '20.01.1980'
    encryptor = AESCipher(key)
    encrypted_birth_date = encryptor.encrypt(birth_date)
    print(f'Encrypted base64={encrypted_birth_date.decode("UTF-8")}')
    print(f'Decrypted base64={encryptor.decrypt(encrypted_birth_date)}')
    encrypted_birth_date = "YUA+4n6qUK4QaoNt6AbL3g=="
    print(f'Decrypted base64 from Java={encryptor.decrypt(encrypted_birth_date)}')
