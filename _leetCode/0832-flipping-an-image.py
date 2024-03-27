#Flipping An Image
#https://leetcode.com/problems/flipping-an-image/description/

caseImage_1 = [[1,1,0],[1,0,1],[0,0,0]]
caseImage_2 = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

if True:
    def flipAndInvertImage(image):
        
        left, right = 0, len(image[0]) -1 

        for row in image:
            left_t = left
            right_t = right
            while left_t < right_t:
                row[left_t], row[right_t] = row[right_t], row[left_t]
                left_t+=1
                right_t-=1

        for row in image:
            for i in range(len(row)):
                row[i] = 1 if row[i] == 0 else 0

        return image        

print(f"{flipAndInvertImage(caseImage_1)}")
print(f"{flipAndInvertImage(caseImage_2)}")