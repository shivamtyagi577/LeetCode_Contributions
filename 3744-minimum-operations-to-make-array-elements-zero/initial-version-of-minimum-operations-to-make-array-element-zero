def min_operations_to_zero(l: int, r: int) -> int:
            """
            For a given range [l,r], calculate the minimum number of operationss
            required to reduce all elements to zero using operation:
            Select two integers a and b, replace them with floor(a/4) and floor(b/4).
            """
            # Create the initial array
            nums = list(range(l, r+1))
            operations = 0

            # Continue until all elements are zero
            while any(num > 0 for num in nums):
                # Sort in descending order to pick the largest two elements
                nums.sort(reverse=True)

                # Pick the two largest elements
                a = nums.pop(0)
                b = nums.pop(0) if nums else 0 # iff when one element left, b = 0

                # Apply the operation
                nums.append(a//4)
                if b > 0:
                    nums.append(b//4)
                
                operations += 1
            
            return operations

        total = 0
        for l,r in queries:
            total += min_operations_to_zero(l,r)

        return total
