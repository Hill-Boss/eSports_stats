BEGIN TRANSACTION;
INSERT OR REPLACE INTO "User" VALUES (1,'sadfdfasj','fafas','dadas','dsafdsa@dasd.com','dasad#1513');
INSERT OR REPLACE INTO "Role" VALUES (1,'intern');
INSERT OR REPLACE INTO "Staff" VALUES (1,1,1,'10.25.2019',NULL);
INSERT OR REPLACE INTO "Status" VALUES (1,'Active',NULL,NULL);
INSERT OR REPLACE INTO "Player" VALUES (1,1,790790,400,'Junior','CSCI','NULL','10.25.2019',NULL);
INSERT OR REPLACE INTO "Game" VALUES (1,'Apex','Active','pc','origin');
INSERT OR REPLACE INTO "Game" VALUES (2,'Rocket League','Active','pc','steam');
INSERT OR REPLACE INTO "Game" VALUES (3,'Overwatch','Active','pc','battlenet');
INSERT OR REPLACE INTO "Game" VALUES (4,'League of Legends','Active','pc','riot');
INSERT OR REPLACE INTO "Team_Rank" VALUES (1,'Varsity');
INSERT OR REPLACE INTO "Team_Rank" VALUES (2,'Junior Varsity');
INSERT OR REPLACE INTO "Team" VALUES (1,1,1,'fdsa','dsaf','10.25.2019',NULL);
INSERT OR REPLACE INTO "user_team" VALUES (1,1,'10.25.2019',NULL,1);
INSERT OR REPLACE INTO "Stats" VALUES (1,'NULL','10.25.2019');
INSERT OR REPLACE INTO "user_game" VALUES (1,1,1,'Mrsad');

COMMIT;
