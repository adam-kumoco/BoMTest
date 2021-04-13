from Crypto.Cipher import AES
import binascii
import time
import calendar
import codecs
from base64 import b64decode,b64encode
from datetime import datetime
import time
import calendar

tid = calendar.timegm(time.gmtime())


bommsg = 'hello world'
# Order status
# bommsg = '{"order_no": "1618314913"}'

# Order Lookup
# bommsg = '{"order_no": "1618314913", "page_number": 1}'

# SI Charge
# bommsg = '{"si_sub_ref_no": "SI2110310001135", "si_mer_charge_ref_no": "1618320467", "si_currency": "OMR", "si_amount": "1.000"}'
# bommsg = '{"si_sub_ref_no": "SI2110310001135", "si_mer_charge_ref_no": "%s", "si_currency": "OMR", "si_amount": "1.000", "order_tid": "%s""}' % (tid, tid, tid)

# Refund
# bommsg = '{"reference_no": "302000008556", "refund_amount": "1.000", "refund_ref_no": "%s"}' % tid

# Cancel
# bommsg = '{"reference_no": "302000008557", "refund_amount": "1.000"}'

bommsg_query = bommsg.encode('ascii')
print(bommsg_query)
# tid = datetime.now()
# bommsg['tid'] = str(tid)
# bommsg_query = urlencode(bommsg).encode('ascii')
# bom_code = {'access_code': 'AVCI00IC10AF30ICFA'}
# bom_code = 'AVCI00IC10AF30ICFA'
# bom_code = 'AVMG00IC10AF29GMFA'
# temp code
bom_code = 'AVTY00ID10AY51YTYA'

# bomaccess_code = urlencode(bom_code)
# bomkey = b'secretKey12345678998765432112345'
# bomkey = b'8613FE17684EB60B91D0E8C143775B57'
# bomkey = b'2A282204AA22E03E90F6909003A285E5'
# tempkey
bomkey = b'7DCBE6CA63923D25829AE77128280025'

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

