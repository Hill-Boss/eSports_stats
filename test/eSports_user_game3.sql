BEGIN TRANSACTION;
DROP TABLE IF EXISTS "eSports_user_game";
CREATE TABLE IF NOT EXISTS "eSports_user_game" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username"	varchar(60) NOT NULL,
	"game_id_id"	integer NOT NULL,
	"stat_id_id"	integer UNIQUE,
	"user_id_id"	integer,
	FOREIGN KEY("stat_id_id") REFERENCES "eSports_stats"("stat_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id_id") REFERENCES "eSports_player"("user_id_id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("game_id_id") REFERENCES "eSports_game"("game_id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "eSports_user_game" VALUES (1,'MrBlueSky-729',1,1,9);
INSERT INTO "eSports_user_game" VALUES (2,'MrBlueSky-729',2,2,9);
INSERT INTO "eSports_user_game" VALUES (3,'MrBlueSky-729',3,NULL,NULL);
INSERT INTO "eSports_user_game" VALUES (4,'Ulfrrr',4,NULL,NULL);
DROP INDEX IF EXISTS "eSports_user_game_user_id_id_cdcf9de8";
CREATE INDEX IF NOT EXISTS "eSports_user_game_user_id_id_cdcf9de8" ON "eSports_user_game" (
	"user_id_id"
);
DROP INDEX IF EXISTS "eSports_user_game_game_id_id_1ab1b731";
CREATE INDEX IF NOT EXISTS "eSports_user_game_game_id_id_1ab1b731" ON "eSports_user_game" (
	"game_id_id"
);
DROP INDEX IF EXISTS "eSports_user_game_user_id_id_game_id_id_4191f10d_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "eSports_user_game_user_id_id_game_id_id_4191f10d_uniq" ON "eSports_user_game" (
	"user_id_id",
	"game_id_id"
);
COMMIT;
