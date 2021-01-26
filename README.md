# GoFundMe-Healthcare-Cost-Evaluation
Online fundraising platforms are now becoming a very popular means to raise money for charity. Hence, through this project, we evaluate the use of the most popular fundraising platform - [GoFundMe](https://www.gofundme.com/) for covering health care related costs.

## Environment Setup
Requirements:
   * [Python](https://www.python.org/) (version = 3.6)
   * [Anaconda](https://www.anaconda.com/) ([installation steps](https://gist.github.com/Arun-George-Zachariah/3cfd2e249b5eda609d5c0f50d0c4db43)). 

To setup the models and install the required libraries:
```
cd Scripts/ && ./node_setup.sh
``` 

Make sure the variables `DOWNLOAD_DIR` and `PRE_COMPUTED_DATA_URL` are pointing to the correct input files.

To set the environment variable required for Clinical Concept Extraction.
```
export CCE_ASSETS=$(pwd)/Clinical_CE/cce_assets
```

## Results
To reproduce the results, follow the steps described [here](Validate_Data/README.md)

## Publication
Suveen Angraal, Arun Zachariah, Raaisa Raaisa, Rohan Khera, Praveen Rao, Harlan M Krumholz, and John A Spertus - **Evaluation of Internet-Based Crowdsourced Fundraising to Cover Health Care Costs in the United States.** In JAMA Network Open, 4(1), 2021 [[PDF](https://jamanetwork.com/journals/jamanetworkopen/articlepdf/2774737/angraal_2021_ld_200198_1609274555.84741.pdf)]

## Data Request
If you need the data used for the above publication, please contact the lead author.

## References
* [GoFundMe Web Scraper](https://github.com/lmeninato/GoFundMe)
* [Clinical Concept Extraction with Contextual Word Embedding](https://github.com/noc-lab/clinical_concept_extraction)
* [BioWordVec: Improving Biomedical Word Embeddings with Subowrd Information and MeSH](https://github.com/ncbi-nlp/BioWordVec.git)
* [FusionCharts](https://www.fusioncharts.com/)
