#Not Boring Movies
#https://leetcode.com/problems/not-boring-movies/description/
import pandas

caseData = {
    'id': [1, 2, 3, 4, 5],
    'movie': ['War', 'Science', 'Irish', 'Ice Song', 'House Card'],
    'description': ['great 3D', 'fiction', 'boring', 'Fantasy', 'Interesting'],
    'rating': [8.9, 8.5, 6.2, 8.6, 9.1]
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def not_boring_movies(cinema):
        return cinema.loc[(cinema['id'] %2==1) & (cinema['description']!="boring")].sort_values(by='rating', ascending=False)

print(f"{not_boring_movies(caseDataFrame).to_markdown(index=False)}")