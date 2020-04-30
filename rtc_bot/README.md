### Live Video Streaming via WebRTC over Sockets

#### On Local system or Cloud server:

1. Install and make a venv:  <br /> 
Install -  <br />
    `sudo apt-get install python3-venv` <br />
Make -  <br />
    `python3 -m venv rtc_env` <br />
    `source rtc_env/bin/activate.sh` <br />
    `pip install -U pip` <br />

2. Install AIORTC, AIOHTTP and opencv: <br />
    `pip install aiohttp aiortc opencv-contrib-python` <br />

3. Install dependencies: <br /> 
    `sudo apt-get install build-essential python3-numpy python3-cffi python3-aiohttp \
    libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev \
    libswscale-dev libswresample-dev libavfilter-dev libopus-dev \
    libvpx-dev pkg-config libsrtp2-dev python3-opencv pulseaudio`

4. Install rtcbot library: <br />
    `pip install rtcbot`

5.  `mkdir rtcbot` <br />
    `cd rtcbot` <br />
    `touch server.py` <br />
    `nano server.py` <br />
<br />
Copy all contents of server.py of repo onto server.py at EC2 Instance and save Ctrl+X --> Enter. <br />
    `python server.py` <br /> 

6. Running the remote client:
    `python client.py`

7. Open http://Your_Server_Public_IPv4_Address:8080 if running on server OR http://localhost:8080 if running on local network.