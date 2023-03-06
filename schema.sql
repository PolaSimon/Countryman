DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;
DROP TABLE IF EXISTS `Orders`;
-- CREATE TABLE `Orders` (
--   `OrderTime` datetime,
--   `Item1` varchar(100) NOT NULL,
--   `Item2` varchar(100) NOT NULL,
--   `Item3` varchar(100) NOT NULL,
--   `Item4` varchar(100) NOT NULL,
-- );




-- DROP DATABASE IF EXISTS 'Countryman';
-- CREATE DATABASE 'Countryman';
-- USE 'Countryman';
-- DROP TABLE IF EXISTS 'Countries';
CREATE TABLE Countries (
  Country_Id int NOT NULL AUTO_INCREMENT,
  Country_Name varchar(100) NOT NULL,
  Country_Offical_Name varchar(100),
  Country_Code varchar(100) NOT NULL,
  Capital_City varchar(100) NOT NULL,
  Region varchar(100),
  Subregion varchar(100),
  Languages varchar(100),
  Currency varchar(100),
  Timezone varchar(100),
  Long_lat varchar(100),
  Flag varchar(300),
  PRIMARY KEY (Country_Id)
);