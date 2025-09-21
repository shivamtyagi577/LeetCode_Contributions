class MovieRentingSystem(object):

    def __init__(self, n, entries):
        self.movie_to_unrent = defaultdict(list) # movieID -> min-heap(price,shop)
        self.shop_movie_price = {} # (shop,movie) -> price
        self.rented_set = set()
        self.rented_heap = []  # min-heap of (price, shop, movie)

        for shop,movie,price in entries:
            heapq.heappush(self.movie_to_unrent[movie], (price,shop))
            self.shop_movie_price[(shop,movie)] = price

    def search(self, movie):
        result = []
        temp = []

        while self.movie_to_unrent[movie] and len(result) < 5:
            price, shop = heapq.heappop(self.movie_to_unrent[movie])
            if (shop, movie) not in self.rented_set:
                result.append(shop)
            temp.append((price, shop))

        for item in temp:
            heapq.heappush(self.movie_to_unrent[movie], item)

        return result


    def rent(self, shop, movie):
        price = self.shop_movie_price[(shop,movie)]
        self.rented_set.add((shop,movie))
        heapq.heappush(self.rented_heap,(price,shop,movie))   

    def drop(self, shop, movie):
        self.rented_set.remove((shop,movie))    

    def report(self):
        result = []
        seen = set()
        temp = []

        while self.rented_heap and len(result) < 5:
            price, shop, movie = heapq.heappop(self.rented_heap)
            if (shop, movie) in self.rented_set and (shop, movie) not in seen:
                result.append([shop, movie])
                seen.add((shop, movie))
            temp.append((price, shop, movie))

        # Reinsert only valid entries
        for item in temp:
            if (item[1], item[2]) in self.rented_set:
                heapq.heappush(self.rented_heap, item)

        return result





# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()