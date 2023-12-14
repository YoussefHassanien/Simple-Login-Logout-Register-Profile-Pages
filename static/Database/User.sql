

CREATE TABLE Usernew(
    userID serial ,
    Fname varchar(30) not null ,
    Lname varchar(30) not null ,
    phone varchar(30) not null,
    Address varchar(100),
    Email varchar(100) UNIQUE not null ,
    password varchar(30)  not null ,
    Job varchar(50),
    Facebook varchar(100),
    Github varchar(100),
    Instagram varchar(100),
    Linkedin varchar(100),
    Image varchar(300)

);
