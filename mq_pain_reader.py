import pika, sys, os
from pain001.pain_001_001_11 import Document
from xsdata.formats.dataclass.parsers import XmlParser
import logging
import sqlite3


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

con = sqlite3.connect("messages.db")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.68.121'))
    channel = connection.channel()

    parser = XmlParser()
    def callback(ch, method, properties, body):
        log.debug(" [x] Received %r" % body)
        pain001_str = body.decode()
        pain001_doc = parser.from_string(pain001_str, Document)
        msg_id = pain001_doc.cstmr_cdt_trf_initn.grp_hdr.msg_id
        log.info(f"Received pain001 with msg_id = {msg_id}")
        cur = con.cursor()
        cur.execute(f"insert into pain001(msg_id, created_date, document) values ('{msg_id}', datetime(), '{pain001_str}')")
        con.commit()

    channel.basic_consume(queue='dev.queue.1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        cur = con.cursor()
        res = cur.execute("select count(*) from pain001")
        count = res.fetchone()
        print(f"{count} total records in table pain001")
        con.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)