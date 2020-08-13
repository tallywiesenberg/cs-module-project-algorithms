'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    maxs = []
    i = 0
    while i <= len(nums)-k:
        for j in range(k-1):
            if nums[i+j+1] > nums[i+j]:
                max_ = nums[i+j+1]
            else:
                pass
        maxs.append(max_)
        i += 1

    return maxs


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
