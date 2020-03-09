# Reference https://d-science.com/articles/finding-broken-links-with-python/
# Crawler internal and external links from help.sling.com
# Visiting only first found 25 links
# Writing results to Json

import unittest
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Challenge11(unittest.TestCase):

    def setUp(self):
        self.site = 'https://help.sling.com'
        self.base = urlparse(self.site).netloc

    def test_challenge11_crawler(self):
        to_visit = [self.site]
        to_visit_count = 25
        out_links = []
        visited = {}
        external_visited = {}

        while to_visit and to_visit_count:
            to_visit_link = to_visit.pop()
            to_visit_count -= 1
            print("Working on link: %s "% to_visit_link)
            url = urljoin(self.site, to_visit_link)

            try:
                r = requests.get(url)
                visited[to_visit_link] = r.status_code

            except:
                visited[to_visit_link] = None

            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html5lib')
                links = [l['href'] for l in soup.find_all('a', href=True)]
                for link in links:
                    parsed_link = urlparse(link)
                    loc = parsed_link.netloc
                    joined_url = urljoin(self.site, link)

                    if loc == '':
                        if joined_url not in to_visit and joined_url not in visited.keys():
                            to_visit.append(joined_url)

                    elif loc == self.base:
                        if link not in to_visit and link not in visited.keys():
                            to_visit.append(link)

                    else:
                        if link not in out_links and link not in visited.keys():
                            out_links.append(link)

        # check the status of external links
        while out_links:
            to_visit_out_link = out_links.pop()

            try:
                r = requests.get(to_visit_out_link)
                external_visited[to_visit_out_link] = r.status_code

            except:
                external_visited[to_visit_out_link] = None

        # Print Status
        result_data = {"internal": visited}
        for link, status in visited.items():
            print("Status %s : %s" % (status, link))

        if out_links:
            result_data["external"] = out_links
            print("External links visited")
            for link, status in external_visited.items():
                print("Status %s : %s" % (status, link))

        # Write results to json
        with open("Crawler_Result_Data.json", "w") as dataFile:
            json.dump(result_data, dataFile, indent=4, separators=(',', ': '), sort_keys=True)


if __name__ == '__main__':
    unittest.main()