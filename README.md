✈️ Planerake

Planerake is a personal project born out of curiosity to track aircraft altitudes over a defined area. It pulls data from the Flightradar24 API and writes it to a CSV and/or JSON file for further analysis. The data can then be visualized using tools like Power BI.

This tool was built to be user-friendly, especially for non-programmers who want to fetch and use data from the Flightradar API. Query parameters can currently be modified in the config file, but I plan to add CLI functionality for easier, terminal-based input.

    ⚠️ This project was initially built before Flightradar24’s official sample scripts for historical batch queries were published. You can find those here:
    https://fr24api.flightradar24.com/docs/endpoints/flight-positions-batch-query

📌 Purpose

This project was created to explore trends in flight data and build visual dashboards from real-world raw data. It gave me hands-on experience with:

    Parsing structured and semi-structured data (JSON/CSV)

    Data wrangling and transformation

    Visualizing time series and geospatial data (altitude, speed, movement)

    Using Power BI for dashboarding and analysis

🛠️ Tools & Technologies

    Python – data handling and preprocessing

    Power BI – dashboards and visualization

📈 What It Does

    Loads and parses historical aircraft flight data over a user-defined area and time window

    Extracts features like timestamps, speed, altitude, and GPS coordinates

    Cleans and reshapes the data for dashboard use

    Supports configuration of coordinates, time window, logging interval, and output format (CSV/JSON) via the config file

📊 Sample Output

A sample Power BI visualization will be included in the /visuals folder.
🧠 What I Learned

This project helped sharpen my:

    Ability to handle and analyze time-indexed data

    Skill in identifying meaningful visual patterns

    Understanding of data pipelines — from raw input to polished dashboard


🔧 Future Improvements

    Add real-time data handling

    Expand functionality to include other Flightradar24 API endpoints

    Turn it into a CLI tool to allow input via terminal instead of editing the config file

🤝 Why It Matters

Projects like this reflect real-world IoT and industrial data challenges — turning noisy sensor data into actionable insight. It’s a hands-on example of how I approach problem-solving and build practical tools from scratch.
