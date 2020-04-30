import asyncio
from rtcbot import Websocket, RTCConnection, CVCamera

cam = CVCamera()
conn = RTCConnection()
conn.video.putSubscription(cam)

# Connect establishes a websocket connection to the server,
# and uses it to send and receive info to establish webRTC connection.
async def connect():
    # ws = Websocket("http://localhost:8080/ws")
    # ws = Websocket("https://rtcbot.dev/myRandomSequence1532")
    # ws = Websocket("http://13.127.250.133:8080/ws")
    # ws = Websocket("http://localhost:8080/xyz")  # xyz could be the remote device id, in multi_client mode.
    ws = Websocket("http://13.127.250.133:1452/xyz002")
    remoteDescription = await ws.get()
    robotDescription = await conn.getLocalDescription(remoteDescription)
    ws.put_nowait(robotDescription)
    print("Started WebRTC")
    await ws.close()

asyncio.ensure_future(connect())
try:
    asyncio.get_event_loop().run_forever()
finally:
    cam.close()
    conn.close()