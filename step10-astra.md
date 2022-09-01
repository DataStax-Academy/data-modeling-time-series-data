<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Time Series Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step9-astra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 10 of 13</span>
 <a href='command:katapod.loadPage?[{"step":"step11-astra"}]'
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Design query Q6</div>

✅ Retrieve time series with a low resolution of 60 minutes for metric `temperature`, 
group `House A` and time range [`2019-01-01 00:00:00`,`2019-01-01 06:00:00`]; 
order by timestamp (desc) and source (asc):

<details>
  <summary>Solution</summary>

```
SELECT * 
FROM time_series.series_by_metric_low
WHERE group = 'House A'
  AND year = 2019
  AND metric = 'temperature'
  AND timestamp >= '2019-01-01 00:00:00'
  AND timestamp <= '2019-01-01 06:00:00';
```

</details>

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step9-astra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step11-astra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

