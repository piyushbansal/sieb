import nltk.data


MAX_LINES = 30

class Book:

	def __init__(self,name):
		self.book_name = name
		self.path = "../dataset/books_txt/" + self.book_name
		self.text = open(self.path,'rb').read()

	def get_chunk(self):
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		self.sentences = sent_detector.tokenize(self.text.strip(),realign_boundaries=True)
		self.sentences = map(lambda x: ' '.join(x.splitlines()),self.sentences)
		for sentences in self.sentences:
			yield sentences

	def get_book(self):
		for sentences in self.get_chunk():
			print sentences





