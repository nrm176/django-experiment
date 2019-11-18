from .models import Article, Tag

articles = [
    {'ext_id': 1, 'body': '侍ジャパンが決勝で韓国を破り初優勝した。主要国際大会では2009年WBC以来の頂点。稲葉篤紀監督（47）の強い意向でメンバー入りし、'},
    {'ext_id': 2, 'body': 'ロッテから国内フリーエージェント（FA）権を行使した鈴木大地内野手（30）が、楽天に移籍する意思を固めたことが17日、分かった。'}
]

tags = [
    {'ext_id': 1, 'tag_text': '侍ジャパン'},
    {'ext_id': 2, 'tag_text': '野球'},
    {'ext_id': 3, 'tag_text': '楽天'},
    {'ext_id': 4, 'tag_text': 'ロッテ'},
]

tag_articles = [
    {'article': 1, 'tags': [1, 2]},
    {'article': 2, 'tags': [2, 3, 4, ]}
]


def run():

    for tag in tags:
        record = Tag.create(**tag)
        record.save()

    for article in articles:
        record = Article.create(**article)
        record.save()

    for tag_article in tag_articles:
        print(tag_article)
        tags_list = []
        for tag in tag_article.get('tags'):
            tags_list.append(Tag.objects.get(ext_id=tag))

        article = Article.objects.get(ext_id=tag_article.get('article'))
        article.tags.add(*tags_list)


