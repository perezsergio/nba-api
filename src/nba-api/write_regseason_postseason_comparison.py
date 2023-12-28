"""
Read regular season and postseason points for every season,
compare the 2 values and write the results to a csv.
"""
from pathlib import Path
from utils.write_and_read_files import read_matrix_from_csv, write_csv_from_matrix
from utils.matrix_filtering import filter_matrix_by_column_names
from utils.floats_with_na import defaultdict_with_na, compare_with_na


def get_pts_per_season_dict(yearly_stats: list[list]) -> dict:
    """
    Given a matrix with the yearly stats,
    return a dict of key:value pairs
    where the keys are all the seasons that appear in the yearly stats
    and the values are the average point for that season
    """
    # Only keep 'SEASON_ID', 'PTS' columns, drop headers.
    filtered_yearly_stats = filter_matrix_by_column_names(
        yearly_stats, ["SEASON_ID", "PTS"]
    )[1:]
    # Construct dict
    pts_per_season = defaultdict_with_na(
        {season: float(pts) for (season, pts) in filtered_yearly_stats}
    )
    return pts_per_season


def compare_regseason_postseason(
    regseason: list[list], postseason: list[list]
) -> list[list]:
    """
    Given the yearly stats for the postseason and regular season,
    construct a matrix (list of lists) with the columns
    ['SEASON_ID', 'PTS_REGSEASON', 'PTS_POSTSEASON', 'BETTER_IN_POSTSEASON']
    """

    # Get regseason yearly stats, create a dict with season:pts_per_season pairs
    pts_per_regseason = get_pts_per_season_dict(regseason)

    # Get postseason yearly stats, create a dict with season:pts_per_postseason pairs
    pts_per_postseason = get_pts_per_season_dict(postseason)

    # Construct a matrix with the columns:
    # ['SEASON_ID', 'PTS_REGSEASON', 'PTS_POSTSEASON', 'BETTER_IN_POSTSEASON']
    pts_per_season = [
        [
            season,
            pts_per_regseason[season],
            pts_per_postseason[season],
            compare_with_na(pts_per_postseason[season], pts_per_regseason[season]),
        ]
        for season in pts_per_regseason.keys()
    ]
    headers = ["SEASON_ID", "PTS_REGSEASON", "PTS_POSTSEASON", "BETTER_IN_POSTSEASON"]

    return [headers] + pts_per_season


def main():
    """
    Read regular season and postseason yearly stats from csv files,
    filter them to get the postseason and regseason pts for every season,
    and compare them to see which one is higher.
    Store the regseason and postseason points as well as the comparison in a csv file.
    """
    # define data directory
    data_dir = Path(__file__).parent.parent.parent / "data"

    # get regular season and postseason yearly stats from csv files
    regseason = read_matrix_from_csv(str(data_dir / "regseason_yearly_stats.csv"))
    postseason = read_matrix_from_csv(str(data_dir / "postseason_yearly_stats.csv"))

    # Get matrix with pts per game comparison between the regseason and the postseason
    pts_comparison = compare_regseason_postseason(regseason, postseason)

    # Write matrix with pts comparison to csv
    write_csv_from_matrix(
        pts_comparison, path=str(data_dir / "regseason_postseason_comparison.csv")
    )


if __name__ == "__main__":
    main()
