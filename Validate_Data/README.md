## Execution steps
1. Since the data was extracted during mid 2019, we consider only the data until 2018. To consolidate the data from inception until 2018:
    ```
    python extract_2018_data.py
    ```

2. As we are focused on medical fundraisers, we extract all medical fundraisers from inception until 2018:
    ```
    python extract_medical_data.py
    ```

3. For this project, we evaluate the fundraisers in the US. Hence to extract medical fundraisers from inception until 2018 orginagted in the US:
    ```
    python extract_us_medical_data.py
    ```

4. To obtain the total online fundraisers in the US from 2010-2018:
    ```
    python fundraising_campaigns.py
    ```

5. To obtain the total online fundraisers in the US from 2010-2018 for different medical conditions:
    * Cancer
        ```
        python fundraising_category_campaigns.py  -cat cancer
        ```
    * Neurological conditions
        ```
        python fundraising_category_campaigns.py  -cat neurological
        ```
    * Trauma/Injury
        ```
        python fundraising_category_campaigns.py  -cat trauma
        ```
    * Cardiovascular conditions
        ```
        python fundraising_category_campaigns.py  -cat cardiovascular
        ```

6. To obtain the geographical distribution of the use of online crowdsourced fundraising for medical conditions in the U.S.:
    ```
    python state_fundraisers.py
    ```

7. To extract text data for categorization:
    ```
    python extract_medical_text.py
    ```
   
8. To categorize the extracted test data
    ```
    cd ../Classify_Data && python classify.py
    ```