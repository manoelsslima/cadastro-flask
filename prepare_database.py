import MySQLdb
conn = MySQLdb.connect(user='flask_user', passwd='flask_Password123', host='127.0.0.1', port=3306)

conn.cursor().execute("DROP DATABASE `cadastro`;")
conn.commit()

create_table = '''SET NAMES utf8;
    CREATE DATABASE `cadastro` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `cadastro`;
    CREATE TABLE `customer` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(255) COLLATE utf8_bin NOT NULL,
      `phone` varchar(20) COLLATE utf8_bin NOT NULL,
      `email` varchar(80) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(create_table)