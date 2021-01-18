import argparse
import glob
import pandas as pd

def read_CSV(inp):
    all_filenames = [i for i in glob.glob(inp)]
    combined_csv = pd.concat([pd.read_csv(f, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) for f in all_filenames ])
    return combined_csv

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='To obtain the online crowdsources fundraising for different medical conditions.')
    parser.add_argument('-data', default="../data/US_Medical_Data_Output.csv", metavar='data', help='Directory containing the csv data.', required=False)
    parser.add_argument('-cat', default="cancer", metavar='category', help='Category to be considerded.', required=False)
    args = parser.parse_args()

    # Read the first CSV, that was scrapped on Sept 2019
    data = read_CSV(args.data)

    # Converting the dataframe to a list.
    rows = data.to_dict('records')

    # Final_Dictionary
    cat_dict = {}

    # Iterating over all the elements in the rows
    for row in rows:
        try:
            fundraising_len = row['Length_of_Fundraising']

            # Computing the year of fundraising.
            year = 2018 - int(((fundraising_len / 30) - 9) / 12)

            # Adding to the total list of the particular category.
            if row["Classifier_Output"] == args.cat:
                if year in cat_dict:
                    cat_dict[year] = cat_dict[year] + 1
                else:
                    cat_dict[year] = 1

        except:
            print("fundraising_campaigns.py :: Exception encountered for the row :: ", row)

    # Sorting the dictionary based on the year
    sorted_total_dict = sorted(cat_dict.items(), key=lambda kv: kv[1], reverse=False)

    print("Total Crowdsourced Online Fundraising Campaigns :: ", sorted_total_dict)

# Output
# Cancer:
# Total Crowdsourced Online Fundraising Campaigns ::  [(2010, 15), (2011, 86), (2012, 416), (2013, 1646), (2014, 4423), (2016, 11888), (2015, 13690), (2017, 20404), (2018, 56175)]
# Neurological conditions:
# Total Crowdsourced Online Fundraising Campaigns ::  [(2010, 7), (2011, 42), (2012, 235), (2013, 883), (2014, 2348), (2016, 5961), (2015, 6895), (2017, 9857), (2018, 27895)]
# Trauma/Injury:
# Total Crowdsourced Online Fundraising Campaigns ::  [(2010, 4), (2011, 28), (2012, 159), (2013, 717), (2014, 2136), (2016, 6987), (2015, 7114), (2017, 11764), (2018, 30237)]
# Cardiovascular conditions:
# Total Crowdsourced Online Fundraising Campaigns ::  [(2010, 2), (2011, 6), (2012, 26), (2013, 152), (2014, 398), (2016, 1118), (2015, 1383), (2017, 2038), (2018, 6170)]
