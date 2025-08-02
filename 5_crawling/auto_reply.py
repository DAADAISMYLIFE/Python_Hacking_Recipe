import requests

login_url="https://shop.hakhub.net/wp-login.php"
reply_url = "https://shop.hakhub.net/wp-comments-post.php"
account_form_data = {"log" : "customer01", "pwd" : "customer01!!"}

# 세션을 유지하여 쿠키 보존
with requests.Session() as s:
    r = requests.post(login_url, data=account_form_data)
    
    comment_form_data = {
        "rating" : 5,
        "comment" : "댓글 작성 테스트",
        "comment_post_ID" : "70",
        "comment_parent" : 0,
    }
    
    # 쿠키 보존되기 때문에 생략 가능
    r = s.post(reply_url, cookies=s.cookies, data=comment_form_data)
    
    if r.status_code == 200:
        print("댓글 작성 완료!")
    elif r.status_code == 403:
        print("댓글 작성 권한이 없거나 로그인 실패")
    elif r.status_code == 409:
        print("이미 댓글을 작성함!")
    elif r.status_code == 429:
        print("댓글을 너무 빨리 달고 있습니다.")
    else:
        print(f"댓글 작성 오류 코드 : {r.status_code}")
    
    