#!/usr/bin/env bash

# Configurations.
DOWNLOAD_DIR=""
PRE_COMPUTED_DATA_URL=""

# Constants
PROJECT_DIR=$(pwd)/..
USER=${USER}

# Installing the requirements.
pip install -r ${PROJECT_DIR}/Scripts/requirements.txt

# Creating the data directory.
mkdir ${PROJECT_DIR}/data && cd ${PROJECT_DIR}/data

# Downloading the datasets.
wget ${DOWNLOAD_DIR} -O GoFundMeData.tar && tar -xvf GoFundMeData.tar && rm -rvf GoFundMeData.tar

# Downloading the pre-computed output for visualization and analytics.
wget ${PRE_COMPUTED_DATA_URL} -O US_Medical_Data_Output.csv

# Setting up Clinical CE.
cd ${PROJECT_DIR}/Scripts && bash setup_clinical_ce.sh

# Downloading the Models
mkdir ${PROJECT_DIR}/models && cd ${PROJECT_DIR}/models
wget https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/BioSentVec/BioWordVec_PubMed_MIMICIII_d200.bin
