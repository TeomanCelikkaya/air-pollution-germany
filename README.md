# Air Pollution Analysis in German Cities

This project explores air pollution patterns in major German cities using open geospatial and environmental data. By combining air quality data from the AQICN API with urban structure data from OpenStreetMap, the goal is to analyze how pollution varies over time and space and uncover correlations with urban features such as road density and green areas.

---

##  Goals

- Explore how air quality varies between cities and over time
- Visualize pollution hotspots using geospatial data
- Correlate pollution with urban features like traffic and green areas
- Practice end-to-end data science workflows with real open datasets

---

##  Tech Stack

**Python** – Main programming language
**Jupyter Notebook** – Exploratory data analysis & visualization
**Pandas / NumPy** – Data wrangling and manipulation
**OSMNx** – Extracting street networks and geospatial features from OpenStreetMap
**Plotly / Folium** – Interactive visualizations and maps
**AQICN API** – Live air quality data across German cities
**Git / GitHub** – Version control and collaboration

---

##  Project Structure

air-pollution-germany/
├── data/ # Raw and processed data files
├── notebooks/ # Jupyter Notebooks for analysis and EDA
├── src/ # Python scripts for fetching and processing data
│ ├── fetch_aqicn.py
├── README.md # Project documentation
├── requirements.txt # Python dependencies
├──.gitignore
└──.env