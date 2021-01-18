import sys
import argparse
import glob
import csv
import pandas as pd

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def read_CSV(inp):
    all_filenames = [i for i in glob.glob(inp)]
    combined_csv = pd.concat([pd.read_csv(f, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) for f in all_filenames ])

    return combined_csv

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='Extract all medical fundraisers from inception until 2018 originated in the US.')
    parser.add_argument('-data', default="../data/Medical_Data.csv", metavar='data', help='Directory containing the csv data.', required=False)
    args = parser.parse_args()

    if args.data == None:
        parser.print_help()
        sys.exit(1)
    else:
        # Combine the data file
        data = read_CSV(args.data)

        # Converting the dataframe to a list.
        rows = data.to_dict('records')
        print(len(rows))
        # Out file.
        out_file = open("../data/US_Medical_Data.csv", "w+")
        w = csv.DictWriter(out_file, rows[0].keys())
        w.writeheader()

        # Extracting the medical posts
        for row in rows:
            try:
                if str(row["Location"]).split(",").__len__() == 2 and str(row["Location"]).split(",")[1].strip().__len__() == 2 and str(row["Location"]).split(",")[1].strip() in states:
                    w.writerow(row)
                elif " US" in row["Location"]:
                    w.writerow(row)
                else:
                    print("Skipping the location :: ", row["Location"])
            except:
                print("extract_medical_data.py :: Exception enccountered for Location :: ", row["Location"])
        out_file.close()
