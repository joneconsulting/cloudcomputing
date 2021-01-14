<<<<<<< HEAD
CREATE TABLE member(userid int, pwd varchar(10));
=======
CREATE TABLE member(userid varchar(20) primary key, pwd varchar(10), name varchar(20));

INSERT INTO member(userid, pwd, name)
VALUES('user1', 'user1', '사용자1');
>>>>>>> 8b280e030c759f32688d3c747155e110c6f4795a
