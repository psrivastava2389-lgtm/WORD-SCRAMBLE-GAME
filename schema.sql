create database word_scramble;

use word_scramble;

CREATE TABLE e (
  words varchar(15) NOT NULL primary key,
  meaning varchar(50) DEFAULT NULL,

) ;

INSERT INTO e VALUES ('coat','u want it in winters!!'),('door','close it or theif will enter'),('egg','rich in protein'),('flower','colorful and blossoming'),('garden','full of flowers'),('ground','synonym for earth'),('party','enjoy it!!'),('shower','you take it to keep yourself neat and clean'),('table','you study on it'),('toy','kids love it');

CREATE TABLE h (
  words varchar(20) NOT NULL primary key,
  meaning varchar(50) DEFAULT NULL,
  
);

INSERT INTO h VALUES ('gale','a strong wind'),('garment','an item of clothing'),('gaze','a steady intent look'),('havoc','a wide destruction'),('hostile','unfriendly'),('idle','lazy or inactive'),('insane','mentally ill'),('jovial','cheerful'),('junk','old or discarded items'),('kindle','light or set on fire');

CREATE TABLE m (
  words varchar(15) NOT NULL primary key,
  meaning varchar(50) DEFAULT NULL,
  
) ;

INSERT INTO m VALUES ('abandon','look after someone'),('abolish','formally put an end to'),('accelerate','rate of change of velocity'),('advocate','synonym of lawyer'),('ballad','a poem or song that narrates a story'),('bedlam','a scene of uproar and confusion'),('cringe','feeling of awkwardness'),('desolate','unhappiness'),('dismantle','take to pieces'),('fasten','close up securely');

CREATE TABLE scores (
  score int DEFAULT NULL,
  user_id varchar(15) NOT NULL,
  primary key(user_id)
 
);

CREATE TABLE user_detail (
  username varchar(50) NOT NULL DEFAULT 'new user',
  user_id varchar(30) DEFAULT NULL,
  passwd varchar(30) DEFAULT NULL,
  PRIMARY KEY (user_id)
);



