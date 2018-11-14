
class ReaderEntries():
    def __init__(self , entries):
        assert 'entries' in entries.keys()
        self._entries = entries['entries']

    def get_entries(self):
        for entry in self._entries:
            yield entry


