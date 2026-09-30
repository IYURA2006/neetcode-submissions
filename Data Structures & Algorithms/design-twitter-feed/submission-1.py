
import heapq
class Twitter:

    def __init__(self):
        self.time = 0 
        self.followers = {}
        self.posts = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((-self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        history = []
        tweetfeed = []
        if userId in self.followers:
            for followees in self.followers[userId]:
                if followees in self.posts:
                    for post in self.posts[followees]:
                        heapq.heappush(history, post)
            
        if userId in self.posts:
            for post in self.posts[userId]:
                heapq.heappush(history, post)
        
        i = 0
        while i < 10 and len(history) != 0: 
            t, user, tweet = heapq.heappop(history)
            tweetfeed.append(tweet)
            i += 1
        
        return tweetfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
