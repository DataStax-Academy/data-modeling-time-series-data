<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Time Series Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step6-astra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 7 of 13</span>
 <a href='command:katapod.loadPage?[{"step":"step8-astra"}]'
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Design query Q3</div>

✅ Retrieve time series with a high resolution of 60 seconds for group `House A`, 
sources `Refrigerator A1` and `Freezer A1`, and time range [`2020-10-05 12:44:00`,`2020-10-05 12:47:00`]; 
order by timestamp (desc) and metric (asc):

<details>
  <summary>Solution</summary>

```
SELECT * 
FROM time_series.series_by_source_high
WHERE group = 'House A'
  AND source IN ('Refrigerator A1','Freezer A1')
  AND timestamp >= '2020-10-05 12:44:00'
  AND timestamp <= '2020-10-05 12:47:00';
```

</details>

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step6-astra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"step8-astra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

