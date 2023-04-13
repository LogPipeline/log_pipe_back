# log_pipe_back

공부를 해보자! 

### 공부공부
* 목표 기간 : 23.04.17 ~ 23.04.22  : 집중해서 해보기


[선순위]

```
아이피 주소 -> 68.244.124.248 - - 
날짜 -> [13/Apr/2023:23:22:35 +0900] 
Method -> "POST /apps/cart.jsp?appID=2081 HTTP/1.0" 
status code ->200 
port number -> 4939 
url -> "http://www.cox.net/privacy/" 
brower injection - >"Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/535.29.1 (KHTML, like Gecko) 
                     Version/5.1 Safari/535.29.1"
```

사용자 들어온 스펙 -> 수집 후 대시보드

1. status numbering (200, 404, 500... 등등)
2. brower 정보 
3. 날짜 정보 
4. HTTP METHOD 정보 (GET, POST, DELETE, PUT)
5. 운영체제 정보 

--------------------------------------------------
[후순위]

우리가 사이트를 운영한다
운영하는 사이트로부터 사용자가 접속을 한다
로그가 생성된다


사용자가 로그인을 했는가?
-> 사용자에 대한 정보
    - 성별
    - 나이
    - 신규회원인지?

-> 어떤 사이트를 봤는가?
    - Resource 
    - tistory
        - 포스팅 uri
        - admin uri
        - 수정 uri

- 로그의 정보가 더 있어야 되지않나? 시각화를 쳤는데
-> 로그에 국가정보, uri 사이트라는 가정에서 API 명시하고,유저 정보를 넣는다./
-> 시각화하고 추출할 가치가 높아진다

그니까 저는 실습이 목적 | 분석이든 대시보드든 상관없어.. 
로그로 시각화 물어본거였어요. -> 이게 안된다고 하면, 경험자의 의견을 따를

-> 시스템 상에서 대시보드



### 1차 전처리

```python
data = {
    "originer": "원본 로그",
    "ip" : "64.233.172.14",
    "timezone" : "16/Apr/2023:05:33:21 +0900",
    "method" : "PUT",
    "resource" : "/app/main/posts",   
    "header" : "HTTP/1.0",
    "status" : 200,
    "port" : 5055,
    "url" : "http://www.harrell.info/wp-content/wp-content/list/search.html" ,
    "device" : "http://lee.info/" "Mozilla/5.0 (Linux; Android 3.2.4) AppleWebKit/532.0 (KHTML, like Gecko)",
    "brower_info" : "Chrome/51.0.819.0 Safari/532.0",
}
```


### 2차 전처리

```python
data = {
    "originer": "원본 로그",
    "ip" : "64.233.172.14",
    "timezone" : "14/Apr/2023:01:14:35",
    "date" : "14/Apr/2023",
    "time" : "01:14:35"
    ""
    "method" : "PUT",
    "resource" : "/app/main/posts",   
    "header" : "HTTP/1.0",
    "status" : 200,
    "port" : 5055,
    "url" : "http://www.harrell.info/wp-content/wp-content/list/search.html" ,
    "device" : "http://lee.info/" "Mozilla/5.0 (Linux; Android 3.2.4) AppleWebKit/532.0 (KHTML, like Gecko)",
    "brower_info" : "Chrome/51.0.819.0 Safari/532.0",
}
```
