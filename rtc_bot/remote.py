import asyncio
from rtcbot import Websocket, RTCConnection, CVCamera

cam = CVCamera()
conn = RTCConnection()
conn.video.putSubscription(cam)

async def connect():
    #ws = Websocket("http://localhost:8080/xyz")
    ws = Websocket("http://13.233.21.7:8080/node2")
    remoteDescription = await ws.get()
    print(remoteDescription)
    robotDescription = await conn.getLocalDescription(remoteDescription)
    #print(robotDescription)
    ws.put_nowait(robotDescription)
    print("Started WebRTC")
    await ws.close()

asyncio.ensure_future(connect())
try:
    asyncio.get_event_loop().run_forever()
finally:
    cam.close()
    conn.close()