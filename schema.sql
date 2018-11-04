DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS story;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS choice;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE story (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user(id)
);

CREATE TABLE event (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  story_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (story_id) REFERENCES user (id)
);

CREATE TABLE choice (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL,
  event_from INTEGER NOT NULL,
  event_to INTEGER NOT NULL,
  FOREIGN KEY (event_from) REFERENCES event (id),
  FOREIGN KEY (event_to) REFERENCES event (id)
);