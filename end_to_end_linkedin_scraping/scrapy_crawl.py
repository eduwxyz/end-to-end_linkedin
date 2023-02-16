from end_to_end_linkedin.spiders.linkedin_jobs import LinkedJobsSpider
from scrapy.crawler import CrawlerProcess


def main():
    process = CrawlerProcess()
    process.crawl(LinkedJobsSpider)
    process.start()


if __name__ == "__main__":
    main()
