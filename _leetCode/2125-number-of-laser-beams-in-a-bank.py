#Number Of Laser Beams In A Bank
#https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

caseBank_1 = ["011001","000000","010100","001000"]
caseBank_2 = ["000","111","000"]

if True:
    def numberOfBeams(bank):
        total = 0
        previous_row_laser_count = 0
        row_laser_count = 0

        for row in bank:
            row_laser_count = row.count("1")
            
            if row_laser_count > 0:
                total += row_laser_count * previous_row_laser_count
                previous_row_laser_count = row_laser_count

        return total
    
print(f"{numberOfBeams(caseBank_1)}")
print(f"{numberOfBeams(caseBank_2)}")