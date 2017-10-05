import codecs
import sys


def sortKSUID(ksuidList):
    """
    sorts a list of ksuids by their date (recent in the front)
    """
    return sorted(ksuidList, key=lambda x: x.getTimestamp(), reverse=False)


def int_to_bytes(n, length, byteorder="big"):
    if sys.version_info[0] >= 3:
        return int(n).to_bytes(length, byteorder=byteorder)

    h = "%x" % n
    s = ("0" * (len(h) % 2) + h).zfill(length * 2).decode("hex")
    return s if byteorder == "big" else s[::-1]


def int_from_bytes(s, byteorder="big", signed=False):
    if sys.version_info[0] >= 3:
        return int.from_bytes(s, byteorder, signed=signed)

    if isinstance(s, list):
        s = "".join(s)

    return int(codecs.encode(s, "hex"), 16)
