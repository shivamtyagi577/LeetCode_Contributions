class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineToHeap = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodToCuisine[food] = cuisine
            self.foodToRating[food] = rating
            heapq.heappush(self.cuisineToHeap[cuisine], (-rating,food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.foodToRating[food] = newRating
        heapq.heappush(self.cuisineToHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineToHeap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.foodToRating[food]:
                return food
            heapq.heappop(heap)


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)