# log_pipe_back

공부를 해보자!
* 목표 기간 : 23.04.17 ~ 23.04.22  : 집중해서 해보기

### Architecture
![아키텍처](https://user-images.githubusercontent.com/62873925/232751752-e9fd63c2-2307-4e2b-9117-4188ef862ad2.png)

### 시각화할 대상
* HTTP METHOD 
    * status code
* 운영체제 정보
    * ios
    * Android
    * Windows
    * Mac
* date별 요청 수


### Kafka topic
* FluentD -> Kafka : 전처리 없이 한개의 topic
    * topic 이름 : log_injection
* Kafka -> Django : spark로 전처리한 data kafka를 통해 Django
    * topic 이름  : pre_processing


### API Schema
```python
{
    "TIMESTAMP" : datetime
    "HTTP_METHOD" : str
    "STATUS_CODE" : int
    "BROWER_WEB" : str
}
```
| key | type |
|:---:|:---:|
| TIMESTAMP | datetime |
| HTTP_METHOD | string | 
| STATUS_CODE | integer |
| BROWER_WEB | string | 


### 자유로운 의견

<details>
<summary>23.04.18</summary>
<div markdown="1">

로그로 분석할 주제 레퍼런스
* [내 서버에는 누가 들어오는 것일까? - NaverD2](https://d2.naver.com/helloworld/3585246)
* [로그가 뭔지 알아? ELK로 만들어 보다 - 42서울](https://42place.innovationacademy.kr/archives/978)

여러 액세스 로그 시각화 프로젝트에서 보통 ELK 스택을 이용한다.

우리는 kafka, spark, django라는 기술을 익히면서 log를 분석할 수 있는 프로젝트를 모색한다.

왜? 기술 학습을 위해서 !
* 시각화는 django 대시보드를 이용해 만들어 볼 것
* fake-log로 발생하는 대용량의 데이터를 kafka - spark라는 기술을 통해 처리를 해보고, 기술의 원리나 이해를 해볼 것 
</div>
</details>
