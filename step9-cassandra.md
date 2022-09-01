<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Time Series Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step8-cassandra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 9 of 11</span>
 <a href='command:katapod.loadPage?[{"step":"step10-cassandra"}]'
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Design query Q5</div>

✅ Retrieve time series with a high resolution of 60 seconds for metric `temperature`, 
group `House A` and time range [`2020-10-04 23:59:00`,`2020-10-05 00:01:00`]; 
order by timestamp (desc) and source (asc):

<details>
  <summary>Solution</summary>

```
SELECT * 
FROM time_series.series_by_metric_high
WHERE group = 'House A'
  AND metric = 'temperature'
  AND timestamp >= '2020-10-04 23:59:00'
  AND timestamp <= '2020-10-05 00:01:00';
```

</details>

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step8-cassandra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step10-cassandra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

