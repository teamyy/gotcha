/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table article_images
# ------------------------------------------------------------

DROP TABLE IF EXISTS `article_images`;

CREATE TABLE `article_images` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` bigint(20) unsigned DEFAULT NULL,
  `image_url` varchar(240) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `article_id` (`article_id`),
  KEY `image_url` (`image_url`),
  CONSTRAINT `article_images_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DELIMITER ;;
/*!50003 SET SESSION SQL_MODE="" */;;
  /*!50003 CREATE */ /*!50017 DEFINER=`gotcha-admin`@`localhost` */ /*!50003 TRIGGER `insert_article_images_history` AFTER INSERT ON `article_images` FOR EACH ROW BEGIN
  INSERT INTO article_images_history (article_id, image_url)
  VALUES (NEW.article_id, NEW.image_url);
END */;;
/*!50003 SET SESSION SQL_MODE="" */;;
  /*!50003 CREATE */ /*!50017 DEFINER=`gotcha-admin`@`localhost` */ /*!50003 TRIGGER `update_article_images_history` AFTER UPDATE ON `article_images` FOR EACH ROW BEGIN
  INSERT INTO article_images_history (article_id, image_url)
  VALUES (NEW.article_id, NEW.image_url);
END */;;
DELIMITER ;
/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;


# Dump of table article_images_history
# ------------------------------------------------------------

DROP TABLE IF EXISTS `article_images_history`;

CREATE TABLE `article_images_history` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `article_id` bigint(20) DEFAULT NULL,
  `image_url` varchar(240) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table articles
# ------------------------------------------------------------

DROP TABLE IF EXISTS `articles`;

CREATE TABLE `articles` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `content` longtext NOT NULL,
  `writer` varchar(64) NOT NULL DEFAULT '',
  `url` varchar(240) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `category` varchar(32) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `writed_at` datetime NOT NULL,
  `modified_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`),
  KEY `category` (`category`),
  KEY `writed_at` (`writed_at`),
  KEY `modified_at` (`modified_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


DELIMITER ;;
/*!50003 SET SESSION SQL_MODE="" */;;
  /*!50003 CREATE */ /*!50017 DEFINER=`gotcha-admin`@`localhost` */ /*!50003 TRIGGER `insert_articles_history` AFTER INSERT ON `articles` FOR EACH ROW BEGIN
  INSERT INTO articles_history (title, content, writer, url, category, writed_at)
  VALUES (NEW.title, NEW.content, NEW.writer, NEW.url, NEW.category, NEW.writed_at);
END */;;
/*!50003 SET SESSION SQL_MODE="" */;;
  /*!50003 CREATE */ /*!50017 DEFINER=`gotcha-admin`@`localhost` */ /*!50003 TRIGGER `update_articles_history` AFTER UPDATE ON `articles` FOR EACH ROW BEGIN
  INSERT INTO articles_history (title, content, writer, url, category, writed_at)
  VALUES (NEW.title, NEW.content, NEW.writer, NEW.url, NEW.category, NEW.writed_at);
END */;;
DELIMITER ;
/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;


# Dump of table articles_history
# ------------------------------------------------------------

DROP TABLE IF EXISTS `articles_history`;

CREATE TABLE `articles_history` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` text NOT NULL,
  `content` longtext NOT NULL,
  `writer` varchar(64) NOT NULL DEFAULT '',
  `url` varchar(240) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `category` varchar(32) CHARACTER SET utf8 NOT NULL DEFAULT '',
  `writed_at` datetime NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
