import sys
import argparse
import glob
import pandas as pd

def read_CSV(inp):
    all_filenames = [i for i in glob.glob(inp)]
    combined_csv = pd.concat([pd.read_csv(f, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) for f in all_filenames ])

    return combined_csv

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='Preprocess to extract text from a folder of csv files.')
    parser.add_argument('-data', default="../data/US_Medical_Data.csv", metavar='data', help='Directory containing the csv data.', required=False)
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
        out_file = open("../data/Medical_Text_Data.txt", "w+")

        # Extracting the medical posts
        for row in rows:
            try:
                out_file.write(row["Text"] + "\n")
            except:
                out_file.write("\n")


        out_file.close()
