from corenlp import batch_parse
corenlp_dir = "../tools/corenlp-python/corenlp/stanford-corenlp-full-2014-01-04"
raw_text_directory = "../dataset/books_txt/small_sample"
parsed = batch_parse(raw_text_directory, corenlp_dir,raw_output=True)
for books in parsed:
    print books['sentences']
