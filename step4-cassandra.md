<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Digital Library Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step3-cassandra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 4 of 13</span>
 <a href='command:katapod.loadPage?[{"step":"step5-cassandra"}]' 
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Insert rows using the CQL shell</div>

✅ Start the CQL shell:
```
cqlsh -k music_data
```

✅ Insert rows into table `users`:
```
INSERT INTO users (id, name)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, 'Joe'); 
INSERT INTO users (id, name)
VALUES (UUID(), 'Jen'); 
INSERT INTO users (id, name)
VALUES (UUID(), 'Jim'); 

SELECT * FROM users;
```

✅ Insert rows into table `tracks_by_user`:
```
INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-01-01', '2020-01-05T11:22:33', '20 Greatest Hits', 1982, 16, 'Hey Jude');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T09:00:00', '20 Greatest Hits', 1982, 16, 'Hey Jude');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T16:41:10', 'Legendary Concert Performances', 1978, 6, 'Johnny B. Goode');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T16:44:56', 'The Beatles 1967-1970', 1973, 17, 'Come Together');

INSERT INTO tracks_by_user (id, month, timestamp, album_title, album_year, number, title)
VALUES (12345678-aaaa-bbbb-cccc-123456789abc, '2020-09-01', '2020-09-15T21:13:13', 'Dark Side Of The Moon', 1973, 3, 'Time');

SELECT * FROM tracks_by_user;
```

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step3-cassandra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step5-cassandra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

