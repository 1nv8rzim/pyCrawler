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
        """
        self.parser = self.arguments()
        self.domain = ''
        self.used = set()
        self.start_crawler()

    def arguments(self):
        """
        Parses command line arguments

        Returns:
            argparse.Namespace : returns parsed command line arguments
        """
        parser = ArgumentParser()
        parser.add_argument('domain', nargs=1, type=str,
                            help='target domain for webcrawler')
        return parser.parse_args()

    def start_crawler(self):
        """
        Starts recursive crawler call to map a domain

        Raises:
            TypeError: raises error if domain is not valid
        """
        if(is_valid_url(self.domain[0])):
            self.domain = self.parser.domain[0]
            print('[+] Domain -> ' + self.domain)
        else:
            raise TypeError(
                f'given domain is not valid "{self.parser.domain[0]}"')

    def crawler(self, url):
        """
        Recursive call for crawler that iterates through all url present with a domain

        Args:
            url ([str]): given url of the page that will be used to find all urls on the page and runs the same command
        """
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
        """
        Checks if a url is valid 

        Args:
            url (str): url whose validity is in question

        Returns:
            bool: whether the url is valid
        """
        parsed = urlparse(url)
        return parsed.scheme and parsed.netloc

    def find_urls(self, url):
        """
        Finds all url in a given url

        Args:
            url (str): url of webpage being search through

        Returns:
            set : set of unique urls to given page
        """
        urls = set()
        domain_name = urlparse(url).netloc
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        for a_tag in soup.findAll('a'):
            href = a_tag.attrs.get('href')
            if href is None or href == '':
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + '://' + parsed_href.netloc + parsed_href.path
            if is_valid_url(href):
                continue
            if href in self.used:
                continue
            if self.domain not in href:
                continue
            urls.add(href)
        return urls


if __name__ == '__main__':
    crawler()
