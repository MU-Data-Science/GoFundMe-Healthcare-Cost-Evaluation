#!/usr/bin/env bash

# Downloading the Clincal Concept extraction source code.
cd ../Clinical_CE && git init
git remote add -f origin https://github.com/noc-lab/clinical_concept_extraction.git # Note: Last Commit Id: 030abacbf61c9c3a7e80879df14299595091c40b
git config core.sparseCheckout true
echo "clinical_concept_extraction/" >> .git/info/sparse-checkout
git pull origin master

# Minor bug fix required in ClincalCE source code.
FIXED_STMT="    dataset = tf.data.Dataset.from_generator("
echo "this is at $(pwd)"
sed -i "42s/.*/${FIXED_STMT}/" clinical_concept_extraction/pipeline.py

# Downloading the pretrained models
mkdir cce_assets && cd cce_assets

# 1) ELMo model
wget https://github.com/noc-lab/clinical_concept_extraction/releases/download/latest/elmo.tar.gz \
  && tar -xvf elmo.tar.gz \
  && rm -rvf elmo.tar.gz

# 2) Pretrained LSTM model
wget https://github.com/noc-lab/clinical_concept_extraction/releases/download/latest/blstm.tar.gz \
  && tar -xvf blstm.tar.gz \
  && rm -rvf blstm.tar.gz \
  && cd ..

# Setting the environment variable CCE_ASSETS
export CCE_ASSETS=$(pwd)/cce_assets

# Downloading the sentence segmentation tool.
wget https://github.com/noc-lab/simple_sentence_segment/releases/download/v0.1.3/simple_sentence_segment-0.1.3.tar.gz

# Installing the python libraries.
pip install -r requirements.txt
