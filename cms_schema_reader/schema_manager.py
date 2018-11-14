

class SchemaManager():
    def __init__(self,content):
        self._content = content
        self._property_names = []

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        assert type(value) == dict
        self._content = value

    def process(self):
        self._process_dict(self._content)
        return self._property_names

    def _process(self, key , obj):
        if key == 'uid':
            self._property_names.append(obj[key])
        #print(key)

    @property
    def property_names(self):
        return self._property_names


    def _process_dict(self, obj):
        keys = obj.keys()
        if len(keys) == 0:
            return
        for key in keys:
            if type(obj[key]) == dict:
                self._process_dict(obj[key])
            elif type(obj[key]) == list:
                self._process_list(obj[key])
            else:
                self._process(key , obj)

    def _process_list(self, objs):
        for obj in objs:
            keys = obj.keys()
            if len(keys) == 0:
                return
            for key in keys:
                if type(obj[key]) == dict:
                    self._process_dict(obj[key])
                elif type(obj[key]) == list:
                    self._process_list(obj[key])
                else:
                    self._process(key, obj)