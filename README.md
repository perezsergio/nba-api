# Parsing private NBA API with request lib

This repo is a solution to the problem statement `docs/problems_statement.pdf`.
The docstring of the `main.py` script contains an informative summary of how this application
works:

    Parse NBA api, get all the data for player Kobe Bryant,
    store all the stats at 'data/kobe_stats.json'.
    Read from the previous file,
    extract regular season and postseason yearly stats,
    store them at 'data/regseason_yearly_stats.csv' and 'data/postseason_yearly_stats.csv'.
    Read from previous files,
    compare points per game of regular season and postseason for each year,
    store result at 'data/regseason_postseason_comparison.csv'.
    Read from 'data/regseason_yearly_stats.csv'
    compute aggregate statistics (season with min points, career avg points per game, ...)
    store result at 'data/regseason_aggregate_stats.json'

## Usage
As one can see in the previous docstring, the app performs a series of steps:

    1 - Downloading all Kobe Bryant's stats from the NBA API.
    2 - Extracting regular season and postseason yearly stats.
    3 - Comparing the regular season and postseason average points.
    4 - Computing aggregate regular season statistics.

The repo has one separate script for each step: 
`download_kobe_stats.py` 
`write_yearly_stats.py`
`write_regseason_postseason_comparison.py`
`write_regseason_agg_stats.py`
And each script saves its results on a different csv or json file.

To work with updated data, the files should be executed in order (
steps 3 and 4 rely on the file created by step 2 and 
step 2 relies on the file created by step 1.
).

However, apart from that consideration the scripts can be executed independently.
This can be useful in some cases,
for example one could run steps 2, 3, and 4 without an internet connection.
Also, if the dataset was larger it could be useful to save the progress after every step.

There is also the option to execute all 4 steps at once,
using `main.py`


## Alternative solution
I specifically avoided using pandas and jupyter notebooks because
I thought it went against the objective of the problem statement. 
However, it is important to note that the solution for most of the problem 
becomes much easier by using them.
Because of this I also included an alternative solution implemented using pandas
and jupyter notebooks, which can be found in `dev/alternative_solution.ipynb`




