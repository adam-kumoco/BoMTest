from Crypto.Cipher import AES
import binascii
import codecs
from base64 import b64decode,b64encode
from datetime import datetime
import time
import calendar

bommsg = '{"order_id": "1618228330"}'
bommsg_query = bommsg.encode('ascii')
print(bommsg_query)
# tid = datetime.now()
# bommsg['tid'] = str(tid)
# bommsg_query = urlencode(bommsg).encode('ascii')
# bom_code = {'access_code': 'AVCI00IC10AF30ICFA'}
# bom_code = 'AVCI00IC10AF30ICFA'
bom_code = 'AVMG00IC10AF29GMFA'
# bomaccess_code = urlencode(bom_code)
# bomkey = b'secretKey12345678998765432112345'
bomkey = b'8613FE17684EB60B91D0E8C143775B57'
bomkey = b'2A282204AA22E03E90F6909003A285E5'
# bomcipher = AES.new(bomkey, AES.MODE_GCM, nonce=b'd99c56fd684cb7ca1a3cd2c73037482c')
bomcipher = AES.new(bomkey, AES.MODE_GCM)
bomenctext, bomtag = bomcipher.encrypt_and_digest(bommsg_query)
bomnonce = bomcipher.nonce
bommsg_enc = (binascii.hexlify(bomnonce) + binascii.hexlify(bomenctext) + binascii.hexlify(bomtag)).decode('ascii')
# bommsg_enc = (bomnonce + binascii.hexlify(bomenctext) + binascii.hexlify(bomtag)).decode('ascii')
print(binascii.hexlify(bomnonce))
print(bomkey)
print(binascii.hexlify(bomenctext))
print(binascii.hexlify(bomenctext+bomtag))
print(binascii.hexlify(bomtag))
print(bommsg_enc)

# iv = b"7b5d0d5d50b417ceb868f645827b9bbe"
# encmsg = b"7609abd59ebbea007230c1f639bbba3d443de1cc2d1aad5523ab94f47a9939144031a314225a7683ff05b8a505486635ffad2a51375298c5566d3951281993ee1b4486d4c08c0c97557001aca283d745400a724f37c0f54be6bc05d6e8613fcfe4779ac7867166c4dc6f400ec5445036ae1624534f2d9824e65105d6921b78ef7caafbf39befbbeffe042434c095d935c6df28a2b20f0863f1dc0066dc862839bb7321eee9cbaf02f9768ca5916722ac0a5ec52d44bce19e8c25cf1883669484f9ffbf48668b29868955d074cea37a9eadeb2f53bfd7cd6e7bf16354dec0dbceba27571e8aed611be697cceca9f11b7af7878bf2d64259f2af6ab82706c396bd761a5c999a2f97a66f21fabf5885e65d4f446712f9ec14abda9ac70a6ff127a5d6d68de192de16e6e991cbfc93508d8913e6703cb2a742715f5f9e5d00765385ff2ef9bf1548424abfd6614a1e2b3d300584d62b18524baa1f521f1db86bd157613e9963bce6f8c6ff4996fe26e31d26ed6bf105e4886c11db0153063f434f743e63d817876868a5c5cffdfdef1961ead3c9335b1acb16dde68acb723e8e7043d840710f4aead7b28707fa2edc1f368751d2464ab480e80be6e6c55b6c3d24da7a1a00a491f120f70dbcb07647eb6237d13c78e3cb00814646dd67c5a0638ccbb340e9ac44ab6b648cc754c766961c7a8a1942e8497aa111204016d7ff5e3154dbef3cc5ee6a42a96094bbc2810960867dc7b731930aa6f0db9b8459156f9ef004005a237941cdae2db07864ec826d0ef1694cd0b77c5da196d5b7d51b141958c923ef76751e6182efcbd2f67c29e05dd8e1634945f5bc001e5c8b886af75d0e8521fe55ecf502b2dd4e057dc5f182743ec979ef942d181341"
# omcipher = AES.new(bomkey, AES.MODE_GCM,nonce=iv)
# omcipher.encrypt_and_digest(encmsg)
print()
print('decrypt')
# bommsg = 'd99c56fd684cb7ca1a3cd2c73037482c18180bd323348fca7779d59f9e56f88e17c169537d617dd39d5179'
bommsg = bommsg_enc
bom_nonce = bommsg[0:32].encode('ascii')
bom_auth = bommsg[-32:].encode('ascii')
# bom_nonce = bomnonce
# bom_auth = bomtag
print(bomnonce)
# bommsg_query = bommsg[32:-32].encode('ascii')
bommsg_query = bomenctext
print(bommsg_query)
bomkey = b'8613FE17684EB60B91D0E8C143775B57'
# bomkey = b'secretKey12345678998765432112345'
bomcipher = AES.new(bomkey, AES.MODE_GCM, nonce=bom_nonce)
# bomnonce = bomcipher.nonce
# print(binascii.hexlify(bomnonce))
bomdecctext = bomcipher.decrypt_and_verify(bommsg_query, bom_auth)
print(bomdecctext)
# print(binascii.b2a_base64(bomenctext))