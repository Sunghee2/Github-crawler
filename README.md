# 빅데이터 프로그래밍
하둡 기반의 빅데이터 NLP 시스템 개발

1. 문제정의

   - 프로젝트 주제

   - 프로젝트 목표

     - 나라별 star repo 순위

       > timestamp써서 가능할까? 시간순으로도? 그러면 전체로 하자
       >
       > 그리고 나라 도시…정리해야됨…ㅠ 가능하겠지..?

     - 나라별 user 순위

     - 

2. 시스템 아키텍처
3. 데이터 수집 방법
4. 데이터 분석 방법
5. 데이터 분석 결과



### Todo

**18-11-02**

- [x] github api  
- [x] pip, requests 설치 —> url을 잘못알아서,,,여기까지 모두 의미 없었음ㅎ.. 삽질
- [x] vs code python 설정

> `https://api.github.com/users` 에서 아이디 개수가 불규칙적으로 나오는 것 같음ㅠ
>
> `https://api.github.com/users?since=` -> api 설명에도 *The integer ID of the last User that you've seen.*
>
> -> 여기는 location 안나옴
>
> -> 따로 `https://api.github.com/users/[username]` 해야 보임...



> star : `https://api.github.com/users/Sunghee2/starred`
>
> following : `https://api.github.com/users/Sunghee2/following` 





https://www.maxmind.com/en/free-world-cities-database 도시, 국가 정보

http://www.geodatasource.com/world-cities-database/free

https://stackoverflow.com/questions/3845006/database-of-countries-and-their-cities