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

2. Navigate to the Project Directory::

   ```bash
   cd openweathermap-data-pipeline
   ```

3. Start Docker Containers:

   ```bash
   docker compose up
   ```
   ### Upon successful execution, the containers will be launched. Here is the expected outcome:
   
   ![image](https://github.com/MouhibMoughtanim/Continuous-Training-Pipeline-with-Apache-Airflow-and-Streamlit/assets/101598112/a6d19f17-0998-489f-a0fe-d92461972abc)


4. Access the Airflow UI at `http://localhost:8080` and trigger the DAG.
   



## Monitoring the Pipeline Progression

1. **Access the Airflow UI:**
   - Open your web browser and go to [http://localhost:8080](http://localhost:8080).

2. **Login:**
   - Log in with the following credentials:
        - Username: airflow
        - Password: airflow
3. **Locate the DAG:**
   - In the Airflow UI, find the DAG associated with your project (e.g., `openweathermap_data_pipeline`).

4. **View DAG Details:**
   - Click on the DAG to access detailed information.

5. **Check Task Status and Execution Times:**
   - Within the DAG details, observe the status of each task, their execution times, and any generated logs.

6. **Monitor Pipeline Evolution:**
   - Keep track of the flow of tasks to monitor the overall progression of the pipeline.

7. **Inspect Task Logs and Outputs:**
   - For more in-depth information, you can inspect individual task logs and outputs.



### This interface provides a comprehensive view of the pipeline's execution and allows you to troubleshoot or analyze the performance of each component.

   ![image](https://github.com/MouhibMoughtanim/Continuous-Training-Pipeline-with-Apache-Airflow-and-Streamlit/assets/101598112/39a8b171-6db8-41be-92fc-aa11a1e8d157)


## Contributors

- Mouhib Moughtanim
- Akram Fouguir
- Salma Arbaoui

Feel free to contribute, open issues, or provide feedback to enhance this data pipeline project. Happy coding!