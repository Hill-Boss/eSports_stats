BEGIN TRANSACTION;

INSERT OR REPLACE INTO "eSports_role" VALUES (1,'intern');


INSERT OR REPLACE INTO "eSports_status" VALUES (1,'Active','04/27/1999',NULL);

INSERT OR REPLACE INTO "eSports_staff" VALUES (1,1,1,'10.25.2019',0);

INSERT OR REPLACE INTO "eSports_player" VALUES (1,1,790790,400,'Junior','CSCI','10.25.2019',0);

INSERT OR REPLACE INTO "eSports_game" VALUES (1,'Apex',0,'pc','origin');
INSERT OR REPLACE INTO "eSports_game" VALUES (2,'Rocket League',0,'pc','steam');
INSERT OR REPLACE INTO "eSports_game" VALUES (3,'Overwatch',0,'pc','battlenet');
INSERT OR REPLACE INTO "eSports_game" VALUES (4,'League of Legends',0,'pc','riot');

INSERT OR REPLACE INTO "eSports_team_rank" VALUES (1,'Varsity');
INSERT OR REPLACE INTO "eSports_team_rank" VALUES (2,'Junior Varsity');

INSERT OR REPLACE INTO "eSports_team" VALUES (1,1,1,'fdsa','dsaf','10.25.2019',0);

INSERT OR REPLACE INTO "eSports_user_team" VALUES (1,1,1,'10.25.2019',0,0);

INSERT OR REPLACE INTO "eSports_stats" VALUES (1,'NULL','10.25.2019');

INSERT OR REPLACE INTO "eSports_user_game" VALUES (1,1,1,'Mrsad', 0);
COMMIT;
