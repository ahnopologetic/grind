class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        self.req.append(t)
        return len([r for r in self.req if t - 3000 <= r and r <= t])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
