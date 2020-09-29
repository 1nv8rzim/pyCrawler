from argparse import ArgumentParser
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0', 'Accept': 'image/webp,*/*',
           'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}


class crawler:
    """
    Main class for pycrawler
    """

    def __init__(self):
        """
        Initializes crawler class
        """
        self.parser = self.arguments()
        self.domain = ''
        self.debug = bool(self.parser.debug)
        self.used = set()
        self.start_crawler()
        for url in sorted(list(self.used)):
            print('[+] ' + url)

    def debug(self, *args):
        if self.debug:
            print(*args)

    def arguments(self):
        """
        Parses command line arguments

        Returns:
            argparse.Namespace : returns parsed command line arguments
        """
        parser = ArgumentParser()
        parser.add_argument('domain', type=str,
                            help='target domain for webcrawler')
        parser.add_argument('-v', '--verbose')
        return parser.parse_args()

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
        return bool(parsed.scheme) and bool(parsed.netloc)

    def start_crawler(self):
        """
        Starts recursive crawler call to map a domain

        Raises:
            TypeError: raises error if domain is not valid
        """
        if(self.is_valid_url(self.parser.domain)):
            self.domain = self.parser.domain
            self.debug('[X] Domain -> ' + self.domain)
            for url in self.find_urls(self.domain):
                self.crawler(url)
        else:
            raise TypeError(
                f'given domain is not valid "{self.parser.domain}"')

    def crawler(self, url):
        """
        Recursive call for crawler that iterates through all url present with a domain

        Args:
            url ([str]): given url of the page that will be used to find all urls on the page and runs the same command
        """
        self.debug('[X] crawling ', url)
        self.used.add(url)
        if urlparse(self.domain).netloc not in url:
            pass
        elif url[-4:].lower() in ('.jpg', 'jpeg', '.png', '.gif', '.pdf', 'tiff', '.raw'):
            pass
        elif url[-5].lower() == '.html':
            for found_url in self.find_urls(url):
                if (found_url in self.used):
                    continue
                self.crawler(found_url)
        elif url[-3].lower() == '.js':
            pass
            # TODO add js parsing for URLs

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
        soup = BeautifulSoup(requests.get(
            url=url, headers=HEADERS).content, 'html.parser')
        for tags in [('a', 'href'), ('script', 'src'), ('img', 'src')]:
            for a_tag in soup.findAll(tags[0]):
                tag = a_tag.attrs.get(tags[1])
                if tag is None or tag == '':
                    continue
                tag = urljoin(url, tag)
                parsed_tag = urlparse(tag)
                tag = parsed_tag.scheme + '://' + parsed_tag.netloc + parsed_tag.path
                if not self.is_valid_url(tag):
                    continue
                urls.add(tag)
        return urls


if __name__ == '__main__':
    crawl = crawler()
