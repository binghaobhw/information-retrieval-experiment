# -*- coding: utf-8 -*-
import argparse
from web_crawler import crawl_web

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('seed_url')
    args = arg_parser.parse_args()
    crawl_web(args.seed_url, 2)
