import spacy
import pl_core_news_sm
import warnings
import re
from spacy.tokenizer import Tokenizer
from spacy import displacy
warnings.filterwarnings("ignore")
nlp = pl_core_news_sm.load()

doc = nlp("To jest zdanie.")
print([(w.text, w.pos_) for w in doc])
print("działam na nowo")
introduction_text = ('To powinno być jako'' Procesowane i wgl na osobne słowa, fajnie.')
introduction_doc = nlp(introduction_text)
# Extract tokens for the given doc
print ([token.text for token in introduction_doc])
 
#How to Read a Text File
file_name = 'C:\Doc.txt'
introduction_file_text = open(file_name).read()
introduction_file_doc = nlp(introduction_file_text)
# Extract tokens for the given doc
#print ([token.text for token in introduction_file_doc])

#Sentence detection
sentences = list(introduction_file_doc.sents)
len(sentences)
for sentence in sentences:
  print (sentence)

#WYKRYWANIE ZDAŃ Z NIESTANDARDOWYMI OGRANICZNIKAMI.
def set_custom_boundaries(doc):
# Adds support to use `...` as the delimiter for sentence detection
 for token in doc[:-1] :
  if token.text == '...':
   doc[token.i+1].is_sent_start = True
  return doc

ellipsis_text = ('Pan Tadeusz nie bardzo pasuje do tego... Mimo Wszystko go pozostawie i skorzystam z tego.')

#Załadowanie nowej instancji modelu
custom_nlp = pl_core_news_sm.load()
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
  print(sentence)

#Wykrywanie zdań bez dostosowywania
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
  print(sentence)

#TOKENIZACJA TEKSTU
for token in introduction_file_doc:
  print (token, token.idx)
#DOSTĘP DO ATRYBUTÓW W TOKENIE
for token in introduction_file_doc:
 print (token, token.idx, token.text_with_ws,
  token.is_alpha, token.is_punct, token.is_space,
  token.shape_, token.is_stop)

#DOSTOSOWANIE TOKENU
custom_nlp = pl_core_news_sm.load()
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')
def customize_tokenizer(nlp):
  # Adds support to use `-` as the delimiter for tokenization
  return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
     suffix_search=suffix_re.search,
     infix_finditer=infix_re.finditer,
     token_match=None
     )
custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_text_doc = custom_nlp(ellipsis_text)
print([token.text for token in custom_tokenizer_text_doc])
#STOP WORDS
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
  print(stop_word)
#POMINIĘCIE STOP WORDS W TEKŚCIE WEJŚCIOWYM
for token in introduction_file_doc:
  if not token.is_stop:
   print (token)
#LEMATYZACJA
for token in introduction_file_doc:
   print (token, token.lemma_)
#CZĘSTOTLIWOŚĆ SŁÓW
#Usunięcie słów pomijanych i symboli interpunkcyjnych
words = [token.text for token in introduction_file_doc
     if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
#5 powszechnie występujących słów wraz z ich częstotliwościami
common_words = word_freq.most_common(5)
print (common_words)
# Wyrazy unikatowe
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)
#ROZPOZNANIE CZĘŚCI MOWY
for token in introduction_file_doc:
  print (token, token.tag_, token.pos_, spacy.explain(token.tag_))
#WYZNACZENIE SŁÓW PO DANEJ KATEGORII
nouns = []
adjectives = []
for token in introduction_file_doc:
  if token.pos_ == 'NOUN':
       nouns.append(token)
  if token.pos_ == 'ADJ':
       adjectives.append(token)

nouns
adjectives
#Visualization: Using displaCy
#displacy.serve(introduction_file_doc, style='dep')

#Preprocessing Functions
def is_token_allowed(token):
  if (not token or not token.string.strip() or
     token.is_stop or token.is_punct):
     return False
  return True
def preprocess_token(token):

   return token.lemma_.strip().lower()

complete_filtered_tokens = [preprocess_token(token)
  for token in introduction_file_doc if is_token_allowed(token)]
complete_filtered_tokens
#DOPASOWANIE OPARTE NA REGUŁACH IMIĘ I NAZWISKO
matcher = Matcher(nlp.vocab)
def extract_full_name(nlp_doc):
 pattern = [{'POS':'PROPN'}, {'POS': 'PROPN'}]
 matcher.add('FULL_NAME ', None, pattern)
 matches = matcher(nlp_doc)
 for match_id, start, end in matches:
  span = nlp_doc[start:end]
  return span.text
extract_full_name(introduction_doc)
new_text_extract="Marek Hennig"
new_text_extract_doc=nlp(new_text_extract)
matcher = Matcher(nlp.vocab)
print(extract_full_name(new_text_extract_doc))
#DOPASOWANIE OPARTE NA REGUŁACH NUMER TELEFONU
matcher = Matcher(nlp.vocab)
conference_org_text = ('790234854')
def extract_phone_number(nlp_doc):
 pattern = [{'ORTH': '('}, {'SHAPE': 'ddd'},
            {'ORTH': ')'}, {'SHAPE': 'ddd'},
            {'ORTH': '-', 'OP': '?'},
            {'SHAPE': 'ddd'}]
 matcher.add('PHONE_NUMBER', None, pattern)
 matches = matcher(nlp_doc)
 for match_id, start, end in matches:
  span = nlp_doc[start:end]
  return span.text

conference_org_doc = nlp(conference_org_text)
extract_phone_number(conference_org_doc)
# ANALIZA ZALEŻNOŚCI PRZY UŻYCIU SPACY
piano_text = 'Gus uczy sie gry na pianinku'
piano_doc = nlp(piano_text)
for token in piano_doc:
 print (token.text, token.tag_, token.head.text, token.dep_)
#PORUSZANIE SIĘ PO DRZEWIE I PODDRZEWIE
one_line_about_doc = ('Gus Proto jest programistą w Python'
                       ' obecnie nie pracuje niegdzie, bo mamy coronawirusa i zimę przynajmniej dwudziestolecia.')
one_line_about_doc = nlp(one_line_about_doc)
# Extract children of `Python`
print([token.text for token in one_line_about_doc[5].children])

# Extract previous neighboring node of `Python`
print (one_line_about_doc[5].nbor(-1))

# Extract next neighboring node of `Python`
print (one_line_about_doc[5].nbor())

# Extract all tokens on the left of `Python`
print([token.text for token in one_line_about_doc[5].lefts])

# Extract tokens on the right of `Python`
print([token.text for token in one_line_about_doc[5].rights])

# Print subtree of `Python`
print (list(one_line_about_doc[5].subtree))
