def sortKSUID(ksuidList):
    """
    sorts a list of ksuids by their date (recent in the front)
    """
    return sorted(ksuidList, key=lambda x: x.getTimestamp(), reverse=False)
