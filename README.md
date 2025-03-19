# Financial Data Pipeline and Predictive Analytics
This project implements an automated pipeline that collects financial data from multiple sources (OANDA and Yahoo Finance), cleans it, and stores it in an H5 database. The pipeline is orchestrated using Apache Airflow to run on a daily interval. The project focuses on ensuring data quality for predictive analytics and financial analysis.

### Features
- **Data Collection**: Fetches financial data from OANDA broker and Yahoo Finance (yFinance).
- **Data Storage**: Stores collected data in an H5 database for easy querying and analysis.
- **Data Cleaning**: Cleans raw data to ensure high quality, such as removing outliers, handling missing values, and ensuring consistency.
- **Orchestration**: Uses Apache Airflow for scheduling and managing the pipeline.
- **Daily Execution**: The pipeline runs daily, ensuring up-to-date and accurate data is available for analysis.
