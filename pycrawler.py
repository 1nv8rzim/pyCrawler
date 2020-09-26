from argparse import ArgumentParser
import re

VALID_URL = re.compile(
    '((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')


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
        try:
            self.domain = VALID_URL.match(
                self.parser.domain[0]).string
            print('[+] Domain -> ' + self.domain)
        except:
            raise TypeError(
                f'given domain is not valid "{self.parser.domain[0]}"')

    def crawler(self, url):
        if (type(url) is not str):
            pass
        else:
            self.used.add(url)
            for found_url in find_urls(url):
                if (found_url in self.used):
                    continue

    def find_urls(self, url):
        pass


crawler()
