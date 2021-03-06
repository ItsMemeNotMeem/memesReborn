import argparse
import os
from pathlib import Path

import nltk

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))


def _get_token_file():
    return os.path.join(CONFIG_DIR, '.token')


def generate_parser():
    argument_parser = argparse.ArgumentParser(
        description='Saves your facebook developer token to an appropriate directory'
    )
    argument_parser.add_argument('--token')
    return argument_parser.parse_args()


def write_token():
    token_file_path = _get_token_file()
    with open(token_file_path, 'w+') as token_file_writer:
        token_file_writer.write(cli_parser.token)
    print('Created .token file')


def load_token() -> str:
    return Path(_get_token_file()).read_text()


def download_nltk():
    nltk.download('all')


if __name__ == '__main__':
    cli_parser = generate_parser()
    download_nltk()
    if hasattr(cli_parser, 'token'):
        write_token()
