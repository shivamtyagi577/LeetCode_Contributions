class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        empty = numBottles
        drunk = numBottles

        while(empty >= numExchange):
            empty -= numExchange
            empty += 1
            drunk += 1
            numExchange += 1

        return drunk

        