CREATE TABLE PARTY
(
    ID int PRIMARY KEY NOT NULL,
    JOB varchar(50) NOT NULL,
    ATK int NULL
);
INSERT INTO PARTY
    (ID, JOB, ATK)
VALUES
    (1, 'バトマス', 100),
    (2, 'まほつか', 200),
    (3, 'そうりょ', 10),
    (4, 'にんじゃ', 150),
    (5, 'スライム', 2);
SELECT
    ID,
    JOB,
    ATK
FROM
    PARTY;
SELECT * FROM PARTY WHERE ATK >=100;
SELECT * FROM PARTY WHERE ATK <100;
