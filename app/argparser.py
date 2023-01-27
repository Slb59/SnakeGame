import app
import argparse
from logs import LOGGER
from .parameters import Parameters


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser('snake game')

        self.parser.add_argument('--version', '-v',
                                 action='store_true',
                                 help='show current version')

        self.parser.add_argument('--ia',
                                 type=str,
                                 help='activate ia mode')

        self.args = self.parser.parse_args()

        LOGGER.debug(self.args)

        if self.args.version:
            print('snake game ' + app.__version__)

    def read_parameters(self):

        p = Parameters()

        if self.args.ia is not None:
            p.ia_mode = self.args.ia_mode

        return p