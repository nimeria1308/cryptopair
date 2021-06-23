-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2021 at 10:51 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cryptopair`
--
CREATE DATABASE IF NOT EXISTS `cryptopair` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `cryptopair`;

-- --------------------------------------------------------

--
-- Table structure for table `bids`
--

CREATE TABLE `bids` (
  `id` int(11) NOT NULL,
  `pair` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `bid` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `currencies`
--

CREATE TABLE `currencies` (
  `id` int(11) NOT NULL,
  `name` char(6) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `currencies`
--

INSERT INTO `currencies` (`id`, `name`, `description`) VALUES
(1, 'USD', 'US Dollar'),
(2, 'EUR', 'Euro'),
(3, 'CAD', 'Canadian Dollar'),
(4, 'JPY', 'Japanese Yen'),
(5, 'GBP', 'British Pound Sterling'),
(6, 'CHF', 'Swiss Franc'),
(7, 'AUD', 'Australian Dollar'),
(8, 'BTC', 'Bitcoin'),
(9, 'ETH', 'Ethereum'),
(10, 'XRP', 'Ripple'),
(11, 'USDT', 'Tether');

-- --------------------------------------------------------

--
-- Table structure for table `pairs`
--

CREATE TABLE `pairs` (
  `id` int(11) NOT NULL,
  `base` int(11) NOT NULL,
  `quote` int(11) NOT NULL,
  `kraken` char(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pairs`
--

INSERT INTO `pairs` (`id`, `base`, `quote`, `kraken`) VALUES
(1, 8, 1, 'XXBTZUSD'),
(2, 8, 2, 'XXBTZEUR'),
(3, 8, 3, 'XXBTZCAD'),
(4, 8, 4, 'XXBTZJPY'),
(5, 8, 5, 'XXBTZGBP'),
(6, 8, 6, 'XBTCHF'),
(7, 8, 7, 'XBTAUD'),
(8, 8, 11, 'XBTUSDT'),
(9, 9, 1, 'XETHZUSD'),
(10, 9, 2, 'XETHZEUR'),
(11, 9, 3, 'XETHZCAD'),
(12, 9, 4, 'XETHZJPY'),
(13, 9, 5, 'XETHZGBP'),
(14, 9, 6, 'ETHCHF'),
(15, 9, 7, 'ETHAUD'),
(16, 9, 8, 'XETHXXBT'),
(17, 9, 11, 'ETHUSDT'),
(18, 10, 1, 'XXRPZUSD'),
(19, 10, 2, 'XXRPZEUR'),
(20, 10, 3, 'XXRPZCAD'),
(21, 10, 4, 'XXRPZJPY'),
(22, 10, 5, 'XRPGBP'),
(23, 10, 7, 'XRPAUD'),
(24, 10, 8, 'XXRPXXBT'),
(25, 10, 9, 'XRPETH'),
(26, 10, 11, 'XRPUSDT'),
(27, 11, 1, 'USDTZUSD'),
(28, 11, 2, 'USDTEUR'),
(29, 11, 3, 'USDTCAD'),
(30, 11, 4, 'USDTJPY'),
(31, 11, 5, 'USDTGBP'),
(32, 11, 6, 'USDTCHF'),
(33, 11, 7, 'USDTAUD');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bids`
--
ALTER TABLE `bids`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pair_fk_constraint` (`pair`);

--
-- Indexes for table `currencies`
--
ALTER TABLE `currencies`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pairs`
--
ALTER TABLE `pairs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base` (`base`),
  ADD KEY `quote` (`quote`),
  ADD UNIQUE(`base`, `quote`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bids`
--
ALTER TABLE `bids`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `currencies`
--
ALTER TABLE `currencies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `pairs`
--
ALTER TABLE `pairs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bids`
--
ALTER TABLE `bids`
  ADD CONSTRAINT `pair_fk_constraint` FOREIGN KEY (`pair`) REFERENCES `pairs` (`id`);

--
-- Constraints for table `pairs`
--
ALTER TABLE `pairs`
  ADD CONSTRAINT `base_fk_constraint` FOREIGN KEY (`base`) REFERENCES `currencies` (`id`),
  ADD CONSTRAINT `quote_fk_constraint` FOREIGN KEY (`quote`) REFERENCES `currencies` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
