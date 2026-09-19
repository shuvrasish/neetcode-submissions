class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid

            if arr[l] <= arr[mid]:
            # left half sorted
                if arr[l] <= target <= arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif arr[mid] <= arr[r]:
            # right half sorted
                if arr[mid] <= target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1