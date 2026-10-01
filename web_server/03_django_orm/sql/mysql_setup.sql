-- MySQL 사용자 및 데이터베이스 생성

-- django 사용자 생성
create user 'django'@'%' identified by 'django';

-- utf8mb4 인코딩으로 데이터베이스 생성
create database djangodb character set utf8mb4 collate utf8mb4_unicode_ci;

-- djangodb 데이터베이스의 모든 권한을 django 사용자에게 부여
grant all privileges on djangodb.* to 'django'@'%';

-- 변경된 권한 설정을 즉시 반영
flush privileges;