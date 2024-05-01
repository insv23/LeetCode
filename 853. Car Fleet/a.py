# https://leetcode.com/problems/car-fleet/description/

'''
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106
'''
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 将车辆按照出发位置从远到近排序(即离终点近的在开头)
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        
        last_arrival_time = 0
        for pos, spd in cars:
            # 计算当前车辆到达目的地的时间
            time = (target - pos) / spd
            # 如果当前车辆到达时间大于上一个车队的到达时间, 将形成一个新的车队(即当前车没追上出发时比它更靠近终点的车)
            if time > last_arrival_time:
                fleets += 1
                last_arrival_time = time
        
        return fleets

if __name__ == "__main__":
    target = int(input().strip())
    position = eval(input())
    speed = eval(input())

    print(Solution().carFleet(target, position, speed))

'''
为了解决这个问题，我们可以按照车辆的起始位置对车辆进行排序，并计算每辆车到达目的地的时间。然后从最靠近目的地的车开始，向后检查每辆车是否能够赶上前面的车队。如果一辆车到达目的地的时间小于或等于前面车队的时间，那么它们将形成一个车队；否则，它将形成一个新的车队。
'''