# OpenWeatherMap API Data Pipeline

This project involves building a data pipeline to collect weather data from the OpenWeatherMap API, preprocessing the data, training multiple machine learning models, and deploying the best-performing model in a web application. The entire pipeline is orchestrated using Apache Airflow with regular updates from the API.

## Repository Structure

- `dags/`: Apache Airflow DAG configuration files and the scripts directory.
- `dags/scripts/streamlit`: Holds files related to the web application .
- `dags/scripts/pickle_files`: Stores serialized machine learning models.
- `dags/scripts/dataset`: Confine the datasets.

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/openweathermap-data-pipeline.git
   ```

2. Install required dependencies:

   ```bash
   docker compose up 
   ```
   ### Upon successful execution, the containers will be launched. Here is the expected outcome:
   
   ![image](https://github.com/MouhibMoughtanim/Continuous-Training-Pipeline-with-Apache-Airflow-and-Streamlit/assets/101598112/a6d19f17-0998-489f-a0fe-d92461972abc)


4. Access the Airflow UI at `http://localhost:8080` and trigger the DAG.

   - After triggering the DAG, you can monitor the progression of our pipeline by navigating to the Apache Airflow UI. Follow these steps:

   - Access the Airflow UI at http://localhost:8080 in your web browser.

   - Log in with the appropriate credentials.

   - In the Airflow UI, locate the DAG related to your project (e.g., openweathermap_data_pipeline).

   - Click on the DAG to view its details.

   - You'll find information such as the status of each task, execution times, and any logs generated during the process.

   - To monitor the evolution of the pipeline, observe the flow of tasks and check for any errors or successful completions.

   - Additionally, you can inspect individual task logs and outputs for more detailed information.

### This interface provides a comprehensive view of the pipeline's execution and allows you to troubleshoot or analyze the performance of each component.

   ![image](https://github.com/MouhibMoughtanim/Continuous-Training-Pipeline-with-Apache-Airflow-and-Streamlit/assets/101598112/39a8b171-6db8-41be-92fc-aa11a1e8d157)


## Contributors

- Mouhib Moughtanim
- Akram Fouguir
- Salma Arbaoui

Feel free to contribute, open issues, or provide feedback to enhance this data pipeline project. Happy coding!
