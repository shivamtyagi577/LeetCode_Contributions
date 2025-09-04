class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Calculate the distance between individuals
        distance_xz = abs(x-z)
        distance_yz = abs(y-z)

        if distance_xz < distance_yz:
            return 1
        elif distance_xz > distance_yz:
            return 2
        else:
            return 0