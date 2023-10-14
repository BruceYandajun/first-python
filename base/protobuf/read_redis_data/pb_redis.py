import rank_pb2
import redis

# dev
# r = redis.Redis(host='10.137.16.160', port=8093, db=0, password="123456a?")
# test
r = redis.Redis(host='10.137.16.160', port=8096, db=0, password="123456a?")


# data = r.get("USER-personal-bruce")
# user_info = rank_pb2.MsgClass.UserInfoClass()
# user_info.ParseFromString(data)
# print(user_info)
# #
data = r.get("ITEM-recannnew-97d38af4b6a4420abe0e6d57157c5153")
item_info = rank_pb2.MsgClass.ItemInfoClass()
item_info.ParseFromString(data)
print(item_info)
