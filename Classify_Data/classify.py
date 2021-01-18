import sys
sys.path.append("../Clinical_CE")

import argparse
import operator
from gensim.models.wrappers import FastText
from extract_entities import get_entities

CATEGORIES = ['cardiovascular', 'cancer', 'trauma', 'neurological', 'renal', 'respiratory']
THRESHOLD_SCORE = 0.4
emb_model = None

def load_model():
    global emb_model
    emb_model = FastText.load_fasttext_format('../models/BioWordVec_PubMed_MIMICIII_d200.bin')

if __name__ == '__main__':
    # Reading the input
    parser = argparse.ArgumentParser(description='Preprocess to extract text from a folder of csv files.')
    parser.add_argument('-data', default="../data/Medical_Text_Data.txt", metavar='data', help='Directory containing the csv data.', required=False)
    args = parser.parse_args()

    if args.data == None:
        parser.print_help()
        sys.exit(1)
    else:
        # Loading the embedding model
        load_model()

        # Out file.
        out_file = open("../data/classifier_output.csv", "w+")

        # Reading the data from the file.
        with open(args.data) as topo_file:
            for line in topo_file:
                # Extracting all medical entities from the text.
                problem_lst = []
                try:
                    problem_lst = get_entities(line)
                except:
                    print("classify.py :: Exception encountered while extracting the entities for the text :: ", line)

                # Dictionary for each case.
                prob_dict = {}

                for problem in problem_lst:
                    # Dictionary for each category.
                    cat_dict = {}

                    # Measure their distance for each category.
                    for category in CATEGORIES:
                        try:
                            cat_dict[category] = emb_model.similarity(w1=category, w2=problem)
                        except:
                            print("classify.py :: Exception encountered while calculating similarity")

                    if cat_dict:
                        prob_dict[problem] = cat_dict

                # Writing the dictionary to the file for auditing.
                print(prob_dict)
                out_file.write(line + "," + str(prob_dict).replace(",", ";"))

                # Dictionary to hold the final results for each category.
                final_dict = {}

                # Iterating over the categories for averaging.
                for category in CATEGORIES:
                    sum = 0;
                    for prob in prob_dict:
                        sum += prob_dict[prob][category]

                    final_dict[category] = sum/len(prob_dict) if len(prob_dict) > 0 else 0

                # Sorting the final dictionary.
                sorted_d = sorted(final_dict.items(), key=operator.itemgetter(1))
                print("classify.py :: sorted_d :: ", sorted_d)

                # Final category selection.
                if float(sorted_d[-1][1]) > THRESHOLD_SCORE:
                    category = sorted_d[-1][0]
                else:
                    category = "others"

                # Noting the final category selected.
                print("classify.py :: Predicted Category :: ", category)
                out_file.write("," + category + "\n")

        # Closing the output file.
        out_file.close()
