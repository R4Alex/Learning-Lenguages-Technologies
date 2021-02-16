#CREATE SCHEMA `platziblog` DEFAULT CHARACTER SET utf8;
#USE DATABASE 'platziblog';

/*
CREATE TABLE people (
	person_id int PRIMARY KEY AUTO_INCREMENT,
    last_name varchar(255),
    first_name varchar(255),
    address varchar(255),
    city varchar(255),
);
*/

CREATE TABLE `platziblog`.`people` (
  `person_id` INT NOT NULL AUTO_INCREMENT,
  `last_name` VARCHAR(45) NULL,
  `first_name` VARCHAR(45) NULL,
  `adrdress` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  PRIMARY KEY (`person_id`));