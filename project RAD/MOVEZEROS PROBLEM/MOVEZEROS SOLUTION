#python for two pointers and moving a particular index element without making a copy of it 

def movezero(nums :list[int]) -> None:
    
    wriptr =0;
    for reaptr in range(len(nums)):
        if nums[reaptr] !=0:
            if reaptr != wriptr:
                nums[wriptr] = nums[reaptr]
                
                nums[reaptr] =0
            wriptr+=1
            
            
nums = [0,1,2,0,2,1]
print(f"orignal array: {nums}")
movezero(nums)
print(f"clean sweep array {nums}")
