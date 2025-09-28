#two sums problem using hash maps python 
def two_sums(nums: list[int] ,target:int) -> list[int]:
    seen = {}
    for curind,currnum in enumerate(nums):
        complement =target - currnum 
        if complement in seen:
            complementind = seen[complement]
            return [complementind,curind]
        seen[currnum]=curind
        
nums = [2,5,6,7,11,15]
target=9
print(f"two sum{nums} : {two_sums(nums,target)}")