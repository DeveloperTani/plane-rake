# ✈️ PlaneRake

**PlaneRake** is a personal project built out of curiosity that tracks aircraft activity over a defined area using the [Flightradar24 API](https://fr24api.flightradar24.com/docs). It fetches data, saves it to **CSV and/or JSON**, and makes it ready for visualization in tools like **Power BI**.

It’s designed to be beginner-friendly, especially for people who aren’t programmers but want to work with real flight data. All query settings are easily adjustable in a config file, and **CLI (command-line) support** is planned for future versions.

> ⚠️ This project was originally developed before Flightradar24 released official batch query samples and before support for filters. You can now find the sample scripts here:  
> [https://fr24api.flightradar24.com/docs/endpoints/flight-positions-batch-query](https://fr24api.flightradar24.com/docs/endpoints/flight-positions-batch-query)

---

## 📌 Purpose

Planerake was built to:

- Explore trends in aircraft flight behavior
- Gain real-world experience with raw data pipelines
- Visualize movement, altitude, and speed using modern tools

---

## 🛠️ Tools & Technologies

- **Python** – for data handling and preprocessing  
- **Power BI** – for dashboards and visualizations

---

## 📈 What It Does

- Fetches historical flight data with parameters such as time, coordinates, altitude, speed
- Saves the data to **CSV and/or JSON**
- Easy configuration via `config.py`

---

## 🔧 Future Improvements

- Support for more Flightradar24 API endpoints
- CLI support


---

## 🧪 Usage

### 1. Install Python

Make sure Python **3.13 or newer** is installed.  
👉 [Download Python here](https://www.python.org/downloads/)

---

### 2. Clone the Repository

```bash
git clone https://github.com/DeveloperTani/planeRake.git
cd planerake
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or, if you prefer manual install:

```bash
pip install requests python-dotenv
```

---

### 4. Get Your API Token

To use this tool, you'll need a Flightradar24 API key.

**To get an API key, visit:** https://fr24api.flightradar24.com/docs/getting-started

Then create a `.env` file inside the `src/` folder:

```
FR24_TOKEN=your_token_here
```

---

### 5. Configure Parameters

Open `config.py` and adjust:

```python
BOUNDS = '60.400, 60.200, 24.800, 25.200'  # North, South, West, East
START_TIME_STRING = '2025-06-09 14:00'     # UTC time
DURATION_SECONDS = 3600                    # Duration (in seconds)
LOG_RATE_SECONDS = 30                      # Interval between samples
SLEEP_SECONDS = 6                          # Delay between requests
WRITE_CSV = True
WRITE_JSON = True
```

---

### 6. Run the Program

```bash
python main.py
```

This will fetch and save aircraft data in your chosen format.



