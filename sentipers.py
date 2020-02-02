import xml.etree.ElementTree as ET
import os
import pandas as pd


class SentiPers:
    def __init__(self):
        self.main_path = "data/main/"
        self.extra_path = "data/extra/"
        self.sentipers_path = "data/sentipers.xlsx"
        self.sentences_columns = ["sid", "text", "polarity", "file"]

    def sentipers_to_excel(self):
        """
        read all sentences in sentipers into a data frame and save them in a single excel file
        :return:
        """
        df = self.read_all_sentences()
        df.to_excel(self.sentipers_path, header=True, index=False, encoding='utf8')

    def read_all_sentences(self, polarity=[]):
        """
        reading all sentences from main and extra folders
        :param polarity: filter for polarity. e.g. ["-1", "+1"]. possible value: ["-2", "-1", "0", "+1", "+2"]
        :return:
        """
        df = self.read_sentences_main(polarity=polarity)
        df = df.append(self.read_sentences_extra(polarity=polarity))
        return df

    def read_sentences_main(self, polarity=[]):
        """
        read all sentences from the corpus
        :param polarity: filter for polarity. e.g. ["-1", "+1"]. possible value: ["-2", "-1", "0", "+1", "+2"]
        :return:
        """
        df = pd.DataFrame(columns=self.sentences_columns)

        def add_sentences(sents):
            tmp_df = pd.DataFrame(columns=self.sentences_columns)
            for sentence in sents:
                if len(polarity) == 0 or sentence.attrib["Value"] in polarity:
                    tmp_df = tmp_df.append([{'sid': sentence.attrib["ID"], 'text': sentence.text,
                                             'polarity': str(sentence.attrib["Value"]),
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

        # making sure rows have non-empty "text" and "polarity"
        df = df.loc[(df["text"] != "") & (df["polarity"] != "")]

        return df.drop_duplicates(subset=["text"], keep=False).reset_index()

    def read_sentences_extra(self, polarity=[]):
        """
        reading sentences in extra folder format
        :param polarity: filter for polarity. e.g. ["-1", "+1"]. possible value: ["-2", "-1", "0", "+1", "+2"]
        :return:
        """
        df = pd.DataFrame(columns=self.sentences_columns)

        for path in os.listdir(self.extra_path):
            full_path = os.path.join(self.extra_path, path)
            if os.path.isfile(full_path) and full_path.endswith(".xml"):
                with open(full_path) as file:
                    sentence = ""
                    for line in file:
                        # check if line is the label
                        if "\t" not in line and all(char in line for char in ["[", "["]) and "[@@@]" not in line:
                            label = line.replace('[', '').replace(']', '').replace('\n', '')

                        else:
                            # check if it's time to save sentence info
                            if "[@@@]" in line and (len(polarity) == 0 or label in polarity):
                                df = df.append([{'sid': '-', 'text': sentence.strip(),
                                                 'polarity': str(label),
                                                 'file': full_path}], ignore_index=True)
                                sentence = ""
                                label = ""
                            else:
                                sentence += line.replace("\n", "").split("\t")[1] + " "

        # making sure rows have non-empty "text" and "polarity"
        df = df.loc[(df["text"] != "") & (df["polarity"] != "")]

        return df.drop_duplicates(subset=["text"], keep=False).reset_index()
