-- Change database character set and collation

ALTER DATABASE `hbtn_0c_0`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Convert individual table to new character set and collation
ALTER TABLE `hbtn_0c_0`.`first_table`
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

