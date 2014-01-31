import json
import jsonrpclib
from pprint import pprint


class StanfordNLP:
    def __init__(self, port_number=8080):
        self.server = jsonrpclib.Server("http://10.2.4.81:%d" % port_number)

    def parse(self, text):
        return json.loads(self.server.parse(text))

#nlp = StanfordNLP()
#result = nlp.parse("Henry gave the book to Carol and she liked it.")
#pprint(result)

#from nltk.tree import Tree
#tree = Tree.parse(result['sentences'][0]['parsetree'])
#pprint(tree)
