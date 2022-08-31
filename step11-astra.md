<!-- TOP -->
<div class="top">
  <img src="https://datastax-academy.github.io/katapod-shared-assets/images/ds-academy-logo.svg" />
  <span class="scenario-title">Time Series Data Modeling</span>
  <span class="scenario-subtitle">ℹ️ For technical support, please contact us via <a href="mailto:aleksandr.volochnev@datastax.com">email</a> or <a href="https://dtsx.io/aleks">LinkedIn</a>.</span> 
</div>

<!-- NAVIGATION -->
<div id="navigation-top" class="navigation-top">
 <a href='command:katapod.loadPage?[{"step":"step10-astra"}]'
   class="btn btn-dark navigation-top-left">⬅️ Back
 </a>
<span class="step-count"> Step 11 of 13</span>
 <a href='command:katapod.loadPage?[{"step":"finish-astra"}]'
    class="btn btn-dark navigation-top-right">Next ➡️
  </a>
</div>

<!-- CONTENT -->

<div class="step-title">Design query Q7</div>

✅ Find tracks from album `Magical Mystery Tour` of `1967`; order by track number (asc):

<details>
  <summary>Solution</summary>

```
SELECT *
FROM tracks_by_album
WHERE album_title = 'Magical Mystery Tour'
  AND album_year  = 1967; 
```

</details>

<!-- NAVIGATION -->
<div id="navigation-bottom" class="navigation-bottom">
 <a href='command:katapod.loadPage?[{"step":"step10-astra"}]'
   class="btn btn-dark navigation-bottom-left">⬅️ Back
 </a>
 <a href='command:katapod.loadPage?[{"step":"finish-astra"}]'
    class="btn btn-dark navigation-bottom-right">Next ➡️
  </a>
</div>

