import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import open3d as o3d

folder = glob.glob('/home/hasti/DPS/resursi/Gazebo/*.csv')

list = []
for file in folder:
    df = pd.read_csv(file)
    df = df[['x', 'y', 'z']]
    print(file)
    list.append(df)

cloud = pd.concat(list)
print(cloud)

pcd =o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.asarray(cloud) * 10.0)

pcd.translate(-pcd.get_center())

down = pcd.random_down_sample(0.2)

o3d.visualization.draw_geometries([down])