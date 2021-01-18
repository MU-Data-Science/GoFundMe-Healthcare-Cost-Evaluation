import sys
sys.path.append("../")

import nltk
from clinical_concept_extraction import pipeline

def tokenize_text(text):
    tokens_span =  nltk.tokenize.TreebankWordTokenizer().span_tokenize(text)
    tokens = []
    for span in tokens_span:
        tokens.append(text[span[0]:span[1]])

    return tokens

def get_entities(text):
    # Tokenizing the text
    tokens = tokenize_text(text)

    # Getting the annotation.
    annotations = pipeline.get_annotation([tokens])[0]

    # Constructing a list of entities
    str_list = []
    for i in range(0, len(annotations)):
        print(annotations[i])
        if "problem" in annotations[i]:
            str_list.append(tokens[i])
            if i < len(annotations)-1:
                if "problem" not in annotations[i + 1]:
                    str_list.append("::")

    return list(map(str.strip, ' '.join(str_list).split("::")))[:-1]

if __name__ == '__main__':
    text = "on april this year my sister ann was given news that would change her life forever ann age 23 was diagnosed with malignant melanoma a big c of the skin that s only dominant to caucasian people and a very rare case for asian age 50 below what a shocking news for my family and her friends i could not quite think how in the world she got it and why it has to be her of all people she had been working in singapore for 2 months already when ann found out about her condition soon after the news ann went back to the phils to have herself operated in the pelvis area after the surgery at st lukes medical centre oncologists advised her to undergo pet scan this type of scan enables them to see if there are traces of cancer cells left on her body thankfully the doctors had found none but having negative result means not having any treatment at all she was strongly recommended to have a maintenance treatment slightly similar to chemo therapy for 52 weeks 1 year to prevent relapse recurrence ann s treatment is done 3x every week an iv injection of interferon that costs 550usd per pen which can only last for a week around 20thou plus pesos per week or 80 100thousand per month aside from the previous unfinished medical bills 34 000sgd from thomson hospital singapore which cost our family over a million pesos from her operation and infusion treatment we have another huge medical bill lining up for 1 year it can be daunting particularly if you don t have any insurance to cover you hence her friends and i came up with the idea of fund raising if you know ann and would want to help you can donate on this page or simply buy shirts for a cause see pic and price below rest assured the money will go for her medication until she fully recovers currently ann is on her 17th week as of today 19 10 10 doing the medication she lives a normal life and still works full time despite of the side effects of her treatment she is standing strong and continues to hold on to god i know that he who is all knowing and all powerful has appointed ann for something great and we just have to trust him completely i hope you are blessed with this story if you choose not to make a donation today please remember prayers are gifts as well may god bless you all please view the on the link below tshirt prices and colors ann s fundraising tshirtif you want to call or contact ann please email her at ann_esg yahoo com or pm her on her facebook and twitter account twitter com esguerraannthank you in advance know more about melanoma see links below http melanomaknowmore com http www cancer gov cancertopics types melanoma"
    print(get_entities(text))



