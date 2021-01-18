import sys
import argparse
import glob
import nltk
import csv
import pandas as pd

def read_CSV(inp):
    all_filenames = [i for i in glob.glob(inp)]
    combined_csv = pd.concat([pd.read_csv(f, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) for f in all_filenames ])

    return combined_csv

def normalize_text(text):
    """
     Cleans up an input text by converting all the characters to lower case and by removing
     punctuations and non-UTF characters.
     Args:
        text: Directory listing the input files that needs to be cleaned and massaged.
     Returns:
        A cleaned version of the original text.
    """
    # Tokenizer.
    regex_tokenizer = nltk.RegexpTokenizer("\w+")

    # Convert text to lower case.
    text = str(text).lower()

    # Remove non-UTF characters.
    text = text.encode("utf-8", "ignore").decode()

    # Remove punctuations.
    text = " ".join(regex_tokenizer.tokenize(text))

    return text

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='Extract all  medical fundraisers from inception until 2018.')
    parser.add_argument('-data', default="../data/Combined_Data_2018.csv", metavar='data', help='Directory containing the csv data.', required=False)
    args = parser.parse_args()

    if args.data == None:
        parser.print_help()
        sys.exit(1)
    else:
        # Combine the data file
        data = read_CSV(args.data)

        # Converting the dataframe to a list.
        rows = data.to_dict('records')

        # Out file.
        out_file = open("../data/Medical_Data.csv", "w+")
        w = csv.DictWriter(out_file, rows[0].keys())
        w.writeheader()

        # Extracting the medical posts
        for row in rows:
            try:
                if row["Category"] == "Medical":
                    row["Text"] = normalize_text( row["Text"].replace('\n','').strip())
                    w.writerow(row)
            except:
                print("extract_medical_data.py :: Exception encountered for row :: ", row["Text"])
        out_file.close()