-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 13, 2019 at 05:04 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.1.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collegedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendtable`
--

CREATE TABLE `attendtable` (
  `name` varchar(100) NOT NULL,
  `srno` int(10) NOT NULL,
  `attfrom` date NOT NULL,
  `utype` varchar(100) NOT NULL,
  `attto` date NOT NULL,
  `pdays` int(100) NOT NULL,
  `adays` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `attendtable`
--

INSERT INTO `attendtable` (`name`, `srno`, `attfrom`, `utype`, `attto`, `pdays`, `adays`) VALUES
('akie', 1, '2019-08-13', 'Student', '2019-08-30', 10, 7);

-- --------------------------------------------------------

--
-- Table structure for table `coursetable`
--

CREATE TABLE `coursetable` (
  `course` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `coursetable`
--

INSERT INTO `coursetable` (`course`) VALUES
('BTECH'),
('MBA'),
('PHD');

-- --------------------------------------------------------

--
-- Table structure for table `examtable`
--

CREATE TABLE `examtable` (
  `srno` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `marks` int(100) NOT NULL,
  `tmarks` int(100) NOT NULL,
  `percentage` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `examtable`
--

INSERT INTO `examtable` (`srno`, `name`, `marks`, `tmarks`, `percentage`) VALUES
(1, 'akie', 85, 100, 85);

-- --------------------------------------------------------

--
-- Table structure for table `feetable`
--

CREATE TABLE `feetable` (
  `name` varchar(100) NOT NULL,
  `srno` int(100) NOT NULL,
  `tfee` int(100) NOT NULL,
  `sem` varchar(100) NOT NULL,
  `paid` int(100) NOT NULL,
  `pdate` date NOT NULL,
  `mode` varchar(100) NOT NULL,
  `due` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sectiontable`
--

CREATE TABLE `sectiontable` (
  `section` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sectiontable`
--

INSERT INTO `sectiontable` (`section`) VALUES
('CSE'),
('Marketing');

-- --------------------------------------------------------

--
-- Table structure for table `stafftable`
--

CREATE TABLE `stafftable` (
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `qualf` varchar(100) NOT NULL,
  `eadd` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `salary` int(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `image` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stafftable`
--

INSERT INTO `stafftable` (`fname`, `lname`, `qualf`, `eadd`, `subject`, `salary`, `dob`, `gender`, `course`, `phone`, `address`, `image`) VALUES
('abc', 'def', 'MBA', 'abc@gmail.com', 'Data Structure', 10000, '2019-08-13', 'Female', 'MBA', '9463364708', 'msn\n\n\n', '1565707194banner4.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `studenttable`
--

CREATE TABLE `studenttable` (
  `srno` int(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `fathername` varchar(100) NOT NULL,
  `mothername` varchar(100) NOT NULL,
  `foccu` varchar(100) NOT NULL,
  `moccu` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `section` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `bg` varchar(100) NOT NULL,
  `landline` varchar(100) NOT NULL,
  `religion` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `admdate` date NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studenttable`
--

INSERT INTO `studenttable` (`srno`, `name`, `lname`, `fathername`, `mothername`, `foccu`, `moccu`, `dob`, `gender`, `course`, `section`, `phone`, `bg`, `landline`, `religion`, `address`, `admdate`, `image`) VALUES
(1, 'akie', 'puri', 'npuri', 'hpuri', 'Service', 'Service', '2019-08-13', 'Male', 'BTECH', 'CSE', '7837239393', 'B+', '2457981', 'Hindu', '686 msn.\n\n', '2019-08-13', '1565704089banner1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `subjecttable`
--

CREATE TABLE `subjecttable` (
  `subject` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subjecttable`
--

INSERT INTO `subjecttable` (`subject`) VALUES
('Data Structure');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `uname` varchar(100) NOT NULL,
  `pass` varchar(100) NOT NULL,
  `utype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`uname`, `pass`, `utype`) VALUES
('akie', '1', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendtable`
--
ALTER TABLE `attendtable`
  ADD PRIMARY KEY (`srno`),
  ADD UNIQUE KEY `present` (`pdays`);

--
-- Indexes for table `coursetable`
--
ALTER TABLE `coursetable`
  ADD PRIMARY KEY (`course`);

--
-- Indexes for table `examtable`
--
ALTER TABLE `examtable`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `feetable`
--
ALTER TABLE `feetable`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `sectiontable`
--
ALTER TABLE `sectiontable`
  ADD PRIMARY KEY (`section`),
  ADD UNIQUE KEY `section` (`section`);

--
-- Indexes for table `stafftable`
--
ALTER TABLE `stafftable`
  ADD PRIMARY KEY (`phone`);

--
-- Indexes for table `studenttable`
--
ALTER TABLE `studenttable`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `subjecttable`
--
ALTER TABLE `subjecttable`
  ADD PRIMARY KEY (`subject`),
  ADD UNIQUE KEY `subject` (`subject`);

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`uname`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `studenttable`
--
ALTER TABLE `studenttable`
  MODIFY `srno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
