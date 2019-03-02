"""
    You run an e-commerce website and want to record the last N order ids in a log.
    Implement a data structure to accomplish this, with the following API:
     - record(order_id): adds the order_id to the log
     - get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
"""

class Log:
    def __init__(self):
        self.records = []
        self.N = 0

    def record(self, order_id):
        self.N += 1
        self.records.append(order_id)

    def get_last(self, i):
        return self.records[self.N - i]
