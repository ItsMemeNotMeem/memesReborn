from urllib.request import urlopen

import pytesseract
from PIL import Image
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def read_local_image_text(local_image_path: str):
    return pytesseract.image_to_string(Image.open(local_image_path))


def read_url_image_text(url: str):
    image = Image.open(urlopen(url))
    return pytesseract.image_to_string(image)


def clean_text(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    english_stop_words = stopwords.words('english')
    filtered_words = [w for w in tokens if w not in english_stop_words]
    return " ".join(filtered_words)
