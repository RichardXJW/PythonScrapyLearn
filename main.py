# Author:Richard


from scrapy import cmdline


def main():
    cmdline.execute(['scarpy', 'crawl', 'quotes'])
    pass


if __name__ == "__main__":
    main()