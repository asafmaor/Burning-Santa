BEGIN;
CREATE TABLE `auth_permission` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(50) NOT NULL, `content_type_id` integer NOT NULL, `codename` varchar(100) NOT NULL, UNIQUE (`content_type_id`, `codename`));
CREATE TABLE `auth_group` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `name` varchar(80) NOT NULL UNIQUE);
CREATE TABLE `auth_group_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `group_id` integer NOT NULL, `permission_id` integer NOT NULL, UNIQUE (`group_id`, `permission_id`));
CREATE TABLE `auth_user` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `password` varchar(128) NOT NULL, `last_login` datetime(6) NOT NULL, `is_superuser` bool NOT NULL, `username` varchar(30) NOT NULL UNIQUE, `first_name` varchar(30) NOT NULL, `last_name` varchar(30) NOT NULL, `email` varchar(75) NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` datetime(6) NOT NULL);
CREATE TABLE `auth_user_groups` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `user_id` integer NOT NULL, `group_id` integer NOT NULL, UNIQUE (`user_id`, `group_id`));
CREATE TABLE `auth_user_user_permissions` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `user_id` integer NOT NULL, `permission_id` integer NOT NULL, UNIQUE (`user_id`, `permission_id`));
ALTER TABLE `auth_permission` ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

COMMIT;

BEGIN;
CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` longtext NOT NULL, `expire_date` datetime(6) NOT NULL);
CREATE INDEX `django_session_de54fa62` ON `django_session` (`expire_date`);

COMMIT;

BEGIN;
CREATE TABLE `santa_address` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `city` varchar(100) NOT NULL, `address` varchar(1000) NOT NULL, `zipcode` varchar(32) NULL);
CREATE TABLE `santa_giftinglog` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `creation_time` datetime(6) NOT NULL, `comment` varchar(100) NULL);
CREATE TABLE `santa_santauser` (`user_ptr_id` integer NOT NULL PRIMARY KEY, `playa_name` varchar(100) NULL, `willing_to_get` longblob NOT NULL, `santa_to_id` integer NULL);
ALTER TABLE `santa_giftinglog` ADD COLUMN `user_id` integer NOT NULL;
ALTER TABLE `santa_giftinglog` ALTER COLUMN `user_id` DROP DEFAULT;
ALTER TABLE `santa_address` ADD COLUMN `user_id` integer NOT NULL;
ALTER TABLE `santa_address` ALTER COLUMN `user_id` DROP DEFAULT;
ALTER TABLE `santa_santauser` ADD CONSTRAINT `santa_santauser_user_ptr_id_6ba11be79508dbdd_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `santa_santauser` ADD CONSTRAINT `santa_santa_to_id_de8fb24858e4134_fk_santa_santauser_user_ptr_id` FOREIGN KEY (`santa_to_id`) REFERENCES `santa_santauser` (`user_ptr_id`);
CREATE INDEX `santa_giftinglog_e8701ad4` ON `santa_giftinglog` (`user_id`);
ALTER TABLE `santa_giftinglog` ADD CONSTRAINT `santa_gi_user_id_5504b28d33fccbd1_fk_santa_santauser_user_ptr_id` FOREIGN KEY (`user_id`) REFERENCES `santa_santauser` (`user_ptr_id`);
CREATE INDEX `santa_address_e8701ad4` ON `santa_address` (`user_id`);
ALTER TABLE `santa_address` ADD CONSTRAINT `santa_add_user_id_90c3229e871827c_fk_santa_santauser_user_ptr_id` FOREIGN KEY (`user_id`) REFERENCES `santa_santauser` (`user_ptr_id`);

COMMIT;
