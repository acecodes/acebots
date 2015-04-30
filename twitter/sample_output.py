"""
Sample data: global trends from 4/29/2015 @ 5:43 PM
"""

data = [{'locations': [{'woeid': 1, 'name': 'Worldwide'}], 'trends': [{'query': '%22Gran+Hermano%22', 'name': 'Gran Hermano', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Gran+Hermano%22'}, {'query': '%23%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA_%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87_%D9%84%D8%A7%D8%AA%D8%AC%D8%AF%D9%87%D8%A7_%D8%A8%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85', 'name': '#مصطلحات_سعوديه_لاتجدها_بالعالم', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA_%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D9%87_%D9%84%D8%A7%D8%AA%D8%AC%D8%AF%D9%87%D8%A7_%D8%A8%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85'}, {'query': '%23BatallasLaVoz', 'name': '#BatallasLaVoz', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23BatallasLaVoz'}, {'query': '%23%D9%84%D9%88_%D8%A7%D9%84%D9%82%D8%AA%D9%84_%D8%AD%D9%84%D8%A7%D9%84_%D9%83%D9%86%D8%AA_%D9%82%D8%AA%D9%84%D8%AA', 'name': '#لو_القتل_حلال_كنت_قتلت', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23%D9%84%D9%88_%D8%A7%D9%84%D9%82%D8%AA%D9%84_%D8%AD%D9%84%D8%A7%D9%84_%D9%83%D9%86%D8%AA_%D9%82%D8%AA%D9%84%D8%AA'}, {'query': 'Paran%C3%A1', 'name': 'Paraná', 'promoted_content': None, 'url': 'http://twitter.com/search?q=Paran%C3%A1'}, {'query': '%23GoodbyeRevenge', 'name': '#GoodbyeRevenge', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23GoodbyeRevenge'}, {'query': '%23MeChamullaronCon', 'name': '#MeChamullaronCon', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%23MeChamullaronCon'}, {'query': 'MahomiesAreExcitedForDirtyWork', 'name': 'MahomiesAreExcitedForDirtyWork', 'promoted_content': None, 'url': 'http://twitter.com/search?q=MahomiesAreExcitedForDirtyWork'}, {'query': '%22Nigel+Pearson%22', 'name': 'Nigel Pearson', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Nigel+Pearson%22'}, {'query': '%22Union+Square%22', 'name': 'Union Square', 'promoted_content': None, 'url': 'http://twitter.com/search?q=%22Union+Square%22'}], 'created_at': '2015-04-30T00:34:38Z', 'as_of': '2015-04-30T00:39:24Z'}]

for i in data[0]['trends']:
    print(i['name'])