ENHANCED RPG CHARACTER MANAGER
A character management system built with Python, utilizing Pandas for data analysis, Matplotlib for visualization, and Faker for procedural content generation.
Project Overview
This application allows users to create, manage, and analyze RPG characters using modern data science libraries. It provides tools for statistical reporting and visual attribute tracking.
Core Features
Procedural Generation: Uses Faker to generate unique names and detailed backstories.
Data Analysis: Pandas integration to calculate mean, median, and max stats across the character roster.
Visualizations: Matplotlib radar charts to visualize character attribute distributions.
Data Persistence: Save and load character databases using CSV format via Pandas.
Installation and Setup
Clone this repository to your local machine.
Ensure Python 3.8 or higher is installed.
Install the required dependencies:
pip install pandas matplotlib faker numpy
Run the application:
python main.py
Class Structure
Character: Core model storing name, race, class, and attributes.
StatisticalAnalyzer: Handles Pandas DataFrame operations and CSV exports.
DataVisualization: Manages Matplotlib plotting logic for radar and bar charts.
RandomGenerator: Uses the Faker library for procedural character creation.
