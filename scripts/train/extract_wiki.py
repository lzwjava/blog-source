from mediawiki_dump.tokenizer import WikiTokenizer
with open('enwiki-latest-pages-articles.xml.bz2', 'rb') as dump:
    tokenizer = WikiTokenizer(dump)
    for token in tokenizer:
        if token.type == 'text':
            print(token.value)