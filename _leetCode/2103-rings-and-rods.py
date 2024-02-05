#Rings And Rods
#https://leetcode.com/problems/rings-and-rods/description/

caseRings_1 = "B0B6G0R6R0R6G9"
caseRings_2 = "B0R0G0R9R0B0G0"
caseRings_3 = "G4"

if False:
    def countPoints(rings):
        r = 0
        for i in range(10):
            r_ = f'R{i}'
            b_ = f'B{i}'
            g_ = f'G{i}'

            if r_ in rings and b_ in rings and g_ in rings:
                r += 1

        return r

if True:
    def countPoints(rings):
        r = 0
        for i in range(10):
            i = str(i)
            if 'R'+i in rings and 'B'+i in rings and 'G'+i in rings:
                r+=1
        
        return r

print(f"{countPoints(caseRings_1)}")
print(f"{countPoints(caseRings_2)}")
print(f"{countPoints(caseRings_3)}")