# 🐭 Micromouse Maze-Solving Simulation

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Algorithm](https://img.shields.io/badge/Algorithm-Greedy_Best--First_Search-brightgreen.svg)]()

## 📌 Project Overview
This repository contains the autonomous navigation logic for a virtual Micromouse robot. The project simulates a physical robot equipped with sensors to explore, map, and find the optimal path to the center of a complex 16x16 maze. 

By separating the movement execution (`API.py`) from the core pathfinding logic (`Main.py`), this project demonstrates a scalable approach to robotics programming. It serves as a strong foundation for translating high-level logic algorithms into dynamic hardware environments (Embedded Systems/AIoT).

## ⚙️ Core Technologies
* **Language:** Python
* **Dependencies:** None! Built entirely using Python's standard libraries (`sys`, `math`), ensuring zero setup friction.
* **Algorithm:** Greedy Best-First Search (optimizing for the shortest path based on simulated sensor coordinates).
* **Simulator:** Mackorone's Micromouse Simulator (mms).

## 📂 Repository Structure
* `/maps`: Contains various `.txt` files representing different maze layouts and configurations.
* `/Mouse_code`: 
  * `Main.py`: The core algorithm driving the robot's decision-making.
  * `API.py`: The bridge interface communicating with the simulator (handling commands like move forward, turn, read sensors).
* `/Program`: Contains `mms.exe`, the lightweight visual simulator used to execute the code.

## 🚀 Quick Start Guide

Follow these steps to run the simulation on your local machine:

**Step 1: Launch the Simulator**
Navigate to the `Program` folder and run `mms.exe`.

**Step 2: Load the Maze**
* In the simulator UI, look at the **Config** section (top right).
* Next to **Maze**, click the folder icon 📁.
* Browse to the `maps` folder in this repository and select any maze file.

**Step 3: Configure the Mouse Algorithm**
* Next to **Mouse**, click the edit icon 📝 (or the `+` button to add a new configuration).
* A configuration window will appear. Fill in the following details:
  * **Name:** Give your mouse a name (e.g., `qang_mouse`).
  * **Directory:** Click **Browse** and select the `Mouse_code` folder in this repository.
  * **Build Command:** *(Leave this completely blank)*.
  * **Run Command:** Type `python Main.py`.
* Click **OK**.

**Step 4: Run!**
Click the **Run** button in the Controls panel and watch the Micromouse navigate the maze!

## 🎥 Demonstration
*(Note to recruiter: Add a GIF here showing the mouse successfully solving a maze)*
> `[Insert an animated GIF of the simulator running here]`

## 💡 Key Engineering Takeaways
* **Sensor Data Processing:** Successfully processed simulated sensor parameters to calculate optimal paths and avoid walls dynamically.
* **Algorithmic Efficiency:** Implemented Greedy Best-First Search to navigate complex layouts, significantly minimizing travel time and redundant movements.
* **Hardware Readiness:** Designed the software architecture with clear abstraction layers, making it easier to port the Python logic into C/C++ for future physical microcontroller deployment.

---
*This project was developed to hone problem-solving skills at the intersection of software algorithms and physical systems.*
