/*
IS211 - Assignment 10 - music.sql
*/

DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;

CREATE TABLE IF NOT EXISTS artists (
artistID INT NOT NULL AUTO_INCREMENT,
artistName VARCHAR(255) NOT NULL,
PRIMARY KEY (artistID));

CREATE TABLE IF NOT EXISTS albums (
albumID INT NOT NULL AUTO_INCREMENT,
albumName VARCHAR(255) NOT NULL,
albumArtist VARCHAR(255) NOT NULL,
PRIMARY KEY (albumID));

CREATE TABLE IF NOT EXISTS songs (
songID INT NOT NULL AUTO_INCREMENT,
songName VARCHAR(255) NOT NULL,
songAlbum VARCHAR(255) NOT NULL,
songTrackNumber VARCHAR(255) NOT NULL,
songLength INT NOT NULL,
PRIMARY KEY (songID));

/*
Insert example:

INSERT INTO artists
(artistID, artistName)
VALUES
(, 'Pearl Jam'),
(, 'Rage Against The Machine'),
(, 'Tool');

*/
