/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80037
 Source Host           : localhost:3306
 Source Schema         : 群聊系统

 Target Server Type    : MySQL
 Target Server Version : 80037
 File Encoding         : 65001

 Date: 03/06/2024 23:40:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for 全部账户
-- ----------------------------
DROP TABLE IF EXISTS `全部账户`;
CREATE TABLE `全部账户`  (
  `账号` int NOT NULL,
  `昵称` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `密码` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `性别` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`账号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 全部账户
-- ----------------------------
INSERT INTO `全部账户` VALUES (111111, '用户11', '123123', '男');
INSERT INTO `全部账户` VALUES (123456, '用户1', '123123', '男');
INSERT INTO `全部账户` VALUES (123987, '用户10', '123123', '女');
INSERT INTO `全部账户` VALUES (234567, '用户2', '321321', '女');
INSERT INTO `全部账户` VALUES (345678, '用户3', '123123', '男');
INSERT INTO `全部账户` VALUES (456789, '用户4', '123123', '女');
INSERT INTO `全部账户` VALUES (567890, '用户5', '321321', '男');
INSERT INTO `全部账户` VALUES (678901, '用户6', '123123', '女');
INSERT INTO `全部账户` VALUES (789012, '用户7', '1123123', '男');
INSERT INTO `全部账户` VALUES (890123, '用户8', '123123', '女');
INSERT INTO `全部账户` VALUES (901234, '用户9', '123123', '男');
INSERT INTO `全部账户` VALUES (1122112, '管理员1', '321321', '女');
INSERT INTO `全部账户` VALUES (2211221, '管理员2', '321321', '男');
INSERT INTO `全部账户` VALUES (12345678, '用户11', '123123', '男');

-- ----------------------------
-- Table structure for 管理员
-- ----------------------------
DROP TABLE IF EXISTS `管理员`;
CREATE TABLE `管理员`  (
  `入群时间` datetime(0) NULL DEFAULT NULL,
  `管理员` tinyint(1) NULL DEFAULT NULL,
  `账号` int NOT NULL,
  `昵称` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `密码` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `性别` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`账号`) USING BTREE,
  CONSTRAINT `FK_包含` FOREIGN KEY (`账号`) REFERENCES `群成员` (`账号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 管理员
-- ----------------------------
INSERT INTO `管理员` VALUES ('2024-05-24 10:15:00', 1, 1122112, '管理员1', '321321', '女');
INSERT INTO `管理员` VALUES ('2024-05-24 11:00:00', 1, 2211221, '管理员2', '321321', '男');

-- ----------------------------
-- Table structure for 群成员
-- ----------------------------
DROP TABLE IF EXISTS `群成员`;
CREATE TABLE `群成员`  (
  `账号` int NOT NULL,
  `昵称` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `密码` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `性别` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `入群时间` datetime(0) NULL DEFAULT NULL,
  `管理员` tinyint(1) NULL DEFAULT NULL,
  PRIMARY KEY (`账号`) USING BTREE,
  CONSTRAINT `群成员_ibfk_1` FOREIGN KEY (`账号`) REFERENCES `全部账户` (`账号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 群成员
-- ----------------------------
INSERT INTO `群成员` VALUES (111111, '用户11', '123123', '男', '2024-06-02 23:13:33', 0);
INSERT INTO `群成员` VALUES (123456, '用户1', '123123', '男', '2024-06-03 23:27:18', 0);
INSERT INTO `群成员` VALUES (234567, '用户2', '321321', '女', '2024-05-25 10:15:00', 0);
INSERT INTO `群成员` VALUES (345678, '用户3', '123123', '男', '2024-05-26 10:30:00', 0);
INSERT INTO `群成员` VALUES (456789, '用户4', '123123', '女', '2024-05-26 10:45:00', 0);
INSERT INTO `群成员` VALUES (567890, '用户5', '321321', '男', '2024-06-02 23:14:09', 0);
INSERT INTO `群成员` VALUES (678901, '用户6', '123123', '女', '2024-05-26 11:15:00', 0);
INSERT INTO `群成员` VALUES (789012, '用户7', '1123123', '男', '2024-05-26 11:30:00', 0);
INSERT INTO `群成员` VALUES (890123, '用户8', '123123', '女', '2024-05-26 11:45:00', 0);
INSERT INTO `群成员` VALUES (901234, '用户9', '123123', '男', '2024-05-26 12:00:00', 0);
INSERT INTO `群成员` VALUES (1122112, '管理员1', '321321', '女', '2024-05-24 10:15:00', 1);
INSERT INTO `群成员` VALUES (2211221, '管理员2', '321321', '男', '2024-05-24 11:00:00', 1);

-- ----------------------------
-- Table structure for 聊天记录
-- ----------------------------
DROP TABLE IF EXISTS `聊天记录`;
CREATE TABLE `聊天记录`  (
  `记录编号` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `账号` int NULL DEFAULT NULL,
  `发送时间` datetime(0) NULL DEFAULT NULL,
  `昵称` char(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `内容` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  PRIMARY KEY (`记录编号`) USING BTREE,
  INDEX `FK_查询`(`账号`) USING BTREE,
  CONSTRAINT `FK_查询` FOREIGN KEY (`账号`) REFERENCES `群成员` (`账号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of 聊天记录
-- ----------------------------
INSERT INTO `聊天记录` VALUES ('REC012', 234567, '2024-05-27 12:15:00', '用户2', '好的，见面地点在公园入口处。');
INSERT INTO `聊天记录` VALUES ('REC013', 345678, '2024-05-27 12:30:00', '用户3', '明白了。');
INSERT INTO `聊天记录` VALUES ('REC014', 456789, '2024-05-27 12:45:00', '用户4', '我会提前到达。');
INSERT INTO `聊天记录` VALUES ('REC016', 678901, '2024-05-27 13:15:00', '用户6', '那我们就定下来了。');
INSERT INTO `聊天记录` VALUES ('REC017', 789012, '2024-05-27 13:30:00', '用户7', '我期待这次聚会。');
INSERT INTO `聊天记录` VALUES ('REC018', 890123, '2024-05-27 13:45:00', '用户8', '我也是。');
INSERT INTO `聊天记录` VALUES ('REC019', 901234, '2024-05-27 14:00:00', '用户9', '同样期待。');
INSERT INTO `聊天记录` VALUES ('REC02', 111111, '2024-06-03 16:06:06', '用户11', '你们在哪');
INSERT INTO `聊天记录` VALUES ('REC020', 1122112, '2024-06-03 16:07:59', '管理员1', '我还在路上');
INSERT INTO `聊天记录` VALUES ('REC021', 111111, '2024-06-03 18:11:01', '用户11', '我也在路上');
INSERT INTO `聊天记录` VALUES ('REC022', 456789, '2024-06-03 18:19:24', '用户4', '看见你了');
INSERT INTO `聊天记录` VALUES ('REC023', 456789, '2024-06-03 18:19:46', '用户4', '用户5');
INSERT INTO `聊天记录` VALUES ('REC024', 456789, '2024-06-03 18:19:57', '用户4', '我在你对面');
INSERT INTO `聊天记录` VALUES ('REC025', 567890, '2024-06-03 18:21:06', '用户5', '拿了好多东西');

-- ----------------------------
-- View structure for chat_record
-- ----------------------------
DROP VIEW IF EXISTS `chat_record`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `chat_record` AS select `聊天记录`.`账号` AS `账号`,`聊天记录`.`发送时间` AS `发送时间`,`聊天记录`.`昵称` AS `昵称`,`聊天记录`.`内容` AS `内容`,`群成员`.`管理员` AS `管理员` from (`聊天记录` join `群成员` on((`聊天记录`.`账号` = `群成员`.`账号`)));

-- ----------------------------
-- Procedure structure for UpdateAccount
-- ----------------------------
DROP PROCEDURE IF EXISTS `UpdateAccount`;
delimiter ;;
CREATE PROCEDURE `UpdateAccount`(IN old_account_id int,
    IN new_account_id int)
BEGIN
    -- 声明变量来存储查询结果
    DECLARE exists_count INT;

    -- 检查新账号是否已存在
    SELECT COUNT(*) INTO exists_count
    FROM 全部账户
    WHERE 账号 = new_account_id;

    -- 如果新账号已存在，则抛出错误
    IF exists_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '该账号已存在';
    END IF;

    -- 如果新账号不存在，则更新账号
    set foreign_key_checks = 0;
    UPDATE 全部账户
    SET 账号 = new_account_id
    WHERE 账号 = old_account_id;

    UPDATE 聊天记录
    SET 账号 = new_account_id
    WHERE 账号 = old_account_id;

    UPDATE 群成员
    SET 账号 = new_account_id
    WHERE 账号 = old_account_id;
    set foreign_key_checks = 1;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table 群成员
-- ----------------------------
DROP TRIGGER IF EXISTS `before_insert_check`;
delimiter ;;
CREATE TRIGGER `before_insert_check` BEFORE INSERT ON `群成员` FOR EACH ROW BEGIN
    IF EXISTS (SELECT 1 FROM 群成员 WHERE 账号 = NEW.账号) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '不能重复添加该用户';
    END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
