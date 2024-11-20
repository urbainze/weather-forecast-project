# **Weather Forecast Pipeline with Airflow, PostgreSQL, and Grafana**

This project implements a data pipeline to fetch, process, and visualize weather data. Using **Apache Airflow**, the pipeline orchestrates the extraction of weather data from an API, stores it in **PostgreSQL**, and visualizes it in **Grafana**.

---

## **Project Overview**

The project retrieves hourly temperature data for a specific location (e.g., Paris) using the Open-Meteo API. The data is then:
1. **Extracted**: Fetched from the API via an Airflow DAG.
2. **Transformed**: Cleaned and formatted into a structured format.
3. **Loaded**: Inserted into a PostgreSQL database.
4. **Visualized**: Displayed in Grafana dashboards for real-time insights.

---

## **Features**

- Automated pipeline with Airflow for ETL (Extract, Transform, Load).
- Persistent storage of weather data in PostgreSQL.
- Dynamic visualizations in Grafana.
- Dockerized setup for seamless deployment.

---

## **Project Architecture**

```plaintext
weather-forecast-project/
├── dags/                            # Airflow DAGs and scripts
│   ├── weather_pipeline.py          # Main DAG
│   └── utils/                       # Functions for ETL tasks
├── data/                            # Sample or temporary data files
├── config/                          # Configuration files for Airflow, Grafana, and PostgreSQL
├── docker/                          # Docker setup for deployment
├── tests/                           # Unit tests for pipeline functions
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
└── .env                             # Environment variables
```

---

## **Technologies Used**

### **1. Apache Airflow**
- Orchestrates the ETL process.
- Manages the pipeline with DAGs (Directed Acyclic Graphs).

### **2. PostgreSQL**
- Stores historical weather data in a relational database.

### **3. Grafana**
- Creates interactive dashboards to visualize temperature trends.

### **4. Docker**
- Ensures reproducibility and easy deployment.

---

## **Setup Instructions**

### **Prerequisites**
- Docker and Docker Compose installed.
- Python 3.9 or later (for local development).
- Optional: Grafana and PostgreSQL installed locally.

### **1. Clone the Repository**
```bash
git clone https://github.com/your_username/weather-forecast-project.git
cd weather-forecast-project
```

### **2. Configure Environment Variables**
Create a `.env` file in the project root:
```plaintext
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=weather_data
API_URL=https://api.open-meteo.com/v1/forecast
LATITUDE=48.8566
LONGITUDE=2.3522
TIMEZONE=Europe/Paris
```

### **3. Install Dependencies**
For local development:
```bash
pip install -r requirements.txt
```

### **4. Run the Project with Docker**
```bash
docker-compose up -d
```

### **5. Access the Services**
- **Airflow**: [http://localhost:8080](http://localhost:8080) (default: `airflow`/`airflow`)
- **Grafana**: [http://localhost:3000](http://localhost:3000) (default: `admin`/`admin`)
- **PostgreSQL**: Port `5432` (use a database client like pgAdmin or DBeaver).

---

## **Pipeline Workflow**

1. **Extract Data**:
   - Fetch hourly weather data from the Open-Meteo API.
2. **Transform Data**:
   - Clean and format the API response into a structured table.
3. **Load Data**:
   - Insert the data into a PostgreSQL database.
4. **Visualize**:
   - Use Grafana to query the database and display temperature trends.

---

## **Testing**

Run unit tests for each component:
```bash
pytest tests/
```

---

## **Example Queries for Grafana**

Use this query in Grafana to visualize temperature data:
```sql
SELECT 
    timestamp AS "time", 
    temperature 
FROM hourly_temperature
ORDER BY timestamp;
```

---

## **Future Improvements**

- Add support for multiple locations.
- Implement real-time streaming using Kafka.
- Store additional weather metrics (e.g., humidity, wind speed).
- Deploy the pipeline to the cloud using AWS or GCP.

---

## **Contributors**

- [Your Name](https://github.com/your_username) - Project Lead

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
