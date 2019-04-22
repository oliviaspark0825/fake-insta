from django import template

register = template.Library()

@register.filter
# 나중에 필터 | 앞에 쓸 인자 넣기, 여기서 post.content 하면 나중에 post.content의 .content는 없으니까
def hashtag_link(post):
    # 해당 포스트가 가지고 있는 모든 해쉬태그 순회하면서, #으로시작하는거 모든 것을 링크 걸기
    content = post.content # 인자로 가지고 오고 내용을
    hashtags = post.hashtags.all()
    # hashtags를 순회하면서, content 내에서 해당 문자열(해시태그) 링크를 포함한 문자열로 치환
    for hashtag in hashtags:
        content = content.replace(hashtag.content, f'<a href="/posts/hashtag/{ hashtag.pk }/">{ hashtag.content }</a>')    
        # content = content.replace(f'{hashtag.content}', f'<a href="/posts/hashtag/{ hashtag.id }/">{ hashtag.content }</a>')
    return content
     
