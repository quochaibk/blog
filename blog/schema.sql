DROP DATABASE IF EXIST blog;
CREATE DATABASE blog;
USE blog;

DROP TABLE IF EXIST users;
CREATE TABLE users(
    id int AUTO_INCREMENT PRIMARY KEY,
    email Varchar(60) not null,
    authencode varchar(40) not null,
    register_time TIMESTAMP,
    last_login TIMESTAMP
);

CREATE TABLE post(
    id int  AUTO_INCREMENT PRIMARY KEY,
    author_users int,
    content TEXT,
    post_date TIMESTAMP,
    title Varchar(256)                
);


CREATE TABLE revision(
    id int AUTO_INCREMENT PRIMARY KEY,
    revision_post int,
    content TEXT,
    create_date TIMESTAMP
);