-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_1201
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

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
-- Table structure for table `films`
--

DROP TABLE IF EXISTS `films`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `films` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(25) NOT NULL,
  `description` text NOT NULL,
  `type_id` int(11) NOT NULL,
  `production_year` year(4) NOT NULL,
  `country` varchar(25) NOT NULL,
  `producer` varchar(25) NOT NULL,
  `scenarist` varchar(25) NOT NULL,
  `actors` varchar(25) NOT NULL,
  `time_in_m` int(11) NOT NULL,
  `poster_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `poster_id` (`poster_id`),
  KEY `type_id` (`type_id`) USING BTREE,
  CONSTRAINT `films_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `types` (`id`),
  CONSTRAINT `films_ibfk_2` FOREIGN KEY (`poster_id`) REFERENCES `posters` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `films`
--

LOCK TABLES `films` WRITE;
/*!40000 ALTER TABLE `films` DISABLE KEYS */;
INSERT INTO `films` VALUES (2,'Blade Runner','Blade Runner is a 1982 science fiction film directed by Ridley Scott, and written by Hampton Fancher and David Peoples. Starring Harrison Ford, Rutger Hauer, Sean Young, and Edward James Olmos, it is loosely based on Philip K. Dick\'s 1968 novel \"Do Androids Dream of Electric Sheep?\". The film is set in a dystopian future Los Angeles of 2019, in which synthetic humans known as replicants are bio-engineered by the powerful Tyrell Corporation to work at space colonies. When a fugitive group of advanced replicants led by Roy Batty (Hauer) escapes back to Earth, burnt-out cop Rick Deckard (Ford) reluctantly agrees to hunt them down.',1,1982,'USA, HONG KONG','Michael Deeley','Hampton Fancher','Harrison Ford',117,1),(8,'There Will Be Blood','There Will Be Blood is a 2007 American epic period drama film written and directed by Paul Thomas Anderson, loosely based on the 1927 novel Oil! by Upton Sinclair. It stars Daniel Day-Lewis as Daniel Plainview, a silver miner-turned-oilman on a ruthless quest for wealth during Southern California\'s oil boom of the late 19th and early 20th centuries. Paul Dano, Kevin J. O\'Connor, Ciarán Hinds, and Dillon Freasier also feature in the film.',2,2007,'USA','Paul Thomas Anderson','Paul Thomas Anderson','Daniel Day-Lewis',158,2),(9,'Full Metal Jacket','Full Metal Jacket is a 1987 war film directed, co-written, and produced by Stanley Kubrick and starring Matthew Modine, R. Lee Ermey, Vincent D\'Onofrio and Adam Baldwin. The screenplay by Kubrick, Michael Herr, and Gustav Hasford was based on Hasford\'s 1979 novel The Short-Timers.',3,1987,'USA, UK','Stanley Kubrick','Stanley Kubrick','Matthew Modine',116,3),(10,'La La Land','La La Land is a 2016 American romantic musical film written and directed by Damien Chazelle. It stars Ryan Gosling as a jazz pianist and Emma Stone as an aspiring actress, who meet and fall in love while pursuing their dreams in Los Angeles. John Legend, Rosemarie DeWitt, Finn Wittrock, and J. K. Simmons also star.',4,2016,'USA','Fred Berger','Damien Chazelle','Ryan Gosling',128,4),(11,'Blade Runner 2049','Blade Runner 2049 is a 2017 American neo-noir science fiction film directed by Denis Villeneuve and written by Hampton Fancher and Michael Green. A sequel to the 1982 film Blade Runner, the film stars Ryan Gosling and Harrison Ford, with Ana de Armas, Sylvia Hoeks, Robin Wright, Mackenzie Davis, Carla Juri, Lennie James, Dave Bautista, and Jared Leto in supporting roles. Ford and Edward James Olmos reprise their roles from the original. Gosling plays K, a Nexus-9 replicant \"blade runner\" who uncovers a secret that threatens to destabilize society and the course of civilization.',1,2017,'USA','Andrew A. Kosove','Hampton Fancher','Ryan Gosling',163,5),(12,'1917','1917 is a 2019 British war film directed and produced by Sam Mendes, who co-wrote the film with Krysty Wilson-Cairns. Partially inspired by stories told to Mendes by his paternal grandfather Alfred about his service during World War I, the film takes place after the German retreat to the Hindenburg Line during Operation Alberich, and follows two British soldiers, Will Schofield (George MacKay) and Tom Blake (Dean-Charles Chapman), in their mission to deliver an important message to call off a doomed offensive attack. Mark Strong, Andrew Scott, Richard Madden, Claire Duburcq, Colin Firth, and Benedict Cumberbatch also star in supporting roles.',3,2019,'USA, UK','Sam Mendes','Sam Mendes','George MacKay',119,6),(15,'The Fool','The Fool (Russian: Дурак, romanized: Durak) is a 2014 Russian drama film written and directed by Yuri Bykov. It had its international premiere at the 2014 Locarno International Film Festival, where it won the prize for the best actor.',2,2014,'RUSSIA','Alexey Uchitel','Yuri Bykov','Artyom Bystrov',116,7),(16,'Free to Play','Free to Play is a 2014 documentary film by American video game company Valve. The film takes a critical look at the lives of Benedict \"hyhy\" Lim, Danil \"Dendi\" Ishutin and Clinton \"Fear\" Loomis, three professional Defense of the Ancients (DotA) players who participated in the first International, the most lucrative esports tournament at the time. The central focus of the film is how their commitment to DotA had affected their lives and how this debut tournament for the sequel, Dota 2, would bring more meaning to their struggles.',5,2014,'USA','Benedict Lim','Benedict Lim','Danil Ishutin',75,8),(17,'Tenet','Tenet is a 2020 science fiction action-thriller film written and directed by Christopher Nolan, who produced it with Emma Thomas. A co-production between the United Kingdom and United States, it stars John David Washington, Robert Pattinson, Elizabeth Debicki, Dimple Kapadia, Michael Caine, and Kenneth Branagh. The film follows a secret agent who learns to manipulate the flow of time to prevent an attack from the future that threatens to annihilate the present world.',6,2020,'USA, UK','Christopher Nolan','Christopher Nolan','John David Washington',150,9);
/*!40000 ALTER TABLE `films` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posters`
--

DROP TABLE IF EXISTS `posters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(25) NOT NULL,
  `MIME` varchar(25) NOT NULL,
  `MD5_hash` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posters`
--

LOCK TABLES `posters` WRITE;
/*!40000 ALTER TABLE `posters` DISABLE KEYS */;
INSERT INTO `posters` VALUES (1,'poster1','1','1'),(2,'poster2','2','2'),(3,'poster3','3','3'),(4,'poster4','4','4'),(5,'poster5','5','5'),(6,'poster6','6','6'),(7,'poster7','7','7'),(8,'poster8','8','8'),(9,'poster9','9','9'),(10,'poster10','10','10');
/*!40000 ALTER TABLE `posters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `film_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `user_text` text NOT NULL,
  `add_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `film_id` (`film_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`film_id`) REFERENCES `films` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Administrator','All actions'),(2,'Moderator','Redactions films / reviews'),(3,'User','Adds reviews');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `types`
--

DROP TABLE IF EXISTS `types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `types`
--

LOCK TABLES `types` WRITE;
/*!40000 ALTER TABLE `types` DISABLE KEYS */;
INSERT INTO `types` VALUES (1,'Sci-Fi'),(2,'Drama'),(3,'War movie'),(4,'Romantic musical'),(5,'Documentary film'),(6,'Action');
/*!40000 ALTER TABLE `types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `middle_name` varchar(25) DEFAULT NULL,
  `password_hash` varchar(256) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','Efremov','Nikita','Alekseevich','65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5',1),(2,'moderator','Fedorov','Aleksandr','Igorevich','8f4a3cfd9be04f11663dae250664433668a14a2ae9752a05fe910aee22af6000',2),(3,'user','Baykalov','Andrey','Evgenyevich','04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb',3);
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

-- Dump completed on 2021-01-26 15:22:53
