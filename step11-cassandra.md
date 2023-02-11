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
 <a href='command:katapod.loadPage?[{"step":"step10-cassandra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 11 of 11</span>
 <a href='command:katapod.loadPage?[{"step":"finish-cassandra"}]'
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Design query Q7</div>

✅ Find daily min, max, median, mean and standard deviation values for 
a time series with source `Termostate A2`, metric `humidity` and 
date range [`2019-12-25`,`2020-01-07`]; order by date (desc):

<details>
  <summary>Solution</summary>

```
SELECT * 
FROM time_series_data.statistics_by_source_metric
WHERE source = 'Termostate A2'
  AND metric = 'humidity'
  AND date >= '2019-12-25'
  AND date <= '2020-01-07';
```

</details>

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step10-cassandra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"finish-cassandra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

