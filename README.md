# AI Crime Hotspot Detection

AI Crime Hotspot Detection is a web-based crime analysis and visualization system for Punjab crime data. It provides an interactive dashboard, chatbot interface, crime statistics, district-wise analysis, maps, and charts to help analyze crime trends across Punjab.

## Features

* Crime intelligence chatbot interface
* District-wise crime analysis for Punjab
* Interactive crime map using Leaflet.js
* Crime type filtering on map
* Year-wise crime trend visualization
* Crime statistics dashboard
* Case status analysis
* Top crime districts and safest district insights
* Quick question buttons for common crime queries
* Chart-based visualization using Chart.js
* Flask backend API integration

## Tech Stack

* HTML
* CSS
* JavaScript
* Leaflet.js
* Chart.js
* Flask
* Python
* Machine Learning
* Data Visualization

## Main Modules

* Chatbot UI for crime-related questions
* Interactive map panel
* Charts panel for crime trends
* Statistics panel for case summaries
* District browsing section
* Flask API connection for backend responses

## Dataset Information

The project is based on Punjab crime records and includes:

* Crime incidents across Punjab districts
* Crime type information
* Case status data
* District and area-level details
* Year-wise crime trends

## How It Works

1. User asks a crime-related question through the chatbot.
2. The frontend sends the query to the Flask backend API.
3. The backend processes the request and returns a response.
4. The dashboard displays chatbot answers, charts, statistics, and map updates.
5. Users can filter map data by crime type and browse district-wise crime statistics.

## API Endpoints Used

```text
GET  /stats
POST /chat
POST /map-data
POST /graph-data
```

## Screenshots

Add screenshots here:

```text
assets/home-page.png
assets/chatbot.png
assets/map-view.png
assets/charts-view.png
assets/stats-panel.png
```

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/gautamSingh0710/AI-Crime-Hotspot-Detection-S-UL-.git
```

2. Open the project folder:

```bash
cd AI-Crime-Hotspot-Detection-S-UL-
```

3. Install Python dependencies:

```bash
pip install flask pandas numpy scikit-learn
```

4. Start the Flask backend:

```bash
python api.py
```

5. Open the frontend HTML file in the browser.

6. Make sure the Flask backend is running on:

```text
http://127.0.0.1:5000
```

## Future Improvements

* Add user authentication for admin access
* Deploy frontend and backend online
* Add more crime prediction models
* Improve chatbot response accuracy
* Add downloadable reports
* Add real-time dataset updates

## Author

Gautam Singh
GitHub: https://github.com/gautamSingh0710
