import sys
import argparse
import glob
import pandas as pd

states_dict = {"AL":0, "AK":0, "AZ":0, "AR":0, "CA":0, "CO":0, "CT":0, "DC":0, "DE":0, "FL":0, "GA":0,
          "HI":0, "ID":0, "IL":0, "IN":0, "IA":0, "KS":0, "KY":0, "LA":0, "ME":0, "MD":0,
          "MA":0, "MI":0, "MN":0, "MS":0, "MO":0, "MT":0, "NE":0, "NV":0, "NH":0, "NJ":0,
          "NM":0, "NY":0, "NC":0, "ND":0, "OH":0, "OK":0, "OR":0, "PA":0, "RI":0, "SC":0,
          "SD":0, "TN":0, "TX":0, "UT":0, "VT":0, "VA":0, "WA":0, "WV":0, "WI":0, "WY":0}

# 2000 Census data
# states_population_dict = {"AL":4447100, "AK":626932, "AZ":5130632, "AR":2673400, "CA":33871648, "CO":4301261, "CT":3405565, "DE":783600, "FL":15982378, "GA":8186453,
#                           "HI":1211537, "ID":1293953, "IL":12419293, "IN":6080485, "IA":2926324, "KS":2688418, "KY":4041769, "LA":4468976, "ME":1274923, "MD":5296486,
#                           "MA":6349097, "MI":9938444, "MN":4919479, "MS":2844658, "MO":5595211, "MT":902195, "NE":1711263, "NV":1998257, "NH":1235786, "NJ":8414350,
#                           "NM":1819046, "NY":18976457, "NC":8049313, "ND":642200, "OH":11353140, "OK":3450654, "OR":3421399, "PA":12281054, "RI":1048319, "SC":4012012,
#                           "SD":754844, "TN":5689283, "TX":20851820, "UT":2233169, "VT":608827, "VA":7078515, "WA":5894121, "DC":572059, "WV":1808344, "WI":5363675, "WY":493782}

# 2010 Census data
states_population_dict = {"AL":4874747,"AK":739795,"AZ":7016270,"AR":3004279,"CA":39536653,"CO":5607154,"CT":3588184,"DC":693972,"DE":961939,"FL":20984400,"GA":10429379,
                          "HI":1427538,"ID":1716943,"IL":12802023,"IN":6666818,"IA":3145711,"KS":2913123,"KY":4454189,"LA":4684333,"ME":1335907,"MD":6052177,
                          "MA":6859819,"MI":9962311,"MN":5576606,"MS":2984100,"MO":6113532,"MT":1050493,"NE":1920076,"NV":2998039,"NH":1342795,"NJ":9005644,
                          "NM":2088070,"NY":19849399,"NC":10273419,"ND":755393,"OH":11658609,"OK":3930864,"OR":4142776,"PA":12805537,"RI":1059639,"SC":5024369,
                          "SD":869666,"TN":6715984,"TX":28304596,"UT":3101833,"VT":623657,"VA":8470020,"WA":7405743,"WV":1815857,"WI":5795483,"WY":579315}

def read_CSV(inp):
    """
    Combines all CSV files to a single CSV file.

    Args:
        inp_dir: Directory listing the input files that needs to be combined.
    """
    all_filenames = [i for i in glob.glob(inp)]
    combined_csv = pd.concat([pd.read_csv(f, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) for f in all_filenames ])

    return combined_csv

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='Geographical distribution of the use of online crowdsourced fundraising for medical conditions in the US.')
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
        print(len(rows))

        # Iterating over the input data rows.
        for row in rows:
            try:
                is_US = False
                # Splitting the location.
                stripped_loc = str(row["Location"]).split(",")
                for data in stripped_loc:
                    # Verifying if the state belongs to any of the ones mentioned abo
                    if data.strip() in states_dict:
                        is_US = True
                        # Incrementing the state count.
                        states_dict[data.strip()] = states_dict[data.strip()] + 1
                        break
                if not is_US:
                    print("extract_medical_data.py :: Skipping the location :: ", row["Location"])
            except:
                print("extract_medical_data.py :: Exception encountered for Location :: ", row["Location"])

        print("States data :: ", states_dict)

        # Normalizing the data
        normalized_states_dict = {}
        for state in states_dict:
            norm_pop = (states_dict[state]/states_population_dict[state]) * 100000
            normalized_states_dict[state] = norm_pop

        # Sorting the data.
        sorted_states_dict = sorted(normalized_states_dict.items(), key=lambda kv: kv[1], reverse=True)
        print("extract_medical_data.py :: sorted_states_dict :: ", sorted_states_dict)

        print("States with most fundraisers per 100,000 population :: ", sorted_states_dict[:10])
        print("States with the lowest fundraisers per 100,000 population :: ", sorted_states_dict[-10:])

# Output
# Sorted_states_dict ::  [('ME', 139.38095990214887), ('AK', 137.2001703174528), ('MT', 134.79385393334368), ('OR', 131.14394792284207), ('WA', 129.629127016695), ('UT', 127.8598815603548), ('CO', 127.53350451940504), ('ND', 127.08616574418879), ('ID', 124.46540158875398), ('NH', 121.09071004881609), ('VT', 121.06013401597352), ('MN', 116.03832151670748), ('WY', 113.75503827796621), ('FL', 104.44425382665219), ('AZ', 103.61630895048222), ('NV', 102.76717547703682), ('SD', 100.0384055487969), ('TX', 96.88885861504612), ('KS', 91.31094018343887), ('HI', 91.27602907943607), ('NM', 89.36482014491851), ('OK', 88.75911250045792), ('RI', 88.7094567112007), ('MA', 88.69038672886268), ('NE', 88.01734931325635), ('GA', 87.0138097388157), ('MO', 83.91221310365269), ('MI', 82.88237538458698), ('SC', 81.2440328327796), ('VA', 81.1332204646506), ('NC', 79.73976336407577), ('CT', 79.70605743741123), ('CA', 78.7370645663911), ('TN', 78.58863273051276), ('WI', 77.52589387286616), ('IA', 77.3751943519287), ('IN', 76.06327336369465), ('IL', 74.98033709203615), ('MD', 74.76648485330155), ('AR', 74.19417437594844), ('NJ', 72.95424957948593), ('LA', 72.02733025171352), ('PA', 71.60964823263562), ('DC', 71.47262425573366), ('OH', 70.24851764048353), ('DE', 67.46789557341994), ('NY', 67.29674787634627), ('AL', 66.75218221581551), ('WV', 62.61506274998526), ('KY', 59.337401264293), ('MS', 54.58932341409471)]
# States with most fundraisers per 100,000 population ::  [('ME', 139.38095990214887), ('AK', 137.2001703174528), ('MT', 134.79385393334368), ('OR', 131.14394792284207), ('WA', 129.629127016695), ('UT', 127.8598815603548), ('CO', 127.53350451940504), ('ND', 127.08616574418879), ('ID', 124.46540158875398), ('NH', 121.09071004881609)]
# States with the lowest fundraisers per 100,000 population ::  [('LA', 72.02733025171352), ('PA', 71.60964823263562), ('DC', 71.47262425573366), ('OH', 70.24851764048353), ('DE', 67.46789557341994), ('NY', 67.29674787634627), ('AL', 66.75218221581551), ('WV', 62.61506274998526), ('KY', 59.337401264293), ('MS', 54.58932341409471)]