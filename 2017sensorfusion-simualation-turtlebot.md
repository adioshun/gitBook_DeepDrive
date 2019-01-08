# [SENSOR FUSION FRAMEWORK AND SIMULATION ON A TURTLEBOT ROBOTIC VEHICLE](https://webpages.uncc.edu/~jmconrad/GradStudents/Thesis_Gangadhar.pdf)

> by Shruti Gangadhar, 2017



## 2. SENSOR FUSION OVERVIEW

### 2.1 Sensor Data Acquisition

- 센서 종류에 따라 포맷이 다르다

### 2.2 Need for Sensor Fusion

- 여러 종류의 센서 데이터를 활용하면 정확도가 올라 간다. 

### 2.3 Sensor Fusion Challenges

1. Data imperfection: Data from the sensors contain some amount of noise and
imprecision. Data fusion algorithms should be able to take advantage of the
redundant data to minimize the effects of such imperfections. 
2. Outliers and spurious data: Ambiguity and inconsistencies in the environment that
the sensors may not be able to distinguish, causing the measured data to be
unreliable. Such data appear as outliers in the data set.
3. Conflicting data: If two sensors are offering conflicting data about an aspect under
observation, the fusion algorithm should be able to handle such conflicts to avoid
counter-intuitive results.
4. Data modality: The fusion process must take into consideration both qualitatively
similar (homogeneous) and different (heterogeneous) sensor data.
5. Data correlation: When sensors are spatially distributed in a system, some sensor
nodes are prone to external disturbances. This can bias the sensor readings and the
fusion result may suffer from over/under confidence.
6. Data alignment: Data from various sensors must be brought to a common frame
of reference before the fusion process. It deals with the calibration error induced
by individual sensors.
7. Operational timing: The data used for fusion may be coming from sensors that
span a vast area or from sensors that are generating data at different rates. Out-ofsequence
arrival of data for fusion process can result in performance degradation
especially in real time applications. 

### 2.4 Categories of Sensor Fusion

Depending upon the sensor configuration, there are three main categories of sensor fusion: Complementary, Competitive and Co-operative [23]. 

#### A. Complementary

In this method, each sensor provides data about different aspects
or attributes of the environment. By combining the data from each of the sensors
we can arrive at a more global view of the environment or situation. Since there is
no dependency between the sensors combining the data is relatively easy [23]
[24].

#### B. Competitive

In this method, as the name suggests, several sensors measure the
same or similar attributes. The data from several sensors is used to determine the
overall value for the attribute under measurement. The measurements are taken
independently and can also include measurements at different time instants for a
single sensor. This method is useful in fault tolerant architectures to provide
increased reliability of the measurement [23] [24].


#### C. Co-operative

When the data from two or more independent sensors in the system
is required to derive information, then co-operative sensor networks are used
since a sensor individually cannot give the required information regarding the
environment. A common example is stereoscopic vision [23] [24].
Several other types of sensor networks exist such as corroborative, concordant,
redundant etc [21]. Most of them are derived from the aforementioned sensor fusion
categories.


### 2.5 Fusion Methodologies

Generally, sensor fusion framework is designed or chosen based on the **application**.

#### A. JDL Model

JDL stands for the US Joint Directors of Laboratories that was established under the guidance of Department of Defense and was proposed in 1985

![](https://i.imgur.com/2lQLGgP.png)

#### B. Waterfall Fusion Process Model

The Waterfall fusion process model (WFFM) deals with the low-level processing of data and is shown in Figure 3

![](https://i.imgur.com/1H06K6G.png)

![](https://i.imgur.com/kNFU47S.png)

#### C. Dasarathy’s Classification

![](https://i.imgur.com/3izVMEM.png)


#### D. Category Theory Based Model by Kokar et al. 


### 2.6 Sensor Fusion Topologies

#### A. Centralized

In this architecture, a single node handles the fusion process. 

The sensors undergo preprocessing before they are sent to the central node for the fusion process to take place. 


![](https://i.imgur.com/YEpNck2.png)

#### B. Decentralized

In this architecture, each of the sensor processes data at its node and there is no need for a global or central node. Since the information is processed individually at the node, it is used in applications that are large and widespread such as huge automated plants, spacecraft health monitoring etc [24]

![](https://i.imgur.com/3GE6t1z.png)


#### C.Hybrid

This architecture is a combination of both centralized and distributed type. 

When there are constraints on the system such as a requirement of less computational workload or limitations on the communication bandwidth, distributed scheme can be enabled.

Centralized fusion can be used when higher accuracy is necessary [24] [32].

![](https://i.imgur.com/MxRes6b.png)

### 2.7 Categories of Fusion Algorithms


Sensor fusion can be performed at various levels based on the condition and type of data.

In this context, there are following fusion stages:
1. Signal level fusion
2. Feature level fusion
3. Decision level fusion










