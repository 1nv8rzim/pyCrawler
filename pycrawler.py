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
        self.crawler_site = {}
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
            self.crawler_info['domain'] = VALID_URL.match(
                self.parser.domain[0]).string
            print('[+] Domain -> ' + self.crawler_info['domain'])
        except:
            raise TypeError(
                f'given domain is not valid "{self.parser.domain[0]}"')

        self.crawler_info['used'] = set()

    def crawler(self, url):
        if (type(url) is not str):
            pass
        else:
            self.crawler_info['used'].add(url)


crawler()
