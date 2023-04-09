-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: obj_det
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `img_label` varchar(200) DEFAULT NULL,
  `obj_detected` varchar(200) DEFAULT NULL,
  `probability` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Turdus_merula641.jpg','Turdus_merula','96.36%'),(2,'Periparus_ater704.jpg','Periparus_ater','51.13%'),(3,'Pica_pica679.jpg','Pica_pica','90.38%'),(4,'ErithacusRubecula1047.jpg','Pica_pica','74.21%'),(5,'Pica_pica662.jpg','Pica_pica','99.02%'),(6,'Pica_pica812.jpg','Pica_pica','98.09%'),(7,'ErithacusRubecula1008.jpg','Turdus_merula','98.34%'),(8,'IMG_3864_11zon.jpg','Pica_pica','96.74%'),(9,'Turdus_merula401.jpg','Turdus_merula','92.86%'),(10,'Pica_pica717.jpg','Pica_pica','95.53%'),(11,'Turdus_merula401.jpg','Turdus_merula','92.86%'),(12,'Turdus_merula401.jpg','Turdus_merula','92.86%'),(13,'Turdus_merula_-New_Zealand_-family-8.jpg','Turdus_merula','98.45%'),(14,'Turdus_merula641.jpg','Turdus_merula','96.36%'),(15,'Pica_pica812.jpg','Pica_pica','98.09%'),(16,'Turdus_merula913.jpg','Turdus_merula','98.08%'),(17,'Turdus_merula202.jpg','Turdus_merula','98.01%'),(18,'Turdus_merula202.jpg','Turdus_merula','98.01%'),(19,'Pica_pica717.jpg','Pica_pica','95.53%'),(20,'Pica_pica341.jpg','Pica_pica','88.94%'),(21,'Pica_pica688.jpg','Pica_pica','96.83%'),(22,'Pica_pica812.jpg','Pica_pica','98.09%'),(23,'Pica_pica674.jpg','Pica_pica','96.75%'),(24,'Pica_pica679.jpg','Pica_pica','90.38%'),(25,'Pica_pica662.jpg','Pica_pica','99.02%'),(26,'Pica_pica662.jpg','Pica_pica','99.02%'),(27,'Pica_pica679.jpg','Pica_pica','90.38%'),(28,'ErithacusRubecula1008.jpg','Turdus_merula','98.34%'),(29,'ErithacusRubecula0998.jpg','Turdus_merula','91.83%'),(30,'ErithacusRubecula1001.jpg','Turdus_merula','78.31%'),(31,'Turdus_merula992.jpg','Turdus_merula','88.74%'),(32,'Turdus_merula1000.jpg','Turdus_merula','98.13%'),(33,'Pica_pica751.jpg','Pica_pica','95.65%'),(34,'Periparus_ater727.jpg','Periparus_ater','99.26%'),(35,'ErithacusRubecula1003.jpg','Turdus_merula','96.74%'),(36,'ErithacusRubecula0942.jpg','Turdus_merula','85.72%'),(37,'ErithacusRubecula0963.jpg','Turdus_merula','94.7%'),(38,'ErithacusRubecula0904.jpg','Turdus_merula','98.86%'),(39,'ErithacusRubecula0817.jpg','Turdus_merula','89.27%'),(40,'ErithacusRubecula1001.jpg','Turdus_merula','78.31%'),(41,'ErithacusRubecula0997.jpg','Erithacus_Rubecula','77.88%'),(42,'ErithacusRubecula0997.jpg','Erithacus_Rubecula','77.88%'),(43,'ErithacusRubecula0991.jpg','Erithacus_Rubecula','1.71%'),(44,'ErithacusRubecula0998.jpg','Turdus_merula','91.83%'),(45,'Periparus_ater728.jpg','Periparus_ater','99.74%'),(46,'Periparus_ater722.jpg','Periparus_ater','99.5%'),(47,'Periparus_ater678.jpg','Periparus_ater','88.51%'),(48,'Periparus_ater678.jpg','Periparus_ater','88.51%'),(49,'Periparus_ater727.jpg','Periparus_ater','99.26%'),(50,'Periparus_ater727.jpg','Periparus_ater','99.26%'),(51,'Turdus_merula954.jpg','Turdus_merula','98.71%'),(52,'IMG_3864_11zon.jpg','Pica_pica','96.73%'),(53,'ErithacusRubecula0200.jpg','Turdus_merula','95.57%'),(54,'Turdus_merula989.jpg','Turdus_merula','97.62%'),(55,'Periparus_ater704.jpg','Periparus_ater','51.13%'),(56,'ErithacusRubecula0722.jpg','Turdus_merula','92.81%'),(57,'ezgif.com-gif-maker.jpg','Turdus_merula','96.38%'),(58,'ErithacusRubecula1118.jpg','Turdus_merula','74.8%');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-08 18:01:45
