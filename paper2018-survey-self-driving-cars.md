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


