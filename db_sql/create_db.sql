CREATE TABLE user_typing_data (
  time timestamp NOT NULL default CURRENT_TIMESTAMP,
  user_id integer NOT NULL,
  input0 text NOT NULL,
  IP text,
  browser text,
  PRIMARY KEY  (time, user_id)
);
