
class History:
    def __init__(self):
        self.pastQueries = set()

    def get_past_queries(self):
        return self.pastQueries

    def add_to_past_queries(self, url):
        self.pastQueries.add(url)
        return url + ' added to past queries.'

    def check_past_queries(self, url):
        return url in self.pastQueries