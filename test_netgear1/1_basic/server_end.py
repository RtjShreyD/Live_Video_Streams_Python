# import libraries
# from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears import CamGear
import cv2

stream = CamGear().start()
#stream = VideoGear(source='test.mp4').start() #Open any video stream
server = NetGear() #Define netgear server with default settings

print("Stream ON")
# infinite loop until [Ctrl+C] is pressed
while True:
	try: 
		frame = stream.read()
		# read frames

		# check if frame is None
		if frame is None:
			#if True break the infinite loop
			break

		# do something with frame here

		# send frame to server
		server.send(frame)
	
	except KeyboardInterrupt:
		#break the infinite loop
		break

# safely close video stream
stream.stop()
# safely close server
server.close()