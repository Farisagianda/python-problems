"""
7. Rolling Average of Request Latency
Problem:
Implement a function to maintain a rolling average of request latency over the last N requests.

Example Usage:


tracker = RollingAverage(5)
tracker.add(100)
tracker.add(200)
tracker.add(300)
tracker.add(400)
tracker.add(500)
print(tracker.get_average())  # 300.0
tracker.add(600)
print(tracker.get_average())  # 400.0  (because only last 5 values are considered)

"""
class RollingAverage():
    def __init__(self, n):
        self.l = []
        self.n = n
    def add(self, t):
        self.l.append(t)
    def get_average(self):
        self.l = self.l[-self.n:]
        avg = sum(self.l) / len(self.l)
        return avg

tracker = RollingAverage(5)
tracker.add(100)
tracker.add(200)
tracker.add(300)
tracker.add(400)
tracker.add(500)
print(tracker.get_average())
tracker.add(600)
print(tracker.get_average())


