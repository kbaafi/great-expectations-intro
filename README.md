# Data Quality Evaluation using Great Expectations

This repo presents an introductory demonstration on how to use Great Expectations as a Data Quality Evaluation tool and incorporate it in your Data Engineering pipelines. In the python notebooks you will find demonstrations on:
* How to setup an Ephemeral Data Context for your Great Expectations Project
* How to setup a Batch Request
* Use the Great Expectations Validator for in-line data quality evaluation of a Pandas dataframe
* Use Expectation Suites to define a number of Expectations
* Use Checkpoints to run your Expectations and present the Validation results
* Setup Expectations in yaml format and use a Great Expectations wrapper to run tests against a Pandas dataframe

# Dataset: NYC Yellow Taxi Trip Data
In this demonstration, the NYC Yello Taxi Trip Data will be used. The dataset can be downloaded from here: [https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). During experimentation for this exercise, the January 2023 monthly data was used. But it is safe to assume that the experiments in the notebooks will work for other months as well. The data is saved as `parquet` and can be placed in a `data` folder in the home directory of this repository.

# Topics to be discussed
The following will be discussed
* **Domain Knowledge:** Taking a look at the data, can we conceptualize a number of expectations based at least, on what we think we know about this data
* **Great Expectations Concepts**
* **Documentation of Expectations:** How do we document the expectations that we have about this dataset
* **Hands-on-1 | Using the Validator Object together with Checkpoints:** We use the validator object to create expectations and an expectation suite and subsequently evaluate the quality of the data in question
* **Hands-on-2 | Using the Expectations Configurations:** We use a list of expectation configurations defined as  a list of python dictionaries to define expectations in an expectation suite and validate the suite using a Checkpoint
* **Hands-on-3 | Expectations as Yaml:** We explore the use of yaml as a configuration vehicle to setup and validate our expectations
* **Analysis of the Checkpoint results:** We analyse the results of the checkpoint validation and try to figure out what useful data can be gleaned from the report


# Setting up the Development Environment and Running the Experimentation Notebooks
## Data
Refer to the section **Dataset: NYC Yellow Taxi Trip Data**
## Setting up the local environment
1. Create a python virtual environment in the home folder of this repo using the command `$ python -m venv venv`
2. Install dependencies by running `$ pip install -r requirements.txt`

