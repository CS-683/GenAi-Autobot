# AutoBot AI - autonomus ai agent

Autobot ai is an autonomus ai agent which is being designed to check to capabilites of varaious llms to understand complex queries which requires planning of multiples tasks which can't be done in one go, plannig appropiate tools which are available and required to complete individual taks and executing those tasks.
This project is built for course Generative AI offered by parimala mam at IIT Mandi in Odd semester 2024-25

### Requirements

- Anaconda 3 (install from here: https://docs.anaconda.com/anaconda/install/)
- Gcloud cli tool. (see: https://cloud.google.com/sdk/docs/install )
- Mongodb, mongosh, mongoimport (I'll recommend to install using docker)
- account on google cloud platform and the create/select a project.

### Setup

- Clone the repositry
- Create a conda environment and install follwoing dependencies installed `conda env create --name generativeai`

  - python-dotenv
  - google-cloud-aiplatform
  - pymongo
  - vertexai

- Autheinticate to gcloud cli in project folder `gcloud auth application-default login`
- import data in mogodb using follwoiing command `mongoimport --db sample_supplies --collection sales --file <file_path> --jsonArray`
- Run the python program.

  - test.py make a sample request to gemini
  - tools/test.py to test mongo connections
