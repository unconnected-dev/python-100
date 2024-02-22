#Article Views I
#https://leetcode.com/problems/article-views-i/description/
import pandas

caseData = {
    'article_id': [1, 1, 2, 2, 4, 3, 3],
    'author_id': [3, 3, 7, 7, 7, 4, 4],
    'viewer_id': [5, 6, 7, 6, 1, 4, 4],
    'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
}

caseDataFrame = pandas.DataFrame(caseData)

if True:
    def article_views(views: pandas.DataFrame) -> pandas.DataFrame:
        authors_ids = views[views['author_id'] == views['viewer_id']]['author_id']
        unique_authors = sorted(authors_ids.unique())

        return pandas.DataFrame({'id': unique_authors})

print(f"{article_views(caseDataFrame)}")