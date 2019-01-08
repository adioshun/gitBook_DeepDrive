```

[L(for lidar)] [m_x] [m_y] [t] [r_x] [r_y] [r_vx] [r_vy]
[R(for radar)] [m_rho] [m_phi] [m_drho] [t] [r_px] [r_py] [r_vx] [r_vy]

Where:
(m_x, m_y) - measurements by the lidar
(m_rho, m_phi, m_dho) - measurements by the radar in polar coordinates
(t) - timestamp in unix/epoch time the measurements were taken
(r_x, r_y, r_vx, r_vy) - the real ground truth state of the system

Example:
R 8.60363 0.0290616 -2.99903  1477010443399637  8.6 0.25  -3.00029  0
L 8.45  0.25  1477010443349642  8.45  0.25  -3.00027  0 

```

In this project the LIDAR measurements are transformed from the cartesian into the polar coordinate system using this formula:



![](http://www.coldvision.io/wp-content/uploads/2017/04/object_tracking_rada_measurements_transform.png)