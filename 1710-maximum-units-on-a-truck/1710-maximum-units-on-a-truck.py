class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        max_units = 0
        for box in boxTypes:
            if truckSize < 0:
                break
            max_units += min(truckSize, box[0]) * box[1]
            truckSize -= box[0]
        return max_units
        