import glob
import pandas as pd
import csv

def read_CSV(all_filenames):
    combined_csv = pd.concat([pd.read_csv(f, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) for f in all_filenames ])

    return combined_csv

if __name__ == '__main__':
    # Read the first CSV, that was scrapped on Sept 2019
    all_filenames = [i for i in glob.glob("../data/1_data.csv")]
    data = read_CSV(all_filenames)

    # Converting the dataframe to a list.
    rows = data.to_dict('records')

    # Getting the header data
    header_data = list(rows[0].keys())

    # Appending the classifier output header.
    header_data.append("Origin_Year")

    # Writing the header to the file.
    out_file = open("../data/Combined_Data_2018.csv", "w+")
    w = csv.DictWriter(out_file, header_data)
    w.writeheader()

    # Iterating over all the elements in the rows
    for row in rows:
        try:
            fundraising_len = row['Length_of_Fundraising']

            # Skipping those campaings that were created in 2019
            if fundraising_len / 30 < 9:
                print("extract_2018_data.py 1:: Skipping for the fundraising length :: ", fundraising_len)
                continue

            # Computing the year of fundraising.
            year = 2018 - int(((fundraising_len / 30) - 9) / 12)

            # Adding the year to the output.
            row["Origin_Year"] = year

            w.writerow(row)

        except:
            print("extract_2018_data.py :: Exception encountered. Continuing")

    # Read the first CSV, that was scrapped on Setp 2019
    all_filenames = ["../data/2_data.csv", "../data/3_data.csv", "../data/4_data.csv", "../data/5_data.csv",
                     "../data/6_data.csv", "../data/7_data.csv", "../data/8_data.csv", "../data/9_data.csv",
                     "../data/10_data.csv", "../data/11_data.csv", "../data/12_data.csv", "../data/13_data.csv",
                     "../data/14_data.csv", "../data/15_data.csv", "../data/16_data.csv", "../data/17_data.csv",
                     "../data/18_data.csv", "../data/19_data.csv", "../data/20_data.csv", "../data/21_data.csv",
                     "../data/22_data.csv", "../data/23_data.csv", "../data/24_data.csv", "../data/25_data.csv",
                     "../data/26_data.csv"]
    data = read_CSV(all_filenames)

    # Converting the combined dataframe to a list.
    rows = data.to_dict('records')

    # Iterating over all the elements in the rows
    for row in rows:
        try:
            fundraising_len = row['Length_of_Fundraising']

            # Skipping those campaings that were created in 2019
            if fundraising_len / 30 < 4:
                print("extract_2018_data.py :: Skipping for the fundraising length :: ", fundraising_len)
                continue

            # Computing the year of fundraising.
            year = 2018 - int(((fundraising_len / 30) - 4) / 12)

            # Adding the year to the output.
            row["Origin_Year"] = year
            w.writerow(row)

        except:
            print("extract_2018_data.py :: Exception encountered. Continuing")

    print("extract_2018_data.py :: main :: Done!")