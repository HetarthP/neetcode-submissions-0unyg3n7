class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #circle=0
        #square= 1 

        #num of sandwich= num of students (len(students))


        res= len(students)

        count= Counter(students)

        for s in sandwiches:

            if count[s]>0:
                res-=1
                count[s]-=1
            else:
                break
        return res
