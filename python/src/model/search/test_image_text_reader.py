import re

from model.search import read_image_text
from model.search.preprocessing_util import clean_text


def test_read_image_text():
    image_text = read_image_text('test/example1.png')
    cleaned_image_text = re.sub(r'\s+', ' ', image_text)
    expected_text = 'Noisy image to test Tesseract OCR'
    assert expected_text == cleaned_image_text


def test_clean_text():
    input_text = 'Noisy \n image to test Tesseract. OCR'
    expected_text = 'noisy image to test tesseract OCR'
    assert expected_text == clean_text(input_text)


test_read_image_text()
test_clean_text()
