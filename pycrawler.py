from argparse import ArgumentParser
import re

VALID_URL = re.compile('_^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)(?:\.(?:[a-z\x{00a1}-\x{ffff}0-9]+-?)*[a-z\x{00a1}-\x{ffff}0-9]+)*(?:\.(?:[a-z\x{00a1}-\x{ffff}]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$_iuS')


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
        self.crawler_info = {}

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
        self.crawler_info['domain'] = self.parser.domain
