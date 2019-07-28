-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 28, 2019 at 08:21 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `username` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('Sajeeb', 'Sajeeb'),
('admin', 'admin'),
('Shafayat', 'Shafayat'),
('Mansur', 'Mansur');

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `dName` varchar(100) NOT NULL,
  `pName` varchar(100) NOT NULL,
  `room` int(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`dName`, `pName`, `room`) VALUES
('Rahul Choudhary', 'Viky', 7),
('Rahul Choudhary', 'Varun', 7),
('Jatinder', 'Kaman', 1),
('Jatinder', 'Rajesh', 1),
('Jatinder', 'Geetanjali', 1),
('Poonam Sharma', 'Shaifali', 3),
('Poonam Sharma', 'Sheetal', 3),
('Reetu Prashar', 'Rajni', 4),
('Reetu Prashar', 'Ravneet', 4),
('Supreet Prashar', 'Sahil', 5),
('Supreet Prashar', 'Tanish', 5),
('Vikas Gupta', 'Tammana', 6),
('Vikas Gupta', 'Tanish', 6),
('Vikas Gupta', 'Pankaj', 6);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE IF NOT EXISTS `doctor` (
  `count` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(10) NOT NULL,
  `id` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` int(5) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `blood` varchar(10) NOT NULL,
  `dept` varchar(40) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `room` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`count`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`count`, `date`, `id`, `name`, `age`, `gender`, `blood`, `dept`, `phone`, `email`, `status`, `address`, `room`, `username`, `password`) VALUES
(1, '15-02-2018', 'D1', 'Jatinder Sharma', 36, 'Male', 'O+', 'Plastic surgeon', '8008004476', 'jatinder@gmail.com', 'Married', 'Indira colony pathankot', 1, 'jatinder', 'jatinder'),
(2, '10-03-2018', 'D2', 'Pawan Sharma', 40, 'Male', 'AB+', 'Gynecologist', '9648054476', 'pawan12@gmail.com', 'Married', 'Shastri nagar pathankot', 2, 'pawan', 'pawan'),
(3, '10-08-2018', 'D3', 'Poonam Sharma', 28, 'Female', 'AB+', 'Gynecologist', '9686544476', 'poonamsharma@gmail.com', 'Married', 'sarna pathankot', 3, 'poonam', 'poonam'),
(4, '10-05-2019', 'D4', 'Reetu Prashar', 38, 'Female', 'O+', 'Gynecplogist', '8967452876', 'reetuprashar@gmail.com', 'Married', 'sujanpur pathankot', 4, 'reetu', 'reetu'),
(5, '10-07-2019', 'D5', 'Supreet Prashar', 33, 'Female', 'B+', 'Dentist', '6895755876', 'supreetprashar@gmail.com', 'Married', 'sujanpur pathankot', 5, 'supreet', 'supreet'),
(6, '10-07-2018', 'D6', 'Vikas Gupta', 33, 'Male', 'B+', 'General Physician', '8968755876', 'vikas@gmail.com', 'Married', 'sujanpur pathankot', 6, 'Vikas', 'Vikas'),
(7, '10-07-2018', 'D7', 'Rahul Sharma', 36, 'Male', 'O+', 'ENT specialist', '9756842384', 'rahul@gmail.com', 'Married', 'shastri nagar pathankot', 7, 'rahul', 'rahul');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `count` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(10) NOT NULL,
  `id` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `age` int(5) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL,
  `disease` varchar(20) NOT NULL,
  `room` int(11) NOT NULL,
  PRIMARY KEY (`count`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`count`, `date`, `id`, `name`, `age`, `gender`, `address`, `phone`, `status`, `disease`, `room`) VALUES
(1, '16-02-2019', '1', 'Harnesh', 19, 'Male', 'pathankot indira colony', '9687596486', 'Unmarried', 'Fever', 10),
(2, '16-02-2019', '2', 'Muskan', 28, 'Female', 'pathankot Govind colony', '6859596486', 'married', 'malaria', 11),
(3, '20-05-2019', '3', 'Kunal', 22, 'Male', 'Arun nagar pathankot ', '8695749235', 'Unmarried', 'Typhoid', 12),
(4, '25-07-2019', '4', 'Kamal', 35, 'Male', 'Arun nagar pathankot ', '6825449235', 'married', 'Jaundice', 13);

-- --------------------------------------------------------

--
-- Table structure for table `receptionist`
--

DROP TABLE IF EXISTS `receptionist`;
CREATE TABLE IF NOT EXISTS `receptionist` (
  `count` int(11) NOT NULL AUTO_INCREMENT,
  `joining` varchar(15) NOT NULL,
  `id` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `age` int(5) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `blood` varchar(10) NOT NULL,
  `email` varchar(40) NOT NULL,
  `phone` varchar(17) NOT NULL,
  `address` varchar(225) NOT NULL,
  `status` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  PRIMARY KEY (`count`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `receptionist`
--

INSERT INTO `receptionist` (`count`, `joining`, `id`, `name`, `age`, `gender`, `blood`, `email`, `phone`, `address`, `status`, `username`, `password`) VALUES
(1, '1-01-2018', 'R1', 'Shalini Sharma', 22, 'Female', 'AB+', 'shalini@gmail.com', '8659754962', 'Gandhi nagar pathankot', 'unmarried', 'shalini', 'shalini'),
(2, '20-01-2018', 'R2', 'Gauri Manhas', 20, 'Female', 'B+', 'gauri@gmail.com', '7685549623', 'Gandhi nagar pathankot', 'unmarried', 'gauri', 'gauri'),
(3, '22-03-2019', 'R3', 'Rahul Kumar', 25, 'Male', 'B-', 'rahul1302@gmail.com', '8697542386', 'Mamun pathankot', 'unmarried', 'rahul', 'rahul'),
(4, '20-09-2018', 'R4', 'Shalija Thakur', 23, 'Female', 'O+', 'shalija@gmail.com', '6895742386', 'Badhani pathankot', 'unmarried', 'shalija', 'shalija');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
