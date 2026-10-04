class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort() 

        #basically saying that if heaviest matches with someone then move l+=1 to try next
        #if not, heaviest goes alone and move the right pointer down and increase the boat count
        #keep repeating until everyones checked up on 
        num_boats=0 

        l=0 

        r= len(people)-1 

        while l<=r:

            if people[l]+ people[r]<=limit:
                l+=1
            r-=1
            num_boats+=1 
        return num_boats 