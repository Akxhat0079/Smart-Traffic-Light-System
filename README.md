# Smart-Traffic-Light-System
"Design and Development of an Embedded Smart Traffic Signal Control System Using Real-Time Sensor Data and Citizen Mobility Analytics for Smart Cities”

🚦 Smart Traffic Signal Control System (STSS)
Real-Time Sensor Data & Citizen Mobility Analytics for Smart Cities
📖 Introduction
The Smart Traffic Signal Control System (STSS) is a data-driven, intelligent urban infrastructure solution designed to mitigate the growing challenges of traffic congestion and gridlock in modern smart cities. Moving beyond traditional fixed-timer signal cycles, this project introduces a dynamic, "Platinum" priority-based control mechanism that adapts to live traffic pulses in real-time.

By leveraging high-frequency data from global traffic APIs and applying unsupervised machine learning, the system creates a "Digital Twin" of a city's mobility—specifically optimized for the unique traffic patterns of Dehradun.

🛠️ Project Core Description
This repository hosts a multi-stage software pipeline that automates the lifecycle of traffic management, from raw data harvesting to automated signal intervention.

1. Real-Time Data Ingestion (Harvester)
The foundation of the system is a high-frequency asynchronous engine that polls traffic metrics on a strict 60-second "Heartbeat" cycle. It captures critical parameters including current velocity, free-flow benchmarks, and reliability confidence scores, ensuring the system operates on the most current state of the road network.

2. Mobility Refinery & Quality Firewall
To ensure high-fidelity decision-making, the system employs a "Quality Firewall" that filters out noisy data (Confidence < 70%) and performs missing-value treatment. It transforms raw technical sensor data into human-readable mobility insights through geolocation mapping and temporal standardization.

3. The Analytical ML Brain
At the heart of the project is an Unsupervised K-Means Clustering model. This intelligence layer automatically categorizes intersections into three distinct states—Low, Moderate, and Heavy Traffic—removing the need for manual, error-prone labeling. Additionally, the system uses Agglomerative Hierarchical Clustering and dendrograms to understand behavioral relationships between different traffic segments.

4. Command Center & Adaptive Signal Trigger
The final layer is a Streamlit-based Command Center. It provides a live heatmap of the city’s traffic density and triggers an Adaptive Signaling Logic. When the system identifies a "Rank 1" critical intersection, it overrides standard timers to extend green phases, prioritizing the clearance of vehicle backlogs in real-time.

🚀 Key Features
Dynamic Priority Scoring: Automatically ranks chowks from 1 (Critical) to 4 (Normal).

3D Dimensional Analysis: Visualizes decision accuracy across Speed, Delay, and Confidence axes.

Asynchronous Harvesting: Designed for scale with non-blocking API requests.

Citizen Mobility Mapping: Integrated geodata for strategic rerouting and public alerts.

Author: [Your Name]

Institution: DIT University

Focus: Data Science, Embedded Systems, and Urban Mobility Analytics
