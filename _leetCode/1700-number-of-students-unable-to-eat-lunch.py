#Number Of Students Unable To Eat Lunch
#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

caseStudents_1 = [1,1,0,0]
caseSandwiches_1 = [0,1,0,1]

caseStudents_2 = [1,1,1,0,0,1]
caseSandwiches_2 = [1,0,0,0,1,1]

if True:
    def countStudents(students, sandwiches):

        while sandwiches:
            if sandwiches[0] in students:
                students.remove(sandwiches[0])
                sandwiches.pop(0)
            else:
                break
        
        return len(sandwiches)

print(f"{countStudents(caseStudents_1, caseSandwiches_1)}")
print(f"{countStudents(caseStudents_2, caseSandwiches_2)}")