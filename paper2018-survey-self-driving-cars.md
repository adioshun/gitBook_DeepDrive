Self-Driving Cars: A Survey

https://arxiv.org/pdf/1901.04407v1.pdf

```
Summary
I. Introduction......................................................................2
II. Overview of the Architecture of Self-Driving Cars.....3
III. Perception ....................................................................4
A. Localization..............................................................4
1) LIDAR-Based Localization .....................................5
2) LIDAR plus Camera-Based Localization ................6
3) Camera-Based Localization .....................................6
B. Offline Obstacle Mapping........................................7
1) Discrete Space Metric Representations....................7
2) Continuous Space Metric Representations...............8
C. Road Mapping..........................................................8
1) Road Map Representation........................................8
2) Road Map Creation ..................................................9
D. Moving Objects Tracking ......................................10
1) Traditional Based MOT .........................................10
2) Model Based MOT.................................................10
3) Stereo Vision Based MOT .....................................11
4) Grid Map Based MOT ...........................................11
5) Sensor Fusion Based MOT ....................................11
6) Deep Learning Based MOT ...................................12
E. Traffic Signalization Detection and Recognition.......12
1) Traffic Light Detection and Recognition ...............12
2) Traffic Sign Detection and Recognition.................13
3) Pavement Marking Detection and Recognition......14
IV. Decision Making........................................................14
A. Route Planning.......................................................14
1) Goal-Directed Techniques .....................................15
2) Separator-Based Techniques..................................15
3) Hierarchical Techniques........................................15
4) Bounded-Hop Techniques .....................................15
5) Combinations.........................................................16
B. Motion Planning ....................................................16
1) Path Planning.........................................................16
2) Trajectory Planning ...............................................17
C. Control...................................................................19
1) Path Tracking Methods..........................................19
2) Hardware Actuation Control Methods...................20
V. Architecture of the UFES’s Car “IARA”...................20
VI. Self-Driving Cars under Development in the Industry
22
References .............................................................................24
```

# Self-Driving Cars: A Survey

```
The architecture of the autonomy system of self-driving cars is typically organized into 
- the perception system and 
- the decision-making system. 

The perception system is generally divided into many subsystems responsible for tasks such as 
- self-driving-car localization, 
- static obstacles mapping, 
- moving obstacles detection and tracking, 
- road mapping, 
- traffic signalization detection and recognition, 
- among others. 

The decision making system is commonly partitioned as well into many subsystems responsible for tasks such as 
- route planning,
- path planning, 
- behavior selection, 
- motion planning, and
- control. 
```

## I. INTRODUCTION

## II. OVERVIEW OF THE ARCHITECTURE OF SELF-DRIVING CARS

![](https://i.imgur.com/34n4ifa.png)

## III. PERCEPTION

- localizer (or localization)
- offline obstacle mapping
- road mapping
- moving obstacle tracking
- and traffic signalization detection and recognition.

### 3.1 Localization



#### A. LIDAR-Based Localization




#### B. LIDAR plus Camera-Based Localization

#### C. Camera-Based Localization


### 3.2 Offline Obstacle Mapping

The offline obstacle mapping subsystem is responsible for computing a map of obstacles in the environment of the selfdriving car. 

> OUT-OF-SCOPE

### 3.3 Road Mapping

The road mapping subsystem is responsible for gathering information of roads and lanes in the surroundings of the selfdriving car, and representing them in a map with geometrical and topological properties, including interconnections and
restrictions. 

The main topics of the road mapping subsystem are 
- the map representation and 
- the map creation.

> OUT-OF-SCOPE

### 3.4 Moving Objects Tracking

>  중요, 다시 살펴 보기 

### 3.5 Traffic Signalization Detection and Recognition


## 4. DECISION MAKING

> OUT-OF-SCOPE



## 5. ARCHITECTURE OF THE UFES’S CAR “IARA”

The Intelligent and Autonomous Robotic Automobile (IARA)

It follows the typical architecture of self driving cars. 

IARA is a research autonomous vehicle that was developed at the Laboratory of High Performance Computing of the Federal University of Espírito Santo (Universidade Federal do Espírito Santo – UFES)

### 5.1 장비 

IARA’s computers and sensors comprise a workstation (Dell Precision R5500, with 2 Xeon X5690 six-core 3.4GHz processors and one NVIDIA GeForce GTX-1030), 
 
networking gear, 

two LiDARs (a Velodyne HDL-32E and a SICK LDMRS),

three cameras (two Bumblebee XB3 and one ZED), 

an IMU (Xsens MTi) 

and a dual RTK GPS (based on the Trimble BD982 receiver).

## 6. SELF-DRIVING CARS UNDER DEVELOPMENT IN THE INDUSTRY

### 6.1 Torc 

Torc was one of the pioneers in developing cars with selfdriving capabilities. 

The company was founded in 2005. 

In 2007, it joined Virginia Tech’s team to participate in the 2007 DARPA Urban Challenge with their autonomous car “Odin” [BAC08], which reached third place in the competition. 

The technology used in the competition was improved since then and it was successfully applied in a variety of commercial ground vehicles, from large mining trucks to military vehicles [TOR18]. 

### 6.2 Google - Waymo

Google's self-driving car project began in 2009 and was formerly led by Sebastian Thrun, who also led the Stanford University’s team with their car “Stanley” [THR07], winner of
the 2005 DARPA Grand Challenge. 

In 2016, Google's self driving car project became an independent company called Waymo [WAY18]. 

The company is a subsidiary of the holding Alphabet Inc., which is also Google's parent company.

Waymo's self-driving car uses a sensor set composed of LIDARs to create a detailed map of the world around the car, RADARs to detect distant objects and their velocities, and high resolution cameras to acquire visual information, such as
whether a traffic signal is red or green [WAY18b]. 


### 6.3 Baidu 

Baidu, one of the giant technology companies in China, is developing an open source self-driving car project with code name Apollo [APO18]. 

The source code for the project is available in GitHub [APOL18]. 

It contains modules for perception (detection and tracking of moving obstacles, and detection and recognition of traffic lights), HD map and localization, planning, and control, among others. 

Several companies are partners of Baidu in the Apollo project, such as TomTom, Velodyne, Bosch, Intel, Daimler, Ford, Nvidia, and Microsoft. 

One of the Apollo project’s goals is to create a centralized place for original equipment manufacturers (OEMs), startups, suppliers, and research organizations to share and integrate their data and resources. 

Besides Baidu, Udacity, is also developing an open source self driving car, which is available for free in GitHub [UDA18].


### 6.5 Uber

Uber is a ride-hailing service and, in 2015, they partnered with the Carnegie Mellon University to develop self-driving cars [UBE15]. 

A motivation for Uber's project is to replace associated drivers by autonomous software [UBE18]. 

### 6.6 Lyft

Lyft is a company that provides ride sharing and on-demand driving services. 

Like Uber, Lyft is doing research and development in self-driving cars [LYF18]. 

The company aims at developing cars with level 5 of autonomy. 

### 6.7 Aptiv

> V2V comm.

Aptiv is one of Lyft's partners. 

Aptiv was created in a split of Delphi Automotive, a company owned by General Motors.

Aptiv’s objective is to build cars with level 4 and, posteriorly, level 5 of autonomy [APT18]. 

Besides other products, the company sells short-range communication modules for vehicle-to-vehicle information exchange. 

Aptiv recently acquired two relevant self-driving companies, Movimento and nuTonomy


### 6.8 Didi

Didi is a Chinese transportation service that bought Uber's rights in China. 

Didi's self-driving car project was announced in 2017 and, in February of 2018, they did the first successful demonstration of their technology. 

In the same month, company’s cars started being tested in USA and China. 

Within a year, Didi obtained the certificate for HD mapping in China. 

The company is now negotiating a partnership with Renault, Nissan, and Mitsubishi to build an electric and autonomous ride-sharing service [ENG18]. 


### 6.9 Tesla 

Tesla was founded in 2003 and, in 2012, it started selling its first electric car, the Model S. 

In 2015, the company enabled the autopilot software for owners of the Model S. 

The software has been improved since then and its current version, the so called enhanced autopilot, is now able to match speed with traffic conditions, keep within a lane, change lanes, transition from one freeway to another, exit the freeway when the destination is near, self-park when near a parking spot, and be summoned to and from the user’s garage [TES18]. 

Tesla's current sensor set does not include LIDARs.

### 6.10 LeEco 

A Chinese company called LeEco is producing self-driving luxury sedans to compete with the Tesla Model S. 

The company is also backing up Faraday Future for the development of a concept car. 

LeEco is also partnering Aston Martin for the development of the RapidE electric car [VERG16]. 

### 6.11 NVIDIA 

Besides developing hardware for general-purpose highperformance computing, NVDIA is also developing hardware and software for self-driving cars [NVI18]. 

Although their solutions rely mostly on artificial intelligence and deep learning, they are also capable of performing sensor fusion, localization in HD maps, and planning [NVID18]. 

### 6.12 Aurora 

Aurora is a new company founded by experienced engineers that worked in Google's self-driving project, Tesla, and Uber [AUR18]. 

The company plans to work with automakers and suppliers to develop full-stack solutions for cars with level 4 and, eventually, level 5 of autonomy. 

Aurora has independent partnerships with Volkswagen group (that owns Volkswagen Passenger Cars, Audi, Bentley, Skoda, and Porsche) and Hyunday [FORT18].


### 6.13 Zenuity 

Zenuity is a joint venture created by Volvo Cars and Autoliv [ZEN18]. 

Ericsson will aid in the development of Zenuity’s Connected Cloud that will use Ericsson's IoT Accelerator [ERI18]. 

TomTom also partnered with Zenuity and provided its HD mapping technology [TOM18].

TomTom’s HD maps will be used for localization, perception and path planning in Zenuity's software stack.

### 6.14 Daimler and Bosch

Daimler and Bosch are joining forces to advance the development of cars with level 4 and 5 of autonomy by the beginning of the next decade [BOS18]. 

The companies already have an automated valet parking in Stuttgart [DAA18] and they also have tested the so called Highway Pilot in trucks in USA and Germany [DAB18]. 

Besides partnering with Bosch, Daimler also merged its car sharing business, Car2Go, with BMW's ReachNow, from the same business segment, in an effort to stave off competition from other technology companies, such as Waymo and Uber [DAC18]. 

The new company will include business in car sharing, ride-hailing, valet parking, and electric vehicle charging.

### 6.15 Argo 

Argo AI founders led self-driving car teams at Google and Uber [ARG18]. 

The company received an investment of U$ 1 billion from Ford with the goal of developing a new software platform for Ford’s fully autonomous vehicle (level 4) coming in 2021. 

They have partnerships with professors from Carnegie Mellon University and Georgia Tech [ARB18]. 

### 6.16 Renesas 

Renesas Autonomy develops several solutions for automated driving assistant systems (ADAS) and automated driving [REN18]. 

The company has a partnership with the University of Waterloo [RENE18]. 


### 6.17 Hoda 

Honda revealed in 2017 plans for introducing cars with level 4 of autonomy by 2025. 

The company intends to have vehicles with level 3 of autonomy by 2020 and it is negotiating a partnership with Waymo [HON18]. 

### 6.18 Visteon 

Visteon is a technology company that manufactures cockpit electronic products and connectivity solutions for several vehicle manufacturers [VIS18]. 

In 2018, Visteon introduced its autonomous driving platform capable of level 3 of autonomy and, potentially, higher levels. 

The company does not aim at producing cars and sensors, but at producing integrated solutions and software. 


### 6.19 AI Motive 

AI motive is using low cost components to develop a selfdriving platform [AIM18]. 

Its solution relies strongly on computer vision, but it uses additional sensors. 

The company is already able to perform valet parking and navigate in highways. 

AImotive also developed a photorealistic simulator for data collection and preliminary system testing, and chips for artificial intelligence-based, latency-critic, and camera centric systems. 

As AImotive, AutoX is avoiding to use LIDARs in its solution. 

However, the company is going further than Almotive and trying to develop a level 5 car without using RADARs, ultrasonics, and differential GPS’s. 

AutoX's approach is to create a full-stack software solution based on artificial intelligence [AUT18].


### 6.20 Mobileye 

Mobileye is also seeking to develop a self-driving solution without using LIDARs, but relying mostly in a single-lensed camera (mono-camera). 

Mobileye is one of the leading suppliers of software for Advanced Driver Assist Systems (ADAS), with more than 25 partners among automakers.

Beyond ADAS, Mobileye is also developing technology to support other key components for autonomous driving, such as perception (detection of free space, driving paths, moving objects, traffic lights, and traffic signs, among others),mapping, and control. 

The company partnered with BMW and Intel to develop production-ready fully autonomous vehicles, with production launch planned for 2021 [MOB18].


### 6.21 Ambarella

Ambarella also does not use LIDAR, but only RADARs and stereo cameras. 

The company joined the autonomous driving race in 2015 by acquiring VisLAB. 

Different from other companies, Ambarella does not aim at becoming a tier one supplier or selling complete autonomous-driving systems.

Instead, they plan to sell chips and software to automakers, suppliers, and software developers. 

Ambarella’s current research and development guidelines include detection of vehicles, obstacles, pedestrians, and lanes; traffic sign recognition; terrain mapping; and issues related to technology commercialization, such as system calibration, illumination, noise, temperature, and power consumption [AMB18]. 


### 6.22 Pony.ai 

Pony.ai was founded in December of 2016 and, in July of 2017, it completed its first fully autonomous driving demonstration. 

The company signed a strategic agreement with one of the biggest Chinese car makers, the Guangzhou Auto Group (GAC) [PON18].

### 6.23 Navya and Transdev

Navya [NAA18] and Transdev [TRA18] are French companies that develop self-driving buses. 

Navya has several of their buses being tested in Europe, Asia, and Australia.

Their sensor set consists of two multi-layer 360º LIDARs, six 180º mono-layer LIDARs, front and rear cameras, odometer (wheels encoder + IMU), and a GNSS RTK [NAB18].

Transdev is also already demonstrating their self-driving buses for the public [TRA18].

### 6.24 JD

JD is a Chinese e-commerce company interested in building self-driving delivery vehicles [JD18]. 

JD's project, started in 2016, is being developed together with Idriverplus [IDR18], a Chinese self-driving car startup. 

### 6.25 Toyota 

In March, 2018, Toyota announced an investment of U$ 2.8 billion in the creation of a new company called the Toyota Research Institute-Advanced Development (TRI-AD) with the goal of developing an electric and autonomous car until 2020
[TOYT18]. 

Besides Toyota [TOY18], other car manufacturers, such as Ford [FOR18], Volvo [VOLV18], and Mercedes-Benz [MER18], have also recently presented their plans for self-driving cars. 

### 6.26 Ford

Ford defined 2021 as a deadline for presenting a fully autonomous vehicle ready for commercial operation.