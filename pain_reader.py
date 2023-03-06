from pathlib import Path
from pain001.pain_001_001_11 import Document
from xsdata.formats.dataclass.parsers import XmlParser
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

pain_string = Path("pain001-sample.xml").read_text()
parser = XmlParser()
pain001_doc = parser.from_string(pain_string, Document)

log.debug(f"Got message pain001 with msg_id = {pain001_doc.cstmr_cdt_trf_initn.grp_hdr.msg_id}")