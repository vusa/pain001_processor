import pika
from pathlib import Path
from pain001.pain_001_001_11 import Document
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
import logging
import random
import datetime

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

pain_string = Path("pain001-sample.xml").read_text()
parser = XmlParser()
pain001_doc = parser.from_string(pain_string, Document)

log.info(f"Got message pain001 with msg_id = {pain001_doc.cstmr_cdt_trf_initn.grp_hdr.msg_id}")

serializer_config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(config=serializer_config)

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.68.121'))
channel = connection.channel()


now = datetime.datetime.now()
date_str = now.strftime("%Y%m%d")

for i in range(2000):
    msg_id = f"{random.choice(['M','R', 'F'])}/{date_str}/{random.randrange(10111111, 98999999)}"
    log.info(f"Generated message id {msg_id}")
    pain001_doc.cstmr_cdt_trf_initn.grp_hdr.msg_id = msg_id
    pain001_doc_str = serializer.render(pain001_doc, ns_map={None:"urn:iso:std:iso:20022:tech:xsd:pain.001.001.11"})
    log.info(pain001_doc_str)
    channel.basic_publish(exchange='',
                      routing_key='dev.queue.1',
                      body=pain001_doc_str)
    log.info(f"Msg [{msg_id}] sent to queue")

connection.close()

'''
queue_manager = pymqi.connect('QM.1', 'SVRCONN.CHANNEL.1', '192.168.68.121(1434)')

q = pymqi.Queue(queue_manager, 'TESTQ.1')
msg = q.get()
print('Here is the message:', msg)
'''