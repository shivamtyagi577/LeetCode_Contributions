class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # function : Add
        def add_op(x):
            arr = list(x)
            for i in range(1,len(arr),2): # odd indices
                arr[i] = str((int(arr[i]) + a ) % 10)
            return ''.join(arr)

        # function : Rotate
        def rotate_op(x):
            return x[-b:] + x[:-b]

        visited = set([s])
        queue = deque([s])
        smallest = s

        while queue:
            curr = queue.popleft()
            if curr < smallest:
                smallest = curr

            # Apply Add 
            next_add = add_op(curr)
            if next_add not in visited:
                visited.add(next_add)
                queue.append(next_add)

            # Apply rotate
            next_rotate = rotate_op(curr)
            
            if next_rotate not in visited:
                visited.add(next_rotate)
                queue.append(next_rotate)

        return smallest
