-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 27, 2021 at 05:29 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `servicehub`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `bid` int(11) NOT NULL,
  `company` varchar(20) NOT NULL,
  `bookingdate` date NOT NULL,
  `problem` varchar(300) NOT NULL,
  `image` varchar(500) NOT NULL,
  `status` varchar(30) NOT NULL,
  `userid` int(11) NOT NULL,
  `scid` int(11) NOT NULL,
  `enddate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`bid`, `company`, `bookingdate`, `problem`, `image`, `status`, `userid`, `scid`, `enddate`) VALUES
(3, 'acer', '2021-01-09', 'battery problem', '', 'delivered', 7, 2, '2021-01-16'),
(4, 'acer', '2021-01-12', 'battery drain\r\n', '', 'delivered', 7, 2, '2021-01-12'),
(5, 'asus', '2021-01-07', 'battery problem', '', 'delivered', 5, 1, '2021-01-14'),
(6, 'dell', '2021-03-06', 'server problem', '', 'delivered', 12, 3, '2021-03-13'),
(7, 'dell', '2021-03-24', 'charger is not save', '', 'delivered', 14, 4, '2021-03-31'),
(8, 'dell', '2021-04-17', 'power is not supplied to the laptop', '', 'complaint registerred', 16, 6, '2021-04-24'),
(9, 'Apple', '2021-04-18', 'keyboard problem', '', 'booked', 14, 7, '2021-04-25'),
(10, 'Apple', '2021-04-19', 'laptop cant shutdown', '', 'complaint registerred', 17, 5, '2021-04-26'),
(11, 'dell', '2021-04-30', 'virus affected', '/media/aidfar3.jpg', 'processing', 17, 3, '2021-05-07');

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE `company` (
  `cid` int(11) NOT NULL,
  `companyname` varchar(20) NOT NULL,
  `photo` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`cid`, `companyname`, `photo`) VALUES
(2, 'asus', '/media/download%20(8)_CPTL7f5.jpg'),
(3, 'acer', '/media/ACER.jpg'),
(4, 'dell', '/media/dell.jpg'),
(7, 'Apple', '/media/apple_glAWGXa.jpg'),
(8, 'OPPO', '/media/oppo.png');

-- --------------------------------------------------------

--
-- Table structure for table `faq`
--

CREATE TABLE `faq` (
  `id` int(11) NOT NULL,
  `company` varchar(20) NOT NULL,
  `faq` varchar(100) NOT NULL,
  `answer` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faq`
--

INSERT INTO `faq` (`id`, `company`, `faq`, `answer`) VALUES
(1, 'asus', 'freequently restarting', 'check software updates'),
(2, 'dell', 'server problm', 'install library');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL,
  `feedback` varchar(100) NOT NULL,
  `userid` int(11) NOT NULL,
  `scid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fid`, `feedback`, `userid`, `scid`) VALUES
(1, 'very good', 5, 1),
(5, 'feedback..azg', 7, 2),
(6, 'nbad', 7, 2),
(8, 'feedback..very good service', 14, 4),
(9, 'Quality service', 14, 0);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `uname` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `usertype` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `password`, `usertype`, `status`) VALUES
('binimol1212@gmail.com', 'binimol', 'user', 'approved'),
('admin@gmail.com', 'admin', 'admin', 'approved'),
('arjun@gmail.com', 'arjun', 'servicecenter', 'approved'),
('merin@gmail.com', 'merin', 'user', 'approved'),
('acertech@gmail.com', 'acer', 'servicecenter', 'approved'),
('shyamsasi94@gmal.com', '123', 'user', 'approved'),
('binimol1212@gmail.com', 'bini', 'user', 'approved'),
('binimol1212@gmail.com', 'bini', 'user', 'approved'),
('anjana@gmail.com', 'anjana', 'user', 'approved'),
('uforia@gmail.com', 'uforia@123', 'user', 'approved'),
('sera@gmail.com', 'sera@123', 'servicecenter', 'approved'),
('d@gmail.com', 'delna@123', 'user', 'approved'),
('user@gmail.com', 'user@123', 'user', 'approved'),
('null@gmail.com', 'register', 'servicecenter', 'requested'),
('ja@gmail.com', 'register', 'user', 'approved'),
('delna@gmail.com', 'delna@123', 'user', 'approved'),
('service@gmail.com', 'service@123', 'servicecenter', 'approved'),
('applo@gmail.com', 'applo@123', 'servicecenter', 'approved'),
('usan@gmail.com', 'usan@123', 'user', 'approved'),
('agloz@gmail.com', 'aglo@123', 'servicecenter', 'approved'),
('alwinpaul@hotmail.com', '123', 'user', 'approved'),
('oppo@gmail.com', '123', 'servicecenter', 'requested'),
('oppo@gmail.com', '123', 'servicecenter', 'requested');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `message` varchar(300) NOT NULL,
  `messenger` varchar(50) NOT NULL,
  `recipient` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`id`, `message`, `messenger`, `recipient`) VALUES
(7, 'sdftgyui', 'admin@gmail.com', 'acertech@gmail.com'),
(8, 'service amount paid', 'user@gmail.com', 'None'),
(9, 'need urgently', 'usan@gmail.com', 'None'),
(10, 'service amount pending', 'agloz@gmail.com', 'None'),
(11, 'service amount paid', 'usan@gmail.com', 'delna@gmail.com'),
(12, 'service amount paid', 'usan@gmail.com', 'uforia@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

CREATE TABLE `question` (
  `qid` int(11) NOT NULL,
  `companyname` varchar(30) NOT NULL,
  `product` varchar(30) NOT NULL,
  `questionn` varchar(200) NOT NULL,
  `answer` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `question`
--

INSERT INTO `question` (`qid`, `companyname`, `product`, `questionn`, `answer`) VALUES
(2, 'asus', 'laptop', 'restarting frequently', 'check for software update');

-- --------------------------------------------------------

--
-- Table structure for table `screg`
--

CREATE TABLE `screg` (
  `scid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `address` varchar(20) NOT NULL,
  `phoneno` int(11) NOT NULL,
  `company` varchar(20) NOT NULL,
  `product` varchar(20) NOT NULL,
  `aid` int(11) NOT NULL,
  `password` varchar(20) NOT NULL,
  `district` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `screg`
--

INSERT INTO `screg` (`scid`, `name`, `email`, `address`, `phoneno`, `company`, `product`, `aid`, `password`, `district`) VALUES
(1, 'arjun', 'arjun@gmail.com', 'asdfghjkl', 2147483647, 'asus', 'laptop', 12334556, 'arjun', 'ernakulam'),
(2, 'acer tech solutions', 'acertech@gmail.com', 'asus', 2147483647, 'acer', 'laptop', 123456789, 'acer', 'trivandram'),
(3, 'sera', 'sera@gmail.com', 'near tcr postoffice', 2147483647, 'dell', 'laptop', 2147483647, 'sera@123', 'thrissur'),
(4, 'Applo', 'applo@gmail.com', 'Edappily Nagar', 2147483647, 'apple', 'laptop', 2147483647, 'applo@123', 'trivandram'),
(5, 'agloz', 'agloz@gmail.com', 'agronagar', 2147483647, 'Apple', 'laptop', 2147483647, 'aglo@123', 'trivandram'),
(6, 'OPPO Care', 'oppo@gmail.com', 'Panampilly Nagar', 2147483647, 'None', 'Smartphone', 78544, '123', 'None'),
(7, 'OPPO Care', 'oppo@gmail.com', 'Panampilly Nagar', 2147483647, 'None', 'Smartphone', 78544, '123', 'None');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE `userreg` (
  `uid` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(30) NOT NULL,
  `phoneno` bigint(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`uid`, `name`, `email`, `address`, `phoneno`) VALUES
(5, 'binimol', 'binimol1212@gmail.com', 'sdfghj', 2147483647),
(6, 'merin', 'merin@gmail.com', 'merin', 2147483647),
(7, 'SHYAM', 'shyamsasi94@gmal.com', 'dysfsjljscscsojcsc', 2147483647),
(11, 'anjana', 'anjana@gmail.com', 'anjana home', 1234567890),
(12, 'uforia', 'uforia@gmail.com', 'None', 2147483647),
(13, 'delna', 'd@gmail.com', 'None', 2147483647),
(14, 'user', 'user@gmail.com', 'None', 2147483647),
(15, 'jacob', 'ja@gmail.com', 'None', 2147483647),
(16, 'delna', 'delna@gmail.com', 'None', 2147483647),
(17, 'usan', 'usan@gmail.com', 'gracevilla', 9090909090),
(18, 'Alwin', 'alwinpaul@hotmail.com', 'Jake Villa', 7510251964);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `faq`
--
ALTER TABLE `faq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`qid`);

--
-- Indexes for table `screg`
--
ALTER TABLE `screg`
  ADD PRIMARY KEY (`scid`);

--
-- Indexes for table `userreg`
--
ALTER TABLE `userreg`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `bid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `company`
--
ALTER TABLE `company`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `faq`
--
ALTER TABLE `faq`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `qid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `screg`
--
ALTER TABLE `screg`
  MODIFY `scid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `userreg`
--
ALTER TABLE `userreg`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
