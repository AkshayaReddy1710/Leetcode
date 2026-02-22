class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count={0:1}
        ans=0
        for num in nums:
            if num%2==1:
                prefix_sum+=1
            if prefix_sum -k in count:
                ans+=count[prefix_sum-k]
            if prefix_sum in count:
                count[prefix_sum]+=1
            else:
                count[prefix_sum]=1
        return ans
        