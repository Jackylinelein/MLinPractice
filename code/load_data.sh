#!/bin/bash

# create directory if not yet existing
mkdir -p data/raw/

# download the three csv files if not yet existing

DATASET_1=data/raw/data_analysis.csv
DATASET_2=data/raw/data_science.csv
DATASET_3=data/raw/data_visualization.csv


if test -f "$DATASET_1"; then
    echo "DATASET_1 exist already"
    
else 
    
    wget -nv https://myshare.uni-osnabrueck.de/f/3e5276caf72b46e7ace2/?dl=1 -O data/raw/data_analysis.csv
fi


if test -f "$DATASET_2"; then
    echo "DATASET_2 exist already"
    
else 
    
    wget -nv https://myshare.uni-osnabrueck.de/f/e620aff7719948d18a52/?dl=1 -O data/raw/data_science.csv
fi


if test -f "$DATASET_3"; then
    echo "DATASET_3 exist already"
    
else 
    
   wget -nv https://myshare.uni-osnabrueck.de/f/9ddaab064c68483e9bff/?dl=1 -O data/raw/data_visualization.csv
fi









