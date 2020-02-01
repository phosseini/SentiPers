import xml.etree.ElementTree as ET
import os
import pandas as pd


class SentiPers:
    def __init__(self):
        self.main_path = "data/main/"
        self.extra_path = "data/extra/"
        self.sentences_columns = ["sid", "text", "polarity", "file"]

    def read_sentences(self, polarity=[]):
        """
        read all sentences from the corpus
        :param polarity: filter for polarity. e.g. ["-1", "+1"]. possible value: ["-2", "-1", "0", "+1", "+2"]
        :return:
        """
        df = pd.DataFrame(columns=self.sentences_columns)

        def add_sentences(obj):
            tmp_df = pd.DataFrame(columns=self.sentences_columns)
            for sentence in obj:
                if len(polarity) == 0 or sentence.attrib["Value"] in polarity:
                    tmp_df = tmp_df.append([{'sid': sentence.attrib["ID"], 'text': sentence.text,
                                             'polarity': sentence.attrib["Value"],
                                             'file': full_path}], ignore_index=True)
            return tmp_df

        for path in os.listdir(self.main_path):
            elements_list = ["General_Reviews", "Critical_Reviews"]
            full_path = os.path.join(self.main_path, path)
            if os.path.isfile(full_path) and full_path.endswith(".xml"):
                try:
                    tree = ET.parse(full_path)
                    root = tree.getroot()
                    for child in root:
                        if child.tag in elements_list:
                            for review in child:
                                df = df.append(add_sentences(review))

                        elif child.tag == "Review":
                            df = df.append(add_sentences(child))
                except Exception as e:
                    print("[log] details: " + str(e), full_path)
        return df
