import re

from model.search.preprocessing_util import clean_text, read_local_image_text, read_url_image_text


def test_read_image_text():
    image_text = read_local_image_text('test/example1.png')
    cleaned_image_text = re.sub(r'\s+', ' ', image_text)
    expected_text = 'Noisy image to test Tesseract OCR'
    assert expected_text == cleaned_image_text


def test_url_image_text():
    input_url = 'http://ammozon.co.in/headtohead/wp-content/uploads/2016/10/Tesseract-300x161.jpg'
    image_text = read_url_image_text(input_url)
    cleaned_image_text = re.sub(r'\s+', ' ', image_text)
    expected_text = 'Tesseract OCR'
    assert expected_text == cleaned_image_text


def test_clean_text():
    input_text = 'Noisy \n image to test Tesseract. OCR'
    expected_text = 'noisy image test tesseract ocr'
    assert expected_text == clean_text(input_text)


test_read_image_text()
test_clean_text()
test_url_image_text()
