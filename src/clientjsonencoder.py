import json


class ClientJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_JSON'):
            return obj.to_JSON()
        return json.JSONEncoder.default(self, obj)
