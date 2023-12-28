"""
Execute all the scripts in the module.

Parse nba api, download Kobe's stats, get yearly regseason and postseason stats,
compute aggregate statistics from regseason stats, 
compares postseason and regseason points, 
and saves all this data in csv and json files.
"""
from download_kobe_stats import main as download_kobe_stats
from write_yearly_stats import main as write_yearly_stats
from write_regseason_agg_stats import main as write_regseason_agg_stats
from write_regseason_postseason_comparison import (
    main as write_regseason_postseason_comparison,
)


def main():
    """
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
    """
    download_kobe_stats()
    write_yearly_stats()
    write_regseason_agg_stats()
    write_regseason_postseason_comparison()


if __name__ == "__main__":
    main()
