from evengsdk.client import EvengClient
from pprint import pprint

client = EvengClient("192.168.1.202", log_file="test.log")
client.login(username="admin", password="eve")
resp = client.api.list_node_templates()
pprint(resp.get("data"))