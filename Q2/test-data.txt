CREATE TABLE clickstream(
	userId VARCHAR(255) NOT NULL,
	time DATETIME NOT NULL,
	action ENUM('FIRST_INSTALL','LIKE_ARTICLE') NOT NULL,
	objectId BIGINT NOT NULL
);

INSERT INTO clickstream
(userId, time, action, objectId)
VALUES
('F57DA5D1', '2021-07-29 09:30:46', 2, 23461);

INSERT INTO clickstream
(userId, time, action, objectId)
VALUES
('F57DA5D2', '2021-07-29 09:27:46', 2, 23460);

INSERT INTO clickstream
(userId, time, action, objectId)
VALUES
('F57DA51111', '2021-07-29 09:27:46', 2, 23460);

INSERT INTO clickstream
(userId, time, action, objectId)
VALUES
('F57DA5D4', '2021-07-29 09:27:46', 2, 23460);

INSERT INTO clickstream
(userId, time, action, objectId)
VALUES
('F57DA5D5', '2021-07-29 09:27:46', 2, 23460);

DROP TABLE clickstream;
SELECT * FROM clickstream;

CREATE TABLE articles(
	id BIGINT,
	title LONGTEXT,
	cerated_by DATETIME,
	update_by DATETIME,
	PRIMARY KEY (id)
);

DROP TABLE articles;
SELECT * FROM articles;

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23456, 'Hello World', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23457, 'Hello World1', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23458, 'Hello World2', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23459, 'Hello World3', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23460, 'Hello World4', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23461, 'Hello World5', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23462, 'Hello World6', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23463, 'Hello World7', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23464, 'Hello World8', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23465, 'Hello World9', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23466, 'Hello World10', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23467, 'Hello World11', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23468, 'Hello World12', '2021-07-30 09:27:46', NOW());

INSERT INTO articles
(id, title, cerated_by, update_by)
VALUES
(23469, 'Hello World13', '2021-07-30 09:27:46', NOW()); 

SELECT objectId, id, action, time, COUNT(*) AS count
FROM clickstream, articles
WHERE clickstream.objectId = articles.id AND clickstream.time <= '2017-04-02 00:00:00' AND clickstream.time >= '2017-03-31 23:59:59' AND clickstream.action = 'LIKE_ARTICLE'
GROUP BY clickstream.action, clickstream.time
ORDER BY count DESC
LIMIT 1;

SELECT count(distinct c1.userId)
FROM clickstream AS c1, clickstream AS c2
WHERE (c1.userId = c2.userId)
AND (c1.action='FIRST_INSTALL' AND c1.time < '2017-04-02' AND c1.time>='2017-04-01') 
AND (c2.action='LIKE_ARTICLE' AND c2.time >= '2017-04-02' AND c2.time <= '2017-04-01');
