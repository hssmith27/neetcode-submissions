class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.network = defaultdict(dict)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].insert(0, [-self.time, tweetId])
        while len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        feed = []
        posters = list(self.network[userId])
        posters.append(userId)

        for poster in posters:
            for tweet in self.tweets[poster]:
                heapq.heappush(feed, tweet)

        i = 0
        while i < 10 and feed:
            tweet = heapq.heappop(feed)
            res.append(tweet[1])
            i += 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId][followeeId] = 1
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].pop(followeeId, False)
        
