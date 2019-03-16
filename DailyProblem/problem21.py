"""
    Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
    find the minimum number of rooms required.

    For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

class Room:
    def __init__(self, interval=None):
        self.intervals = []
        if interval:
            self.intervals.append(interval)
    def occupied(self, interval):
        start = interval[0]
        end = interval[1]
        for i in self.intervals:
            if (start >= i[0] and start <= i[1]) or (end >= i[0] and end <= i[1]):
                return True
        return False

def minimum_rooms(intervals):
    rooms = []
    if len(intervals) > 0:
        rooms.append(Room())
    for interval in intervals:
        i = 0
        ok = False
        while (not ok and i < len(rooms)):
            if not rooms[i].occupied(interval):
                rooms[i].intervals.append(interval)
                ok = True
            i += 1
        if not ok:
            rooms.append(Room(interval))
    return len(rooms)



print(minimum_rooms([(30, 75), (0, 50), (60, 150)]))
print(minimum_rooms([(30, 75), (0, 530), (60, 150),(30, 75), (10, 50), (233, 150),(30, 735), (10, 530), (3, 54),(30, 75), (0, 530), (60, 150),(30, 75), (10, 50), (233, 150),(30, 735), (10, 530), (3, 54),(30, 75), (0, 530), (60, 150),(30, 75), (10, 50), (233, 150),(30, 735), (10, 530), (3, 54),(30, 75), (0, 530), (60, 150),(30, 75), (10, 50), (233, 150),(30, 735), (10, 530), (3, 54)]))
