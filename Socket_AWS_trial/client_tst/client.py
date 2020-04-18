import json
import pprint
import websocket
from websocket import create_connection

websocket.enableTrace(True)
ws = create_connection('wss://1qh6rc38y1.execute-api.us-east-1.amazonaws.com/dev?clientid=rtj')

ws.send(json.dumps({"Msg":"Hey how are you Shreyansh??","ReceiverID":"shd","action":"sendmsg"}))

print("Msg sent")

result = ws.recv()
print('Result: {}'.format(result))