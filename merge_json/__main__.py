# test cases for jsonStringA and jsonStringB according to your data input
jsonStringA = '{"title": "WLBX", "provider_name": "Wing Lung Bank", "alias": "wing-lung-bank"}'
jsonStringB = '{"provider_name": "Wing Lung Bank Updated"}'

# now we have two json STRINGS
import json
dictA = json.loads(jsonStringA)
dictB = json.loads(jsonStringB)

merged_dict = {key: value for (key, value) in (dictB.items() | dictA.items())}

# string dump of the merged dict
jsonString_merged = json.dumps(merged_dict)
print(merged_dict)