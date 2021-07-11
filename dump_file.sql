-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: LifechoicesDB
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id_number` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `cellnumber` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `role` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('0002035200084','Abdul-Malik','Mohamed',764971338,'abdulmalikmohamed360@gmail.com','Student','password01'),('0203131075087','Aaliyah','Jardien',679288043,'aaliyahjar13@gmail.com','Student','password01'),('9512285835083','Abdullah','Isaacs',734425442,'Abdullah.isaacs@gmail.com','Student','password01'),('9609095470083','Uthmaan','Breda',794637741,'uthmaanbreda@gmail.com','Student','password01'),('9610055082082','Justin','Calvert',679150663,'calvertjustin1996@gmail.com','Student','password01'),('9650055083083','Jason','Calvert',618975649,'jasoncee@gmail.com','Admin','password01'),('9712225172080','Mujaid','Kariem',761884456,'mujaid.kariem22@gmail.com','Student','password01');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kin_of_next`
--

DROP TABLE IF EXISTS `kin_of_next`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kin_of_next` (
  `number` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `phone` int NOT NULL,
  `id_number` varchar(20) NOT NULL,
  PRIMARY KEY (`number`),
  KEY `id` (`id_number`),
  CONSTRAINT `kin_of_next_ibfk_1` FOREIGN KEY (`id_number`) REFERENCES `Users` (`id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kin_of_next`
--

LOCK TABLES `kin_of_next` WRITE;
/*!40000 ALTER TABLE `kin_of_next` DISABLE KEYS */;
/*!40000 ALTER TABLE `kin_of_next` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_in`
--

DROP TABLE IF EXISTS `sign_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sign_in` (
  `number` int NOT NULL AUTO_INCREMENT,
  `sign_in` varchar(20) NOT NULL,
  `sign_out` varchar(20) DEFAULT NULL,
  `sign_in_date` varchar(20) NOT NULL,
  `id_number` varchar(20) NOT NULL,
  PRIMARY KEY (`number`),
  KEY `id_number` (`id_number`),
  CONSTRAINT `sign_in_ibfk_1` FOREIGN KEY (`id_number`) REFERENCES `Users` (`id_number`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_in`
--

LOCK TABLES `sign_in` WRITE;
/*!40000 ALTER TABLE `sign_in` DISABLE KEYS */;
/*!40000 ALTER TABLE `sign_in` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:29:13
