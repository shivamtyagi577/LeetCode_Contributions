class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        #Function tp calculate how much the pass ratio improves by adding one student
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total

        # Use a max heap to always pick the class with highest improvement
        heap = []
        for passed, total in classes:
            heapq.heappush(heap, (-improvement(passed,total), passed, total))
        
        # Assign each extra student
        for _ in range(extraStudents):
            _, passed, total = heapq.heappop(heap)
            passed += 1
            total  += 1
            heapq.heappush(heap, (-improvement(passed,total), passed, total))

        # Calculate the final average pass ratio 
        total_ratio = sum(passed / total for _, passed, total in heap)
        return round(total_ratio / len(classes), 5)