import json


class StorageRoomEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            return {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
        except AttributeError:
            return super().default(o)
