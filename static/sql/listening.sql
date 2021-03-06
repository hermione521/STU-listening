-- MySQL dump 10.13  Distrib 5.5.28, for osx10.6 (i386)
--
-- Host: localhost    Database: listening
-- ------------------------------------------------------
-- Server version	5.5.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `BBC`
--

DROP TABLE IF EXISTS `BBC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BBC` (
  `indexID` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `fileName` varchar(255) DEFAULT NULL,
  `subtitleFile` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BBC`
--

LOCK TABLES `BBC` WRITE;
/*!40000 ALTER TABLE `BBC` DISABLE KEYS */;
INSERT INTO `BBC` VALUES (212957,'2013-03-10','news 2013-03-10','20130310BBC.mp3',''),(212898,'2013-03-09','news 2013-03-09','20130309BBC.mp3',''),(212785,'2013-03-08','news 2013-03-08','20130308BBC.mp3',''),(212697,'2013-03-07','news 2013-03-07 åŠ æ–‡æœ¬','20130307BBC.mp3','20130307BBC.txt'),(212587,'2013-03-06','news 2013-03-06 åŠ æ–‡æœ¬','20130306BBC.mp3','20130306BBC.txt'),(212482,'2013-03-05','œ¨çº¿æ”¶å¬ä¸‹è½½:è‹±å›½å¥³çŽ‹è‚ èƒƒç‚Žç»æ²»ç–—åŽå‡ºé™¢','20130305BBC.mp3','20130305BBC.txt');
/*!40000 ALTER TABLE `BBC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BBCinfo`
--

DROP TABLE IF EXISTS `BBCinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BBCinfo` (
  `maxId` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BBCinfo`
--

LOCK TABLES `BBCinfo` WRITE;
/*!40000 ALTER TABLE `BBCinfo` DISABLE KEYS */;
INSERT INTO `BBCinfo` VALUES (190887);
/*!40000 ALTER TABLE `BBCinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-03-11 13:49:23
