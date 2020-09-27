from argparse import ArgumentParser
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class crawler:
    """
    Main class for webcrawler
    """

    def __init__(self):
        """
        Initializes crawler class
        :params: n/a
        :return: n/a
        """
        self.parser = self.arguments()
        self.domain = ''
        self.used = set()
        self.start_crawler()

    def arguments(self):
        """
        Parses command line arguments
        :params: n/a uses command line args
        :return: argparse.Namespace with parsed arguments
        """
        parser = ArgumentParser()
        parser.add_argument('domain', nargs=1, type=str,
                            help='target domain for webcrawler')
        return parser.parse_args()

    def start_crawler(self):
        if(is_valid_url(self.domain[0])):
            self.domain = self.parser.domain[0]
            print('[+] Domain -> ' + self.domain)
        else:
            raise TypeError(
                f'given domain is not valid "{self.parser.domain[0]}"')

    def crawler(self, url):
        if (self.domain not in url):
            pass
        else:
            self.used.add(url)
            for found_url in find_urls(url):
                if (found_url in self.used):
                    continue
                self.crawler

    @staticmethod
    def is_valid_url(url):
        parsed = urlparse(url)
        return parsed.scheme and parsed.netloc

    def find_urls(self, url):
        pass


crawler()
