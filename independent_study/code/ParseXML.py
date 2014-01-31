import xml.etree.ElementTree as ET
from collections import Counter

class ParseXML(object):

    def __init__(self, xml_filename):
        self.file = xml_filename
        self.tree = None
        self.root = None
        self.ner = {}

    def getroot(self):
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()

    def getNER(self):
        for sentences in self.root.iter('sentence'):
            sentence_tagged = {}
            sentence_roles = {}
            for token in sentences.iter('token'):
                word = token.find('word').text
                NER = token.find('NER').text
                token_id = int(token.attrib['id'])

                sentence_tagged[token_id-1] = [word,NER]

            entity = ''
            for i in range(len(sentence_tagged)-2):
                if not entity:
                    entity = sentence_tagged[i][0]
                if(sentence_tagged[i][1] == sentence_tagged[i+1][1]):
                    entity += ' '
                    entity += sentence_tagged[i+1][0]
                else:
                    if entity:
                        sentence_roles[entity] = sentence_tagged[i][1]
                        entity = '' 
                    else:
                        entity = sentence_tagged[i][0]
            sentence_roles[entity] = sentence_tagged[len(sentence_tagged)-1][1]

            for role in sentence_roles:
                if sentence_roles[role] != 'O':
                    try:
                        self.ner[role].append(sentence_roles[role])
                    except KeyError:
                        self.ner[role] = [sentence_roles[role]]
            print sentence_roles
            print

        for role in self.ner:
            c = Counter(self.ner[role])
            self.ner[role] = c.most_common(1)[0][0]

        return self.ner




            



