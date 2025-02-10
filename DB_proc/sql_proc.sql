-- 실습 1 기본적인 기능 확인 및 데이터베이스,테이블 만들어보기
use employees;
select count(*) from employees;
show databases;
show table status;
show tables;
desc employees;
select first_name, gender From employees;
select first_name as '이름', gender as '성별' , hire_date as '회사 입사일'
from employees;
drop database if exists sqldb; -- db존재하면 삭제
create database sqldb;

use sqldb;
create table usertbl -- 회원테이블 생성
( userID CHAR(8) Not null primary Key, -- 사용자 아이디 PK
  name varchar(10) not null, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr	  	CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1	CHAR(3), -- 휴대폰의 앞자리
  mobile2	CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    SMALLINT,  -- 신장
  mDate    	DATE  -- 회원 가입일
  );
  
  CREATE TABLE buytbl -- 회원 구매 테이블(Buy Table의 약자)
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID  	CHAR(8) NOT NULL, -- 아이디(FK)
   prodName 	CHAR(6) NOT NULL, --  물품명
   groupName 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 단가
   amount    	SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES usertbl(userID)
);

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
  
  select * from usertbl;
  select count(*) from usertbl;
  select * from buytbl;
  
  
  -- 실습 2
  use sqldb;
  select * from usertbl;
  select * from usertbl where name='김경호';
  select userID, name from usertbl where birthYear >= 1970 and height >=182;
  select userid, name from usertbl where birthyear >=1970 or height >=182;
  select name, height from usertbl where height between 180 and 183;
  select name, addr from usertbl where addr='경남' or addr='전남' or addr='경북';
  select name,addr from usertbl where addr in ('경남','전남','경북');
  select name, height from usertbl where name like '김%';
  select name, height from usertbl where name like '조__';
  select name, height from usertbl where height>177;
  select name,height from usertbl where height> (select height from usertbl where name ='김경호');
  select name,height from usertbl where height >= (select height from usertbl where addr = '경남'); -- subquerry 에서 반환하는 값이 1개 이상이라서 단일값을 비교할 수 없어서 오류
  select name,height,addr from usertbl where height >= any (select height from usertbl where addr = '경남');
  select name,height,addr from usertbl where height >= (select height from usertbl where addr = '경남' limit 1);
  select name,height,addr from usertbl where height IN (select height from usertbl where addr = '경남');
  select name,height,addr from usertbl where height >= all (select height from usertbl where addr = '경남');
  select name,height,addr from usertbl where addr ='경남';
  
  select * from usertbl;
  
  select name, mDatE from usertbl order by mDate;
  select name, mDatE from usertbl order by mDate desc; -- 내림차순
  select name, mDatE from usertbl order by mDate asc; -- 오름차순
  select addr from usertbl;
  SELECT addr FROM usertbl ORDER BY addr;
  SELECT DISTINCT addr FROM usertbl; -- 중복값 삭제 단일값만 보여줌, unique
  
  
use employees;
select emp_no, hire_date from employees order by hire_date asc;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 5;
SELECT emp_no, hire_date FROM employees ORDER BY hire_date ASC LIMIT 3, 5;

USE sqldb;
CREATE TABLE buytbl2 (SELECT * FROM buytbl);
SELECT * FROM buytbl2;

create table buytbl3 (select userid, prodname from buytbl);
select * from buytbl3;

SELECT userID, amount FROM buytbl ORDER BY userID;
select userid, sum(amount) from buytbl group by userid; -- sum등 집계함수 사용시 groupby를 사용해야한다.
select userid as'사용자 아이디', sum(amount) as '총 구매개수' from buytbl group by userid;
select userid as'사용자 아이디', sum(price*amount) as '총 구매액' from buytbl group by userid;

select name, MAX(height), MIN(height) from usertbl;
select name, MAX(height), MIN(height) from usertbl group by name;

select * from usertbl;

SELECT name, height
   FROM usertbl 
   WHERE height = (SELECT MAX(height)FROM usertbl) 
       OR height = (SELECT MIN(height)FROM usertbl) ;

SELECT COUNT(*) FROM usertbl;

SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자' FROM usertbl;

USE sqldb;
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID ;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   WHERE SUM(price*amount) > 1000 
   GROUP BY userID ;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID
   HAVING SUM(price*amount) > 1000 ;

SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'  
   FROM buytbl 
   GROUP BY userID
   HAVING SUM(price*amount) > 1000 
   ORDER BY SUM(price*amount) ;

SELECT num, groupName, SUM(price * amount) AS '비용' 
   FROM buytbl
   GROUP BY  groupName, num
   WITH ROLLUP;

SELECT groupName, SUM(price * amount) AS '비용' 
   FROM buytbl
   GROUP BY  groupName
   WITH ROLLUP;
   
use sqldb;
create table testTbl1 (id int,userName char(3), age int);
insert into testTbl1 values (1, '홍길동', 23 );  -- 테이블의 컬럼명이 없으려면, 설정된 테이블의 열과 제약조건에 맞춰서 values를 넣어줘야한다.
insert into testTbl1 (id, username) values (2,'설현'); -- 컬럼명을 명시하고, 제약조건에 notnull조건이 없으면 맞춰서 데아터가 들어간다.
INSERT INTO testTbl1(userName, age, id) VALUES ('하니', 26,  3); -- 입력하는 데이터의 순서가 달라도 컬럼명과 일치하면 해당 컬럼에 잘 들어간다.

select * from testTbl1;

CREATE TABLE testTbl2 
  (id  int AUTO_INCREMENT PRIMARY KEY,  -- id 자동 증가로 값이 들어가면 알아서 들어감
   userName char(3), 
   age int );
INSERT INTO testTbl2 VALUES (NULL, '지민', 25);
INSERT INTO testTbl2 VALUES (NULL, '유나', 22);
INSERT INTO testTbl2 VALUES (NULL, '유경', 21);
INSERT INTO testTbl2 VALUES (4,'민지', 21);
INSERT INTO testTbl2 VALUES (null,'수민', 21);
insert into testTbl2 (username, age) values ('민수',25);
SELECT * FROM testTbl2;
SELECT last_insert_id();  -- 가장 마지막에 입력된 값 확인 id만 확인 가능..;

USE  sqldb;

ALTER TABLE testTbl2 AUTO_INCREMENT=100; -- 증가값 100부터 시작
INSERT INTO testTbl2 VALUES (NULL, '찬미', 23);
SELECT * FROM testTbl2;

USE  sqldb;
CREATE TABLE testTbl3 
  (id  int AUTO_INCREMENT PRIMARY KEY, 
   userName char(3), 
   age int );
ALTER TABLE testTbl3 AUTO_INCREMENT=1000; -- id 증가 시작값 1000
SET @@auto_increment_increment=3; -- id값이 증가하는 범위를 설정할 수있음 
INSERT INTO testTbl3 VALUES (NULL, '나연', 20);
INSERT INTO testTbl3 VALUES (NULL, '정연', 18);
INSERT INTO testTbl3 VALUES (NULL, '모모', 19);
SELECT * FROM testTbl3;

CREATE TABLE testTbl4 (id int, Fname varchar(50), Lname varchar(50));
INSERT INTO testTbl4 (SELECT emp_no, first_name, last_name FROM employees.employees); -- 서브쿼리
select * from testTbl4 LIMIT 10;

CREATE TABLE testTbl5 
   (SELECT emp_no, first_name, last_name  FROM employees.employees) ; -- 다른데이터베이스에 있는 테이블에서 가지고오는거

select * from testTbl5 LIMIT 10;


UPDATE testTbl4
    SET Lname = '없음'
    WHERE Fname = 'Kyoichi'; -- safe 업데이트 모드로 업데이트 불가

USE sqldb;
UPDATE buytbl SET price = price * 1.5 ;

USE sqldb;
DELETE FROM testTbl4 WHERE Fname = 'Aamer';

DELETE FROM testTbl4 WHERE Fname = 'Aamer'  LIMIT 5;


DESC usertbl;
drop table buytbl_1;