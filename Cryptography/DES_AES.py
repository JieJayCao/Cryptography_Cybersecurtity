"""AES加密"""
import Crypto.Cipher.AES
import Crypto.Random
import base64
import binascii
import Crypto.Cipher.DES3


def auto_fill(x):
    if len(x) <= 32:
        while len(x) not in [16, 24, 32]:
            x += " "

        return x.encode()
    else:
        raise ("密钥长度不能大于32位！")

key = "cjnb"
content = "caojie03163124"

#ECB模式AES加密
x = Crypto.Cipher.AES.new(auto_fill(key), Crypto.Cipher.AES.MODE_ECB)
#字符串二进制编码
a = base64.encodebytes(x.encrypt(auto_fill(content)))
b = x.decrypt(base64.decodebytes(a))

print("AES加密密文：",a)
print("AES解密明文：",b)


"""DES加密"""


def auto_fill(x):
    if len(x) > 24:
        raise ("密钥长度不能大于等于24位！")
    else:
        while len(x) < 16:
            x += " "
        return x.encode()


y = Crypto.Cipher.DES3.new(auto_fill(key), Crypto.Cipher.DES3.MODE_ECB)

c = binascii.b2a_base64(y.encrypt(auto_fill(content)))
d = y.decrypt(binascii.a2b_base64(c))

print("DES加密密文：", c)
print("DES解密明文：", d)

