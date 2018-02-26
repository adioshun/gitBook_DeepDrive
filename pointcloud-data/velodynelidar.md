
# Sample data 

- [HDL-32/VLP-16](https://midas3.kitware.com/midas/community/29)
    
    - PCAP: all received packet data.
    - CSV: one frame data that is reflection intensity and distance of 0-359.9 degree.
    
- [Velodyne HDL-64E LiDAR, LiDAR Velodyne HDL-32e LiDAR, Velodyne VLP-16 Puck](http://masc.cs.gmu.edu/wiki/MapGMU)

- [VLP16](https://goo.gl/MJDfWA)
            
# VeloView 뷰어 

- [Wiki](https://www.paraview.org/Wiki/VeloView), [Homepage](https://www.paraview.org/VeloView/), [Github](https://github.com/Kitware/VeloView)
- `.pcap` files 재생 
- csv/txt files로 저장 가능

## Point Cloud Library with Velodyne LiDAR

- Point Cloud Library (PCL) have `Grabber` for input data from Velodyne LiDARs.

- `.pcap`파일을 사용 하기 위해서는, You need build PCL with WITH_PCAP option. (Pre-built library is disabled this option.)
    - HDLGrabber : This Grabber for HDL-64E/HDL-32E.
    - VLPGrabber : This Grabber for VLP-16.


## Article 

- [Parse pcap from HDL-32E Sensor](https://github.com/ritzalam/velodyne-lidar-parser): python, Github

- [ROS support for Velodyne 3D LIDARs](https://github.com/ros-drivers/velodyne)

- [Point cloud conversions for Velodyne 3D LIDARs.](http://wiki.ros.org/action/fullsearch/velodyne_pointcloud?action=fullsearch&context=180&value=linkto%3A%22velodyne_pointcloud%22)

- [Velodyne Lidar Python Library](https://github.com/esrlabs/velodyne): HDL 64E S2 only.

- [The Velodyne High Definition LiDAR (HDL) Grabber](http://pointclouds.org/documentation/tutorials/hdl_grabber.php): pcap설정, cpp

---

## `pcap`파일 읽어 Play하기 
- [pcap_reader.py](https://gist.github.com/gerkey/bf749775e6bc600368b97ce3d9f113e5): Read a .pcap file full of UDP packets from a velodyne and play them back to

```python 
#!/usr/bin/env python

# Read a .pcap file full of UDP packets from a velodyne and play them back to
# localhost:2368, for consumption by the velodyne driver.
#
# TODO: error-checking and options (looping, etc.)

import dpkt
import sys
import socket
import time

UDP_IP = "localhost"
UDP_PORT = 2368

def parse(fname):
    lasttime = -1
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i = 0
    with open(fname, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            udp = ip.data
            velodata = udp.data
            if lasttime > 0 and (ts-lasttime) > 0:
                time.sleep(ts-lasttime)
            lasttime = ts
            print('[%d] [%s] sending %d-byte message'%(i,`ts`,len(velodata)))
            sock.sendto(velodata, (UDP_IP, UDP_PORT))
            i += 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('ERROR: must supply pcap filename')
        sys.exit(1)
    while True:
        parse(sys.argv[1])
```

> To prevent exception: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 0: invalid continuation byte we need to use binary mode for open file: dpkt.pcap.Reader(open(filename,'rb'))