class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            for j in range(n):
                # Skip comparing a point itself
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                print(x1,y1,x2,y2)

                # Check if point i on the upper left side of point j
                if x1 <= x2 and y1 >= y2:
                    valid = True

                    for k in range(n):
                        if k != i and k!= j:
                            x, y  = points[k]

                            # Check if point k lies inside or on the border of the rectangle
                            if x1 <= x <= x2 and y2 <= y <= y1:
                                valid = False
                                break
                    
                    if valid:
                        count += 1
        return count