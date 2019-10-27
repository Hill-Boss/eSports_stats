-- ************************************** User

CREATE TABLE IF NOT EXISTS User
(
 `user_id`    int NOT NULL ,
 `login_name` linestring NOT NULL ,
 `First_name` linestring NOT NULL ,
 `Last_name`  linestring NOT NULL ,
 `email`      linestring NOT NULL ,
 `discord`    linestring NULL ,

PRIMARY KEY (`user_id`)
);


-- ************************************** Staff

CREATE TABLE IF NOT EXISTS Staff
(
 `user_id`    int NOT NULL ,
 `role_id`    int NOT NULL ,
 `status`     bit NOT NULL ,
 `date_start` date NOT NULL ,
 `date_end`   date NULL ,

PRIMARY KEY (`user_id`),
FOREIGN KEY (`role_id`) REFERENCES Role(`role_id`),
FOREIGN KEY (`user_id`) REFERENCES User(`user_id`)
);


-- ************************************** Role

CREATE TABLE IF NOT EXISTS Role
(
 `role_id`   int NOT NULL ,
 `role_name` linestring NOT NULL ,

PRIMARY KEY (`role_id`)
);


-- ************************************** Player

CREATE TABLE IF NOT EXISTS Player
(
 `user_id`    int NOT NULL ,
 `year`       int NULL ,
 `gpa`        float NULL ,
 `status`     linestring NOT NULL ,
 `date_start` date NOT NULL ,
 `date_end`   date NULL ,

PRIMARY KEY (`user_id`),
FOREIGN KEY (`user_id`) REFERENCES User(`user_id`)
);


-- ************************************** Game

CREATE TABLE IF NOT EXISTS Game
(
 `game_id`  int NOT NULL ,
 `name`     linestring NOT NULL ,
 `status`   linestring NOT NULL ,
 `platform` linestring NOT NULL ,
 `launcher` linestring NOT NULL ,

PRIMARY KEY (`game_id`)
);


-- ************************************** Team_Rank

CREATE TABLE IF NOT EXISTS Team_Rank
(
 `rank_id` int NOT NULL ,
 `name`    linestring NOT NULL ,

PRIMARY KEY (`rank_id`)
);


-- ************************************** Team

CREATE TABLE IF NOT EXISTS Team
(
 `team_id`    int NOT NULL ,
 `game_id`    int NOT NULL ,
 `rank_id`    int NOT NULL ,
 `team_name`  linestring NOT NULL ,
 `status`     linestring NOT NULL ,
 `date_start` date NOT NULL ,
 `date_end`   date NULL ,

PRIMARY KEY (`team_id`),
FOREIGN KEY (`rank_id`) REFERENCES Team_Rank (`rank_id`),
FOREIGN KEY (`game_id`) REFERENCES Game (`game_id`)
);


-- ************************************** user_team

CREATE TABLE IF NOT EXISTS user_team
(
 `team_id`    int NOT NULL ,
 `user_id`    int NOT NULL ,
 `date_start` date NOT NULL ,
 `date_end`   date NULL ,
 `team_cap`   bit NOT NULL ,

PRIMARY KEY (`team_id`, `user_id`),
FOREIGN KEY (`user_id`) REFERENCES Player (`user_id`),
FOREIGN KEY (`team_id`) REFERENCES Team (`team_id`)
);


-- ************************************** Stats

CREATE TABLE IF NOT EXISTS Stats
(
 `stat_id`      int NOT NULL ,
 `date_updated` date NOT NULL ,
 `STATS`       json NOT NULL ,

PRIMARY KEY (`stat_id`)
);


-- ************************************** user_game

CREATE TABLE user_game
(
 `user_id`  int NOT NULL ,
 `game_id`  int NOT NULL ,
 `stat_id`  int NOT NULL ,
 `username` linestring NOT NULL ,

PRIMARY KEY (`user_id`, `game_id`),
FOREIGN KEY (`user_id`) REFERENCES Player (`user_id`),
FOREIGN KEY (`game_id`) REFERENCES Game (`game_id`),
FOREIGN KEY (`stat_id`) REFERENCES Stats (`stat_id`)
);
