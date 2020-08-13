CREATE DATABASE IF NOT EXISTS fbref_data;

USE fbref_data;

CREATE TABLE IF NOT EXISTS seasons(

    id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(36) NOT NULL

);

CREATE TABLE IF NOT EXISTS competition(

    id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    season_id INTEGER NOT NULL,
    `name` VARCHAR(36) NOT NULL

);

CREATE TABLE IF NOT EXISTS team(

    id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(36) NOT NULL

);

CREATE TABLE IF NOT EXISTS country(

    id INTEGER AUTO_INCREMENT  NOT NULL PRIMARY KEY,
    `name` VARCHAR(36) NOT NULL

);

CREATE TABLE IF NOT EXISTS player(

    id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` VARCHAR(36) NOT NULL
    born INTEGER,
    position VARCHAR(36),

);

CREATE TABLE IF NOT EXISTS standard_stats(
    competition_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    minutes_played INTEGER,
    starts INTEGER,
    goals INTEGER,
    assists INTEGER,
    penalties_scored INTEGER,
    penalties_attempted INTEGER,
    yellow_cards INTEGER,
    red_cards INTEGER,
    xG DOUBLE,
    npXG DOUBLE,
    xA DOUBLE,
    PRIMARY KEY (competition_id,player_id,team_id,country_id),
    FOREIGN_KEY fk_competition (competition_id) REFERENCES competition (id),
    FOREIGN_KEY fk_player (player_id) REFERENCES player (id),
    FOREIGN_KEY fk_team (team_id) REFERENCES team (id),
    FOREIGN_KEY fk_country (country_id) REFERENCES country (id)
);

CREATE TABLE IF NOT EXISTS standard_stats_per_90(
    competition_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    goals DOUBLE,
    assists DOUBLE,
    goals_plus_assists DOUBLE,
    goals_minus_pens DOUBLE,
    goals_plus_assists_minus_pens DOUBLE,
    xG DOUBLE,
    xA DOUBLE,
    xg_plus_xA DOUBLE,
    npXG DOUBLE,
    npXG_plus_xA DOUBLE,
    PRIMARY KEY (competition_id,player_id,team_id,country_id),
    FOREIGN_KEY fk_competition (competition_id) REFERENCES competition (id),
    FOREIGN_KEY fk_player (player_id) REFERENCES player (id),
    FOREIGN_KEY fk_team (team_id) REFERENCES team (id),
    FOREIGN_KEY fk_country (country_id) REFERENCES country (id)
);
