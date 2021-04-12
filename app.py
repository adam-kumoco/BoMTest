from flask import Flask, render_template, redirect, url_for
from Crypto.Cipher import AES
import binascii
from datetime import datetime
import time
import calendar
from urllib.parse import urlencode
app = Flask(__name__)


@app.route('/')
def index():
    tid = calendar.timegm(time.gmtime())
    # bommsg = {'merchant_id': '26', 'order_id': '1234', 'currency': 'OMR', 'amount': '1.000', 'redirect_url': 'https://google.com', 'cancel_url': 'https://youtube.com', 'language': 'EN'}
    bommsg = 'tid=%s&merchant_id=26&order_id=%s&currency=OMR&amount=1.000&redirect_url=https://google.com&cancel_url=https://youtube.com&language=EN' % (tid, tid)
    bommsg_query = bommsg.encode('ascii')
    print(bommsg)
    # tid = datetime.now()
    # bommsg['tid'] = str(tid)
    # bommsg_query = urlencode(bommsg).encode('ascii')
    # bom_code = {'access_code': 'AVCI00IC10AF30ICFA'}
    bom_code = 'AVMG00IC10AF29GMFA'
    # bomaccess_code = urlencode(bom_code)
    bomkey = b'2A282204AA22E03E90F6909003A285E5'
    bomcipher = AES.new(bomkey, AES.MODE_GCM)
    bomenctext, bomtag = bomcipher.encrypt_and_digest(bommsg_query)
    bomnonce = bomcipher.nonce
    bommsg_enc = (binascii.hexlify(bomnonce) + binascii.hexlify(bomenctext) + binascii.hexlify(bomtag)).decode('ascii')
    return render_template('form.html', bommsg_query=bommsg_enc, bomaccess_code=bom_code, bomraw=bommsg_query)



if __name__ == '__main__':
    app.run()
