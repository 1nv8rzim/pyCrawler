from argparse import ArgumentParser


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
        pass

    def arguments(self):
        """
        Parses command line arguments
        :params: n/a uses command line args
        :return: argparse.Namespace with parsed arguments
        """
        parser = ArgumentParser()
        parser.add_argument(nargs=1, type=str,
                            help='target domain for webcrawler')
        return parser.parse_args()
