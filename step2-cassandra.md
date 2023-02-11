<!-- TOP -->
<div class="top">
  <img class="scenario-academy-logo" src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-2023.svg" />
  <div class="scenario-title-section">
    <span class="scenario-title">Time Series Data Modeling</span>
    <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span>
  </div>
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step1-cassandra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 2 of 11</span>
 <a href='command:katapod.loadPage?[{"step":"step3-cassandra"}]' 
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Create tables</div>

✅ Create tables `sources_by_group`, `metrics`, `series_by_source_high`, 
`series_by_source_low`, `series_by_metric_high`, `series_by_metric_low` and `statistics_by_source_metric`:
```
cqlsh -e "

USE time_series_data;

CREATE TABLE IF NOT EXISTS sources_by_group (
  group TEXT,
  source TEXT,
  characteristics MAP<TEXT,TEXT>,
  description TEXT STATIC,
  PRIMARY KEY ((group), source)
);

CREATE TABLE IF NOT EXISTS metrics (
  bucket TEXT,
  metric TEXT,
  unit TEXT,
  PRIMARY KEY ((bucket), metric)
);

CREATE TABLE IF NOT EXISTS series_by_source_high (
  group TEXT,
  source TEXT,
  timestamp TIMESTAMP,
  metric TEXT,
  value DECIMAL,
  PRIMARY KEY ((group, source), timestamp, metric)
) WITH CLUSTERING ORDER BY (timestamp DESC, metric ASC);

CREATE TABLE IF NOT EXISTS series_by_source_low (
  group TEXT,
  year INT,
  source TEXT,
  timestamp TIMESTAMP,
  metric TEXT,
  value DECIMAL,
  PRIMARY KEY ((group, year), source, timestamp, metric)
) WITH CLUSTERING ORDER BY (source ASC, timestamp DESC, metric ASC);

CREATE TABLE IF NOT EXISTS series_by_metric_high (
  group TEXT,
  metric TEXT,  
  timestamp TIMESTAMP,
  source TEXT,
  value DECIMAL,
  PRIMARY KEY ((group, metric), timestamp, source)
) WITH CLUSTERING ORDER BY (timestamp DESC, source ASC);

CREATE TABLE IF NOT EXISTS series_by_metric_low (
  group TEXT,
  year INT,
  metric TEXT,  
  timestamp TIMESTAMP,
  source TEXT,
  value DECIMAL,
  PRIMARY KEY ((group, year, metric), timestamp, source)
) WITH CLUSTERING ORDER BY (timestamp DESC, source ASC);

CREATE TABLE IF NOT EXISTS statistics_by_source_metric (
  source TEXT,
  metric TEXT,
  date DATE,
  min DECIMAL,
  max DECIMAL,
  median DECIMAL,
  mean DECIMAL,
  stdev DECIMAL,       
  PRIMARY KEY ((source,metric),date)
) WITH CLUSTERING ORDER BY (date DESC);"
```

✅ Verify that the seven tables have been created:
```
cqlsh -k time_series_data -e "DESCRIBE TABLES;"
```

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step1-cassandra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step3-cassandra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>
