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
 <a href='command:katapod.loadPage?[{"step":"step2-cassandra"}]' 
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 3 of 11</span>
 <a href='command:katapod.loadPage?[{"step":"step4-cassandra"}]' 
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Populate tables using DSBulk</div>

✅ Load data into table `sources_by_group`:
```
dsbulk load -url assets/sources.csv     \
            -k time_series_data         \
            -t sources_by_group         \
            -header true                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `sources_by_group`:
```
cqlsh -e "
SELECT group, source, description, 
       characteristics['Model number'] 
FROM time_series_data.sources_by_group;"      
```

✅ Load data into table `metrics`:
```
dsbulk load -url assets/metrics.csv     \
            -k time_series_data         \
            -t metrics                  \
            -header true                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `metrics`:
```
cqlsh -e "SELECT * FROM time_series_data.metrics;"      
```

✅ Load data into tables `series_by_source_high` and `series_by_metric_high`:
```
dsbulk load -url assets/series_high_resolution.csv  \
            -k time_series_data                     \
            -t series_by_source_high                \
            -header true                            \
            -logDir /tmp/logs
            
dsbulk load -url assets/series_high_resolution.csv  \
            -k time_series_data                     \
            -t series_by_metric_high                \
            -header true                            \
            -logDir /tmp/logs                        
```

✅ Retrieve rows from tables `series_by_source_high` and `series_by_metric_high`:
```
cqlsh -e "SELECT * FROM time_series_data.series_by_source_high LIMIT 5;"   
cqlsh -e "SELECT * FROM time_series_data.series_by_metric_high LIMIT 5;"                                         
```

✅ Load data into tables `series_by_source_low` and `series_by_metric_low`:
```
dsbulk load -url assets/series_low_resolution.csv   \
            -k time_series_data                     \
            -t series_by_source_low                 \
            -header true                            \
            -logDir /tmp/logs
            
dsbulk load -url assets/series_low_resolution.csv   \
            -k time_series_data                     \
            -t series_by_metric_low                 \
            -header true                            \
            -logDir /tmp/logs
```

✅ Retrieve rows from tables `series_by_source_low` and `series_by_metric_low`:
```
cqlsh -e "SELECT * FROM time_series_data.series_by_source_low LIMIT 5;"   
cqlsh -e "SELECT * FROM time_series_data.series_by_metric_low LIMIT 5;"      
```

✅ Load data into table `statistics_by_source_metric`:
```
dsbulk load -url assets/statistics_by_source_metric.csv \
            -k time_series_data                         \
            -t statistics_by_source_metric              \
            -header true                                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `statistics_by_source_metric`:
```
cqlsh -e "SELECT * FROM time_series_data.statistics_by_source_metric LIMIT 5;"      
```

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step2-cassandra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step4-cassandra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>
