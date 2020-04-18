import json
import pprint
import websocket
from websocket import create_connection

websocket.enableTrace(True)
ws = create_connection('wss://1qh6rc38y1.execute-api.us-east-1.amazonaws.com/dev?clientid=shd')
print("Connected")
while True:
    try:
        received = ws.recv()
        if received is not None:
            received = eval(received)
            print(received['Message'])

    except KeyboardInterrupt:
        break

