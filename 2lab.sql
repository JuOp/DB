CREATE DATABASE lab2_db; 
  
 CREATE TABLE customers( 
     id integer NOT NULL UNIQUE PRIMARY KEY, 
     full_name varchar(50) NOT NULL, 
     timestamp timestamp NOT NULL, 
     delivery_address text NOT NULL 
 ); 
  
 CREATE TABLE products( 
     id varchar NOT NULL UNIQUE PRIMARY KEY, 
     name varchar NOT NULL UNIQUE, 
     description text, 
     price double precision NOT NULL check ( price > 0 ) 
 ); 
  
 CREATE TABLE orders( 
     code integer NOT NULL UNIQUE PRIMARY KEY, 
     customer_id integer REFERENCES customers(id), 
     total_sum double precision NOT NULL check ( total_sum > 0 ), 
     is_paid boolean NOT NULL 
 ); 
  
 CREATE TABLE order_item( 
     order_code integer NOT NULL UNIQUE REFERENCES orders(code), 
     products_id varchar NOT NULL UNIQUE REFERENCES products(id), 
     quantity integer NOT NULL check ( quantity > 0 ) 
 ); 
  
  
 CREATE TABLE students( 
     id varchar(9) NOT NULL UNIQUE PRIMARY KEY, 
     full_name text, 
     age smallint, 
     birthdate date, 
     gender char(1), 
     GPA double precision, 
     personal_info text, 
     needs_dormitory boolean, 
     additional_info text 
 ); 
  
 CREATE TABLE instructors( 
     id varchar(9) NOT NULL UNIQUE PRIMARY KEY, 
     full_name text, 
     speaking_languages text, 
     work_experience text, 
     remote_lessons_possible boolean 
 ); 
  
 CREATE TABLE participants( 
     lesson_id varchar(8) NOT NULL UNIQUE PRIMARY KEY, 
     lesson_title text, 
     teaching_instructor text, 
     studying_students smallint, 
     room_number smallint 
 );