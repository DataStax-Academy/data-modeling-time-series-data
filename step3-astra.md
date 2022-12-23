<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <div class="scenario-title-section">
    <span class="scenario-title">Time Series Data Modeling</span>
    <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span>
  </div>
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step2-astra"}]' 
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 3 of 11</span>
 <a href='command:katapod.loadPage?[{"step":"step4-astra"}]' 
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Populate tables using DSBulk</div>

✅ Load data into table `sources_by_group`:
```
astra db load data-modeling             \
            -url assets/sources.csv     \
            -k time_series_data         \
            -t sources_by_group         \
            -header true                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `sources_by_group`:
```
astra db cqlsh data-modeling -e "
SELECT group, source, description, 
       characteristics['Model number'] 
FROM time_series_data.sources_by_group;"      
```

✅ Load data into table `metrics`:
```
astra db load data-modeling             \
            -url assets/metrics.csv     \
            -k time_series_data         \
            -t metrics                  \
            -header true                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `metrics`:
```
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.metrics;"      
```

✅ Load data into tables `series_by_source_high` and `series_by_metric_high`:
```
astra db load data-modeling                         \
            -url assets/series_high_resolution.csv  \
            -k time_series_data                     \
            -t series_by_source_high                \
            -header true                            \
            -logDir /tmp/logs

astra db load data-modeling                         \
            -url assets/series_high_resolution.csv  \
            -k time_series_data                     \
            -t series_by_metric_high                \
            -header true                            \
            -logDir /tmp/logs                        
```

✅ Retrieve rows from tables `series_by_source_high` and `series_by_metric_high`:
```
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.series_by_source_high LIMIT 5;"   
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.series_by_metric_high LIMIT 5;"                                         
```

✅ Load data into tables `series_by_source_low` and `series_by_metric_low`:
```
astra db load data-modeling                         \
            -url assets/series_low_resolution.csv   \
            -k time_series_data                     \
            -t series_by_source_low                 \
            -header true                            \
            -logDir /tmp/logs

astra db load data-modeling                         \
            -url assets/series_low_resolution.csv   \
            -k time_series_data                     \
            -t series_by_metric_low                 \
            -header true                            \
            -logDir /tmp/logs
```

✅ Retrieve rows from tables `series_by_source_low` and `series_by_metric_low`:
```
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.series_by_source_low LIMIT 5;"   
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.series_by_metric_low LIMIT 5;"      
```

✅ Load data into table `statistics_by_source_metric`:
```
astra db load data-modeling                             \
            -url assets/statistics_by_source_metric.csv \
            -k time_series_data                         \
            -t statistics_by_source_metric              \
            -header true                                \
            -logDir /tmp/logs
```

✅ Retrieve rows from table `statistics_by_source_metric`:
```
astra db cqlsh data-modeling -e "SELECT * FROM time_series_data.statistics_by_source_metric LIMIT 5;"      
```

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step2-astra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step4-astra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>
