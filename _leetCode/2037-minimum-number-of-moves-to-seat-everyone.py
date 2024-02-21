#Minimum Number Of Moves To Seat Everyone
#https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

caseSeats_1 = [3,1,5]
caseStudents_1 = [2,7,4]

caseSeats_2 = [4,1,5,9]
caseStudents_2 = [1,3,2,6]

caseSeats_3 = [2,2,6,6]
caseStudents_3 = [1,3,2,6]

if False:
    def minMovesToSeat(seats, students):
        seats.sort()
        students.sort()

        total = 0
        for i in range(len(seats)):
            total += abs(seats[i] - students[i])
        
        return total

if True:
    def minMovesToSeat(seats, students):
        #two arrays of 0s will be created
        #max(seats) gets the highest value from seats
        seats_cnt = [0] * (max(seats) + 1)
        students_cnt = [0] * (max(students) + 1)


        #set to 1
        #rest are 0
        for seat in seats:
            seats_cnt[seat] += 1
        for student in students:
            students_cnt[student] += 1

        ans = 0
        student = 1
        seat = 1
        while student < len(students_cnt):
            #check if set to 1
            if students_cnt[student]:
                # find the next available seat
                while seat < len(seats_cnt) and not seats_cnt[seat]:
                    seat += 1

                ans += abs(student - seat)
                #set to 0
                seats_cnt[seat] -= 1
                students_cnt[student] -= 1

            #students += 1, to find next 1 in students_cnt
            else:
                student += 1

        return ans

print(f"{minMovesToSeat(caseSeats_1, caseStudents_1)}")
print(f"{minMovesToSeat(caseSeats_2, caseStudents_2)}")
print(f"{minMovesToSeat(caseSeats_3, caseStudents_3)}")