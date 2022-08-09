-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.29-0ubuntu0.18.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for FundedFuturesNetwork
CREATE DATABASE IF NOT EXISTS `FundedFuturesNetwork` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `FundedFuturesNetwork`;

-- Dumping structure for table FundedFuturesNetwork.Subscriptions
CREATE TABLE IF NOT EXISTS `Subscriptions` (
  `Username` varchar(50) DEFAULT NULL,
  `Tier` int(11) DEFAULT NULL,
  `SystemDate` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table FundedFuturesNetwork.Subscriptions: ~0 rows (approximately)
DELETE FROM `Subscriptions`;
/*!40000 ALTER TABLE `Subscriptions` DISABLE KEYS */;
INSERT INTO `Subscriptions` (`Username`, `Tier`, `SystemDate`) VALUES
	('f', 0, '2022-08-08 16:40:14');
/*!40000 ALTER TABLE `Subscriptions` ENABLE KEYS */;

-- Dumping structure for table FundedFuturesNetwork.Users
CREATE TABLE IF NOT EXISTS `Users` (
  `Username` varchar(50) NOT NULL,
  `First` varchar(50) DEFAULT NULL,
  `Last` varchar(50) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `SystemDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table FundedFuturesNetwork.Users: ~5 rows (approximately)
DELETE FROM `Users`;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` (`Username`, `First`, `Last`, `Address`, `Phone`, `Email`, `Password`, `SystemDate`) VALUES
	('', '', '', '', '', '', '', '2022-08-08 16:21:44'),
	('a', 'a', 'a', 'a', 'a', 'a', 'a', '2022-08-08 16:19:47'),
	('b', 'b', 'b', 'b', 'b', 'b', 'b', '2022-08-08 16:23:06'),
	('e', '', '', 'e', 'e', 'e', 'e', '2022-08-08 16:23:27'),
	('email2', 'first', 'last', 'address', 'phone', 'email2', 'pass', '2022-08-08 16:14:41'),
	('f', 'f', 'f', 'f', 'f', 'f', 'f', '2022-08-08 16:40:14');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
