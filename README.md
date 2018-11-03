# 빅데이터 프로그래밍
하둡 기반의 빅데이터 NLP 시스템 개발

1. 문제정의

   - 프로젝트 주제

   - 프로젝트 목표

     - 나라별 star repo 순위

       > timestamp써서 가능할까? 시간순으로도? 그러면 전체로 하자
       >
       > 그리고 나라 도시…정리해야됨…ㅠ 가능하겠지..?

     - 나라별 user 몇명인지, 순위

     - follower 많이 한 것 

2. 시스템 아키텍처
3. 데이터 수집 방법
4. 데이터 분석 방법
5. 데이터 분석 결과



### Todo

**18-11-02**

- [x] github api  
- [x] pip, requests 설치 —> url을 잘못알아서,,,여기까지 모두 의미 없었음ㅎ.. 삽질
- [x] vs code python 설정

> - `https://api.github.com/users` 에서 아이디 개수가 불규칙적으로 나오는 것 같음ㅠ
>
> - `https://api.github.com/users?since=` -> api 설명에도 *The integer ID of the last User that you've seen.*
>
>   ​	-> 여기는 location 안나옴
>
>   ​		-> 따로 `https://api.github.com/users/[username]` 해야 보임...

> star : `https://api.github.com/users/Sunghee2/starred`
>
> following : `https://api.github.com/users/Sunghee2/following` 

<br/>

**18-11-03**

- [x] python3....
- [x] json to csv file
- [x] 마지막 id 받아오기 
- [x] 마지막 value 받아오기
- [x] csv파일에 덮어쓰기
- [x] /user/sunghee2 user상세정보 요청
- [x] series => df
- [x] 두 개의 df join하기 
- [x] user상세정보 api -> web scraping (취소)
- [ ] 

> :bug: pandas 2.* 버전은 안됨.. 
>
> ​	-> pip3 사용, `#!/usr/bin/env python3` 맨 앞에 작성
>
> - pandas에 to_csv 함수 : http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html?highlight=csv#pandas.DataFrame.to_csv
>
> - csv 전체를 읽어오는데 마지막 것만 읽어올 수 없을까…. -> index 
>
> - 맨 처음 실행했을 때(csv파일이 없을 때) 에러처리
>
> - 마지막 index 받아오는 것 index 잘못함[-2:-1] 이렇게 하면 마지막에서 2번째 출력됨 -> [-1:]
>
> - csv 파일 추가되는데 df의 row index가 그대로 들어감... 상관없나..? 일단 냅두자.. -> csv파일이랑 다르게 인덱스 제대로 나옴 -> df의 row index 없앰
>
> - *API rate limit exceeded* -> oauth/ params에 client_id, client_secret 보내주면 됨
>
>   ​	(인증되었으면 시간당 5000, 인증x면 시간당 60) https://api.github.com/rate_limit : 남아있는 요청 횟수
>
> - *ValueError: If using all scalar values, you must pass an index* -> `read_json(typ='series')`
>
> <br/>
>
> - api 호출 너무 많아서 user details은 web에서 긁어오자……….ㅜ -> 근데 api보다 엄청 느린 듯 ㅠㅠㅠㅠ
>
>   ​	xxxxxxxx api는 제한이 있다 해도 30명당 20초인데 scraping은 한 명당 50초 가까이 걸림 ==> 다시 변경 
>
>   ​	star은 또 api를 이용해야하니깐 starred는 scraping으로 하자 -> 그냥 starred는 따로 파일 만들자...
>
> - *Command "python setup.py egg_info" failed with error code 1 in /private/tmp/pip-install-lgil0nds/BeautifulSoup/*   --> 코드만 보고 BeautifulSoup로 다운받았는데 알고보니 bs4로 install 했어야 했다....

> crawler 참고 코드
>
> https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas





https://www.maxmind.com/en/free-world-cities-database 도시, 국가 정보

http://www.geodatasource.com/world-cities-database/free

https://stackoverflow.com/questions/3845006/database-of-countries-and-their-cities