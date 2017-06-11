from ksuid import KSUID

# sorts a list of ksuids by their date (recent in the front)
def sortKSUID(ksuidList):
    return sorted(ksuidList, key=lambda x: x.getTimestamp(), reverse=False)
