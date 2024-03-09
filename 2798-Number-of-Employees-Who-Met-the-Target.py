class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        employes=0
        for i in range (len(hours)):
            if hours[i]>=target:
                employes+=1
        return employes