-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 27, 2022 at 08:43 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `szavazatszámláló`
--

-- --------------------------------------------------------

--
-- Table structure for table `indul`
--

CREATE TABLE `indul` (
  `jID` int(2) NOT NULL,
  `fID` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `indul`
--

INSERT INTO `indul` (`jID`, `fID`) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(3, 1),
(3, 2),
(4, 1),
(4, 2),
(5, 1),
(5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `jelölt`
--

CREATE TABLE `jelölt` (
  `szID` int(3) NOT NULL,
  `jID` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `jelölt`
--

INSERT INTO `jelölt` (`szID`, `jID`) VALUES
(1, 1),
(2, 2),
(4, 3),
(15, 4),
(16, 5);

-- --------------------------------------------------------

--
-- Table structure for table `körzet`
--

CREATE TABLE `körzet` (
  `kID` int(1) NOT NULL,
  `korzet_nev` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `körzet`
--

INSERT INTO `körzet` (`kID`, `korzet_nev`) VALUES
(2, 'Jóhalom'),
(3, 'Kisfalu'),
(4, 'Nagyfalu'),
(1, 'Rosszhalom');

-- --------------------------------------------------------

--
-- Table structure for table `szavaz`
--

CREATE TABLE `szavaz` (
  `szID` int(3) NOT NULL,
  `jID` int(2) NOT NULL,
  `fID` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `szavaz`
--

INSERT INTO `szavaz` (`szID`, `jID`, `fID`) VALUES
(7, 1, 1),
(8, 2, 1),
(1, 3, 2),
(4, 3, 2),
(5, 3, 1),
(5, 3, 2),
(9, 3, 1),
(2, 4, 1),
(2, 4, 2),
(3, 4, 1),
(4, 4, 1),
(10, 4, 1),
(1, 5, 1),
(3, 5, 2),
(6, 5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `szavazás`
--

CREATE TABLE `szavazás` (
  `fID` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `szavazás`
--

INSERT INTO `szavazás` (`fID`) VALUES
(1),
(2);

-- --------------------------------------------------------

--
-- Table structure for table `szavazó`
--

CREATE TABLE `szavazó` (
  `szID` int(3) NOT NULL,
  `vnev` varchar(25) NOT NULL,
  `knev` varchar(25) NOT NULL,
  `kID` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `szavazó`
--

INSERT INTO `szavazó` (`szID`, `vnev`, `knev`, `kID`) VALUES
(1, 'Ügyet', 'Lenke', 1),
(2, 'Fá', 'Zoltán', 2),
(3, 'Nyúl', 'Kálmán', 1),
(4, 'Patta', 'Nóra', 1),
(5, 'Kala ', 'Pál', 2),
(6, 'Meg', 'Győző', 2),
(7, 'Hú', 'Zóra', 1),
(8, 'Ipsz', 'Ilonka', 1),
(9, 'Ebéd', 'Elek', 2),
(10, 'Gá', 'Zóra', 2),
(11, 'Hot', 'Elek', 1),
(12, 'Szalmon', 'Ella', 1),
(13, 'Trab', 'Antal', 3),
(14, 'Bac', 'Ilus', 4),
(15, 'Git', 'Áron', 3),
(16, 'Dil', 'Emma', 3),
(17, 'Kér', 'Ede', 3),
(18, 'Virra', 'Dóra', 4),
(19, 'Kispál', 'Inka', 4),
(20, 'Tank', 'Aranka', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `indul`
--
ALTER TABLE `indul`
  ADD PRIMARY KEY (`jID`,`fID`),
  ADD KEY `indul_ibfk_1` (`fID`);

--
-- Indexes for table `jelölt`
--
ALTER TABLE `jelölt`
  ADD PRIMARY KEY (`jID`),
  ADD UNIQUE KEY `szID` (`szID`);

--
-- Indexes for table `körzet`
--
ALTER TABLE `körzet`
  ADD PRIMARY KEY (`kID`),
  ADD UNIQUE KEY `korzet_nev` (`korzet_nev`);

--
-- Indexes for table `szavaz`
--
ALTER TABLE `szavaz`
  ADD PRIMARY KEY (`szID`,`fID`) USING BTREE,
  ADD KEY `jID` (`jID`),
  ADD KEY `fID` (`fID`) USING BTREE;

--
-- Indexes for table `szavazás`
--
ALTER TABLE `szavazás`
  ADD PRIMARY KEY (`fID`);

--
-- Indexes for table `szavazó`
--
ALTER TABLE `szavazó`
  ADD PRIMARY KEY (`szID`),
  ADD KEY `kID` (`kID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jelölt`
--
ALTER TABLE `jelölt`
  MODIFY `jID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `indul`
--
ALTER TABLE `indul`
  ADD CONSTRAINT `indul_ibfk_1` FOREIGN KEY (`fID`) REFERENCES `szavazás` (`fID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `indul_ibfk_2` FOREIGN KEY (`jID`) REFERENCES `jelölt` (`jID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `jelölt`
--
ALTER TABLE `jelölt`
  ADD CONSTRAINT `jelölt_ibfk_1` FOREIGN KEY (`szID`) REFERENCES `szavazó` (`szID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `szavaz`
--
ALTER TABLE `szavaz`
  ADD CONSTRAINT `szavaz_ibfk_1` FOREIGN KEY (`szID`) REFERENCES `szavazó` (`szID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `szavaz_ibfk_2` FOREIGN KEY (`jID`) REFERENCES `jelölt` (`jID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `szavaz_ibfk_3` FOREIGN KEY (`fID`) REFERENCES `szavazás` (`fID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `szavazó`
--
ALTER TABLE `szavazó`
  ADD CONSTRAINT `szavazó_ibfk_1` FOREIGN KEY (`kID`) REFERENCES `körzet` (`kID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
