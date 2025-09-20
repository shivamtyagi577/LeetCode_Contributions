class Router(object):

    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.packet_set = set() 
        self.queue = deque() # FIFO queue of packets
        self.dest_map = defaultdict(list) # destination -> sorted list of timestamps

    def addPacket(self, source, destination, timestamp):
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False
        
        # If memory limit exceeded, remove oldest packet
        if len(self.queue) >= self.memoryLimit:
            old_packet = self.queue.popleft()
            old_key = tuple(old_packet)
            self.packet_set.remove(old_key)

            # Remove timestamp from the dest_map
            timestamps = self.dest_map[old_packet[1]]
            idx = bisect.bisect_left(timestamps,old_packet[2])

            if idx < len(timestamps) and timestamps[idx] == old_packet[2]:
                timestamps.pop(idx)
        
        # Add new packet
        self.queue.append([source, destination, timestamp])
        self.packet_set.add(key)
        bisect.insort(self.dest_map[destination], timestamp)

        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        
        packet = self.queue.popleft()
        key = tuple(packet)
        self.packet_set.remove(key)

        # Remove timestamp from the dest_map
        timestamps = self.dest_map[packet[1]]
        idx = bisect.bisect_left(timestamps,packet[2])

        if idx < len(timestamps) and timestamps[idx] == packet[2]:
            timestamps.pop(idx)
        
        return packet

    def getCount(self, destination, startTime, endTime):
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)