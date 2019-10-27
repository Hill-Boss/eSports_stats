BEGIN TRANSACTION;
DROP TABLE IF EXISTS "user_game";
CREATE TABLE IF NOT EXISTS "user_game" (
	"user_id"	int NOT NULL,
	"game_id"	int NOT NULL,
	"stat_id"	int NOT NULL,
	"username"	linestring NOT NULL,
	FOREIGN KEY("stat_id") REFERENCES "Stats"("stat_id"),
	FOREIGN KEY("game_id") REFERENCES "Game"("game_id"),
	PRIMARY KEY("user_id","game_id"),
	FOREIGN KEY("user_id") REFERENCES "Player"("user_id")
);
DROP TABLE IF EXISTS "Stats";
CREATE TABLE IF NOT EXISTS "Stats" (
	"stat_id"	int NOT NULL,
	"STATS"	json NOT NULL,
	"date_updated"	date NOT NULL,
	PRIMARY KEY("stat_id")
);
DROP TABLE IF EXISTS "user_team";
CREATE TABLE IF NOT EXISTS "user_team" (
	"team_id"	int NOT NULL,
	"user_id"	int NOT NULL,
	"date_start"	date NOT NULL,
	"date_end"	date,
	"team_cap"	bit NOT NULL,
	FOREIGN KEY("team_id") REFERENCES "Team"("team_id"),
	PRIMARY KEY("team_id","user_id"),
	FOREIGN KEY("user_id") REFERENCES "Player"("user_id")
);
DROP TABLE IF EXISTS "Team";
CREATE TABLE IF NOT EXISTS "Team" (
	"team_id"	int NOT NULL,
	"game_id"	int NOT NULL,
	"rank_id"	int NOT NULL,
	"status"	linestring NOT NULL,
	"team_name"	linestring NOT NULL,
	"date_start"	date NOT NULL,
	"date_end"	date,
	FOREIGN KEY("game_id") REFERENCES "Game"("game_id"),
	PRIMARY KEY("team_id"),
	FOREIGN KEY("rank_id") REFERENCES "Team_Rank"("rank_id")
);
DROP TABLE IF EXISTS "Team_Rank";
CREATE TABLE IF NOT EXISTS "Team_Rank" (
	"rank_id"	int NOT NULL,
	"name"	linestring NOT NULL,
	PRIMARY KEY("rank_id")
);
DROP TABLE IF EXISTS "Game";
CREATE TABLE IF NOT EXISTS "Game" (
	"game_id"	int NOT NULL,
	"name"	linestring NOT NULL,
	"status"	linestring NOT NULL,
	"platform"	linestring NOT NULL,
	"launcher"	linestring NOT NULL,
	PRIMARY KEY("game_id")
);
DROP TABLE IF EXISTS "Status";
CREATE TABLE IF NOT EXISTS "Status" (
	"status_id" int NOT NULL,
	"status" linestring NOT NULL,
	"date_start" date,
	"date_end" date,
	PRIMARY KEY("status_id")
);
DROP TABLE IF EXISTS "Player";
CREATE TABLE IF NOT EXISTS "Player" (
	"user_id"	int NOT NULL,
	"status_id" int NOT NULL,
	"790" int NOT NULL,
	"gpa"	smallint NOT NULL, -- I don't like floats
	"year"	linestring NOT NULL,
	"major" linestring NOT NULL,
	"status"	linestring NOT NULL,
	"date_start"	date NOT NULL,
	"date_end"	date,
	FOREIGN KEY("status_id") REFERENCES "Status"("status_id"),
	FOREIGN KEY("user_id") REFERENCES "User"("user_id"),
	PRIMARY KEY("user_id")
);
DROP TABLE IF EXISTS "Role";
CREATE TABLE IF NOT EXISTS "Role" (
	"role_id"	int NOT NULL,
	"role_name"	linestring NOT NULL,
	PRIMARY KEY("role_id")
);
DROP TABLE IF EXISTS "Staff";
CREATE TABLE IF NOT EXISTS "Staff" (
	"user_id"	int NOT NULL,
	"role_id"	int NOT NULL,
	"status"	bit NOT NULL,
	"date_start"	date NOT NULL,
	"date_end"	date,
	FOREIGN KEY("user_id") REFERENCES "User"("user_id"),
	PRIMARY KEY("user_id"),
	FOREIGN KEY("role_id") REFERENCES "Role"("role_id")
);
DROP TABLE IF EXISTS "User";
CREATE TABLE IF NOT EXISTS "User" (
	"user_id"	int NOT NULL,
	"login_name"	linestring NOT NULL,
	"First_name"	linestring NOT NULL,
	"Last_name"	linestring NOT NULL,
	"email"	linestring NOT NULL,
	"discord"	linestring,
	PRIMARY KEY("user_id")
);
COMMIT;
