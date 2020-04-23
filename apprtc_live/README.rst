AppRTC client
=============

This example illustrates how to connect to Google's AppRTC demo application.
It actually illustrates:

How to establish a live video stream in a video-chat room over Webrtc using aiortc python, this script can be initiated
from the client end to send realtime video frames on a global network.

First install the required packages:

.. code-block:: console

    $ pip install aiohttp aiortc opencv-python websockets

When you run the example, it will connect to AppRTC and wait for a participant
to join the room:

.. code-block:: console

   $ python apprtc.py

You will be given a URL which you can point your browser to in order to join
the room.

Additional options
------------------

If you want to record the received media you can run the following:

.. code-block:: console

   $ python apprtc.py --record-to video.mp4

--------------------

