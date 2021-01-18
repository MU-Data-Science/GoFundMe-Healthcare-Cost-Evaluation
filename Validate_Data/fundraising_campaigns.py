import glob
import pandas as pd

def read_CSV(all_filenames):
    combined_csv = pd.concat([pd.read_csv(f, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) for f in all_filenames ])

    return combined_csv

if __name__ == '__main__':
    # Read the first CSV, that was scrapped on Sept 2019
    all_filenames = [i for i in glob.glob("../data/1_data.csv")]
    data = read_CSV(all_filenames)

    # Converting the dataframe to a list.
    rows = data.to_dict('records')

    # Final_Dictionary
    total_dict = {}
    medical_dict = {}

    # Iterating over all the elements in the rows
    for row in rows:
        try:
            fundraising_len = row['Length_of_Fundraising']

            # Skipping those campaings that were created in 2019
            if fundraising_len / 30 < 9:
                print("fundraising_campaigns.py :: Skipping for the fundraising length :: ", fundraising_len)
                continue

            # Computing the year of fundraising.
            year = 2018 - int(((fundraising_len / 30) - 9) / 12)

            # Adding to the total list of campaigning events.
            if year in total_dict:
                total_dict[year] = total_dict[year] + 1
            else:
                total_dict[year] = 1

            # Adding to the total list of medical campaigning events.
            if row["Category"] == "Medical":
                if year in medical_dict:
                    medical_dict[year] = medical_dict[year] + 1
                else:
                    medical_dict[year] = 1

        except:
            print("fundraising_campaigns.py :: Exception encountered for the row :: ", row)

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
    print("Length of rows :: ", len(rows))

    # Iterating over all the elements in the rows
    for row in rows:
        try:
            fundraising_len = row['Length_of_Fundraising']

            # Skipping those campaings that were created in 2019
            if fundraising_len / 30 < 4:
                print("fundraising_campaigns.py :: Skipping for the fundraising length :: ", fundraising_len)
                continue

            # Computing the year of fundraising.
            year = 2018 - int(((fundraising_len / 30) - 4) / 12)

            # Adding to the total list of campaigning events.
            if year in total_dict:
                total_dict[year] = total_dict[year] + 1
            else:
                total_dict[year] = 1

            # Adding to the total list of medical campaigning events.
            if row["Category"] == "Medical":
                if year in medical_dict:
                    medical_dict[year] = medical_dict[year] + 1
                else:
                    medical_dict[year] = 1

        except:
            print("fundraising_campaigns.py :: Exception encountered for the row :: ", row)

    # Sorting the dictionary based on the year
    sorted_total_dict = sorted(total_dict.items(), key=lambda kv: kv[1], reverse=False)
    sorted_medical_dict = sorted(medical_dict.items(), key=lambda kv: kv[1], reverse=False)

    print("Total Crowdsourced Online Fundraising Campaigns :: ", sorted_total_dict)
    print("Total Crowdsourced Online Fundraising Campaigns For Medical Conditions :: ", sorted_medical_dict)

# Output
# Total Crowdsourced Online Fundraising Campaigns ::  [(2010, 93), (2011, 699), (2012, 3784), (2013, 15514), (2014, 70091), (2015, 145329), (2016, 183627), (2017, 187037), (2018, 450281)]
# Total Crowdsourced Online Fundraising Campaigns For Medical Conditions ::  [(2010, 42), (2011, 235), (2012, 1140), (2013, 4689), (2014, 25902), (2015, 39464), (2016, 50744), (2017, 66036), (2018, 119373)]