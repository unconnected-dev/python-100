#Minimum Number Of Moves To Seat Everyone
#https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

caseSeats_1 = [3,1,5]
caseStudents_1 = [2,7,4]

caseSeats_2 = [4,1,5,9]
caseStudents_2 = [1,3,2,6]

caseSeats_3 = [2,2,6,6]
caseStudents_3 = [1,3,2,6]

if True:
    def minMovesToSeat(seats, students):
        seats.sort()
        students.sort()

        total = 0
        for i in range(len(seats)):
            total += abs(seats[i] - students[i])
        
        return total

print(f"{minMovesToSeat(caseSeats_1, caseStudents_1)}")
print(f"{minMovesToSeat(caseSeats_2, caseStudents_2)}")
print(f"{minMovesToSeat(caseSeats_3, caseStudents_3)}")