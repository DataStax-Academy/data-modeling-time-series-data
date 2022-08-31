<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Time Series Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step1-astra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 2 of 13</span>
 <a href='command:katapod.loadPage?[{"step":"step3-astra"}]' 
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Create tables</div>

✅ Create tables `performers`, `albums_by_performer`, `albums_by_title`, 
`albums_by_genre`, `tracks_by_title`, `tracks_by_album`, `users` and `tracks_by_user`:
```
astra db cqlsh data-modeling -k music_data -e "

CREATE TABLE IF NOT EXISTS performers (
  name TEXT,
  type TEXT,
  country TEXT,
  born INT,
  died INT,
  founded INT,
  PRIMARY KEY ((name))
);

CREATE TABLE IF NOT EXISTS albums_by_performer (
  performer TEXT,
  year INT,
  title TEXT,
  genre TEXT,
  PRIMARY KEY ((performer),year,title)
) WITH CLUSTERING ORDER BY (year DESC, title ASC);

CREATE TABLE IF NOT EXISTS albums_by_title (
  title TEXT,
  year INT,
  performer TEXT,
  genre TEXT,
  PRIMARY KEY ((title),year)
) WITH CLUSTERING ORDER BY (year DESC);

CREATE TABLE IF NOT EXISTS albums_by_genre (
  genre TEXT,
  year INT,
  title TEXT,
  performer TEXT,
  PRIMARY KEY ((genre),year,title)
) WITH CLUSTERING ORDER BY (year DESC, title ASC);

CREATE TABLE IF NOT EXISTS tracks_by_title (
  title TEXT,
  album_year INT,
  album_title TEXT,
  number INT,
  length INT,
  genre TEXT,
  PRIMARY KEY ((title),album_year,album_title,number)
) WITH CLUSTERING ORDER BY (album_year DESC, album_title ASC, number ASC);

CREATE TABLE IF NOT EXISTS tracks_by_album (
  album_title TEXT,
  album_year INT,
  number INT,
  title TEXT,
  length INT,
  genre TEXT STATIC,
  PRIMARY KEY ((album_title,album_year),number)
);

CREATE TABLE IF NOT EXISTS users (
  id UUID,
  name TEXT,
  PRIMARY KEY ((id))
);

CREATE TABLE IF NOT EXISTS tracks_by_user (
  id UUID,
  month DATE,
  timestamp TIMESTAMP,
  album_title TEXT,
  album_year INT,
  number INT,
  title TEXT,
  length INT,
  PRIMARY KEY ((id,month),timestamp,album_title,album_year,number)
) WITH CLUSTERING ORDER BY (timestamp DESC, album_title ASC, album_year ASC, number ASC);"
```

✅ Verify that the eight tables have been created:
```
astra db cqlsh data-modeling -k music_data -e "DESCRIBE TABLES;"
```

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step1-astra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step3-astra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>
