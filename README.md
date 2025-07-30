# Robotic Grasping Database

This repository contains a comprehensive database for robotic grasping, featuring data for both a 2-finger gripper and a suction cup. The database is based on the EGAD mesh dataset. Additionally, it includes scripts to visualize the data, aiding in the analysis and development of grasping algorithms.

# Features
- 2-Finger Gripper Data: Detailed datasets for grasping tasks using a 2-finger gripper, to be presented at the International IFAC Symposia on Mechatronics & Robotics 2025.
- Suction Cup Data: Comprehensive datasets for grasping tasks using a suction cup.
- Visualization Scripts: Tools to visualize and analyze the grasping data.


# License
The source code is released under [MIT License](LICENSE). The dataset is released under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

# Contributing

Contributions are welcome! Please open an issue or submit a pull request.

# Requierements

- Python3.11 
- Librairies (requierements.txt)
  + Open3d
  + Numpy
  + H5py
 
## Installation :
```
git clone https://github.com/MichaelGs1/Grasping-Dataset.git
cd grasping-dataset
pip install -r requierements.txt
```

# Usage :

1. Download EGAD Database :
```
cd EGAD
chmod +x download_egad.sh
./download_egad.sh
```

2. Visualization :
```
cd Scripts
python3.11 show_grasps.py A05_0 50
python3.11 show_suctions.py A05_0 50 light    #if you want light gripper for better visualization
```

# Dataset

#### Hdf5 file structure:

```
/grasp : array of grasps transformation matrix
/center : array of transformation matrix from center of egad object to center of gravity 
```
