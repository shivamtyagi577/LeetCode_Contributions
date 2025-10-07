class Solution(object):
    def avoidFlood(self, rains):
        n = len(rains)
        dict_lake_next_rain = defaultdict(list)

        for i, lake in enumerate(rains):
            if lake > 0:
                dict_lake_next_rain[lake].append(i)

        set_full_lakes = set()
        list_dry_days = []
        ans = [-1] * n
        dict_next_rain_day = {}

        for i in range(n):
            if rains[i] > 0:
                lake = rains[i]
                if lake in set_full_lakes:
                    return []
                set_full_lakes.add(lake)
                dict_lake_next_rain[lake].pop(0)
                if dict_lake_next_rain[lake]:
                    heapq.heappush(list_dry_days, (dict_lake_next_rain[lake][0], lake))
            
            else:
                if list_dry_days:
                    day, lake_to_dry = heapq.heappop(list_dry_days)
                    set_full_lakes.remove(lake_to_dry)
                    ans[i] = lake_to_dry
                else:
                    ans[i] = 1
        return ans
