import argparse
import logging

class Arguments():
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialize_parser()

    def initialize_parser(self):
        self.parser.add_argument('--mode', type=str, default='csv', help='model: "QA" or "csv" | Mode "QA": get input and return output score in terminal | Mode "csv": input and output in csv format')
        self.parser.add_argument('--input_path', type=str, default=None, help='path of input csv file if mode csv')
        self.parser.add_argument('--save_to', type=str, default='results.csv', help='path of output csv file if mode csv')
        self.parser.add_argument('--model_name', type=str, default='original', help='model name: "original" or "unbiased"')
    
    def parse(self):
        opt = self.parser.parse_args()
        return opt