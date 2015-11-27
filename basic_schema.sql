BEGIN;
CREATE TABLE `santa_giftinglog` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `creation_time` datetime(6) NOT NULL);
CREATE TABLE `santa_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `first_name` varchar(100) NOT NULL, `last_name` varchar(100) NOT NULL, `playa_name` varchar(100) NOT NULL, `email` varchar(100) NOT NULL, `address` varchar(1000) NOT NULL, `zipcode` varchar(32) NOT NULL, `santa_to_id` integer NOT NULL);
ALTER TABLE `santa_giftinglog` ADD COLUMN `user_id` integer NOT NULL;
ALTER TABLE `santa_giftinglog` ALTER COLUMN `user_id` DROP DEFAULT;
ALTER TABLE `santa_user` ADD CONSTRAINT `santa_user_santa_to_id_279170e87c7bd0a2_fk_santa_user_id` FOREIGN KEY (`santa_to_id`) REFERENCES `santa_user` (`id`);
CREATE INDEX `santa_giftinglog_e8701ad4` ON `santa_giftinglog` (`user_id`);
ALTER TABLE `santa_giftinglog` ADD CONSTRAINT `santa_giftinglog_user_id_5504b28d33fccbd1_fk_santa_user_id` FOREIGN KEY (`user_id`) REFERENCES `santa_user` (`id`);

COMMIT;