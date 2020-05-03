import asyncio
from rtcbot import Websocket, RTCConnection, CVCamera

cam = CVCamera()
conn = RTCConnection()
conn.video.putSubscription(cam) # subscribed to the camera of device, reads it forever

# Connect establishes a websocket connection to the server,
# and uses it to send and receive info to establish webRTC connection.
async def connect():
    #ws = Websocket("http://13.233.21.7:8080/ws")
    #ws = Websocket("https://rtcbot.dev/00001")
    ws = Websocket("http://localhost:8080/ws") # Wraps an aiohttp websocket to have an API matching RTCBot. So ws becomes an API obj here

    remoteDescription = await ws.get()  # gets information of the browser through socket
    robotDescription = await conn.getLocalDescription(remoteDescription) # creates a response obj for browser 
    # ie remoteDescription obj and the response obj is the video stream which it was already subscribed to. 
    ws.put_nowait(robotDescription) # directly start sending robotDescription data ie video stream,
    # to the ws API through WebRTC. When put_nowait encountered the object waits only for put_nowait(), 
    # thus keeps looping everytime with run_forever.
    print("Started WebRTC")
    await ws.close()
    print("Websocket closed")


asyncio.ensure_future(connect()) # ensure_future is a method to create Task from coroutine and 
# ensure each task of coroutine gets completed.
# Every time robotDescription is computed and put_nowait sends that to the browser. 
# A future is an object that is supposed to have a result in future, 
# thus ensure_future creates tasks by calling coroutine connect() here,
# and directly start its execution and does not bother whether it is awaiting a result or not.
try:
    asyncio.get_event_loop().run_forever() #runs coroutine from ensure_future in an infinite loop

except KeyboardInterrupt:
        pass

finally:
    cam.close()
    conn.close()
