from schema_manager import SchemaManager

class SchemaValidator():
    def __init__(self, valid_property_names):
        self._valid_property_names = valid_property_names
        self._property_names = []

    def check(self, entry):
        self._process_dict(entry)
        helper_set_a = set(self._property_names)# remove dublicates
        helper_set_b = set(self._valid_property_names)# remove dublicates
        result = helper_set_a.difference(helper_set_b)
        if len(result) == 1 :
            return True
        else:
            assert  len(result) == 1, result

        #self.process()

    @property
    def property_names(self):
        return self._valid_property_names

    def process(self):

        return self._property_names


    def _process(self, key):
        self._property_names.append(key)
        #print(key)


    def _process_dict(self, obj):
        keys = obj.keys()
        if len(keys) == 0:
            return
        for key in keys:
            if type(obj[key]) == dict:
                self._process_dict(obj[key])
            elif type(obj[key]) == list:
                self._process_list(obj[key],key)
            else:
                self._process(key)

    def _process_list(self, objs , key):
        for obj in objs:
            if obj is None:
                continue
            if type(obj) == dict:
                self._process_dict(obj)
            elif type(obj) == list:
                self._process_list(obj)
            else:
                self._process(key)


