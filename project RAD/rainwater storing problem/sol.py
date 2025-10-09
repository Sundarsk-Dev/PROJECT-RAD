from typing import List
def trap(height:List[int])->int:
    if not height or len(height)<3:
        return 0
    left,right=0,len(height)-1
    leftmax=0
    rightmax=0
    totalwater=0
    while left<right:
        if height[left]<height[right]:
            if height[left]>=leftmax:
                leftmax=height[left]
            else:
                totalwater+=leftmax-height[left]
            left+=1
        else:
            if height[right]>= rightmax:
                rightmax=height[right]
            else:
                totalwater +=rightmax-height[right]
            right-=1
    return totalwater

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 1], 1),
        ([2, 0, 2], 2),
        ([5, 5, 5, 5], 0), # No water trapped
        ([4, 2, 3], 1), # 3 > 2, so 1 unit of water is trapped
    ]

    print("--- Trapping Rain Water Test Results ---")
    
    for heights, expected in test_cases:
        result = trap(heights)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Heights: {heights} -> Trapped Water: {result}, Status: {status}\n")