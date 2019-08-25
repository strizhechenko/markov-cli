# coding=utf-8

from argparse import ArgumentParser
import re

from pymarkovchain import MarkovChain


class MarkovCli(MarkovChain):
    """ My wrapper for MarkovChain """

    def __init__(self, text):
        super().__init__()
        self.generateDatabase(text)

    @staticmethod
    def from_multiple_files(filepath_list, encoding='utf-8', strip=False):
        """
        :param filepath_list: list of text-files with sentences
        :param encoding: some books may be in cp1251
        :param strip: skip - in dialogs
        """
        text = ""
        for filepath in filepath_list:
            text += open(filepath, encoding=encoding).read()
        if strip:
            text = re.sub(r"[\n^][-–] ", "", text, flags=re.MULTILINE)
        return MarkovCli(text)

    @staticmethod
    def __parse_args():
        parser = ArgumentParser()
        parser.add_argument('--files', nargs='+', required=True)
        parser.add_argument('--seed', type=str)
        parser.add_argument('--count', type=int, default=1)
        parser.add_argument('--encoding', default='utf-8')
        parser.add_argument('--strip', action='store_true')
        return parser.parse_args()

    @staticmethod
    def main():
        """ Main use-case """
        args = MarkovCli.__parse_args()
        chain = MarkovCli.from_multiple_files(args.files, args.encoding, args.strip)
        output = set()
        count = 0
        for _ in range(args.count * 2):
            line = chain.generateStringWithSeed(args.seed) if args.seed else chain.generateString()
            if len(line.split()) < 3:
                continue
            if line not in output:
                print(line)
                print()
                output.add(line)
                count += 1
            if count >= args.count:
                break


if __name__ == '__main__':
    MarkovCli.main()
