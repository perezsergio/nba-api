"""
Read json file with the yearly regular season stats,
compute aggregate stats based on the yearly stats, and write the results to a csv.
"""
from pathlib import Path
from functools import reduce

from utils.write_and_read_files import read_matrix_from_csv, write_json_from_dict
from utils.matrix_filtering import filter_matrix_by_column_names


def compute_agg_stats(stats: list[list]) -> dict:
    """
    Use the yearly stats to compute the season with the least total points,
    the season with the most total points,
    and the career averages for points, rebounds and assists
    """
    # Keep only the necessary columns for the calculations
    filtered_stats = filter_matrix_by_column_names(
        stats, ["SEASON_ID", "GP", "REB", "AST", "PTS"]
    )[1:]

    # multiply GP * (PTS, AST, REB) to get the totals per season
    totals_per_season = [
        [
            season,
            int(gp),
            int(gp) * float(reb),
            int(gp) * float(ast),
            int(gp) * float(pts),
        ]
        for (season, gp, reb, ast, pts) in filtered_stats
    ]

    # compute the sum of each column, the 2nd sum is the career_total_games,
    # the 3rd the total rebs...
    (
        _,
        career_total_games,
        career_total_reb,
        career_total_ast,
        career_total_pts,
    ) = reduce(lambda a, b: [a[i] + b[i] for i in range(len(a))], totals_per_season)

    # season with the least total points
    row_min_pts = reduce(lambda a, b: a if a[4] < b[4] else b, totals_per_season)
    season_min_points = row_min_pts[0]

    # season with the most total points
    row_max_pts = reduce(lambda a, b: a if a[4] > b[4] else b, totals_per_season)
    season_max_points = row_max_pts[0]

    # return a dict with the aggregate stats
    return {
        "career_reb_per_game": career_total_reb / career_total_games,
        "career_ast_per_game": career_total_ast / career_total_games,
        "career_pts_per_game": career_total_pts / career_total_games,
        "season_min_points": season_min_points,
        "season_max_points": season_max_points,
    }


def main():
    """
    Read Kobe stats from json file, and filter them to get the yearly regular season stats.
    Store the yearly regular season stats in a csv file.
    """
    # define data directory
    data_dir = Path(__file__).parent.parent.parent / "data"

    # get regular season yearly stats from csv file
    stats = read_matrix_from_csv(str(data_dir / "regseason_yearly_stats.csv"))

    # compute aggregate career stats
    agg_stats = compute_agg_stats(stats)

    # write agg stats to json file
    write_json_from_dict(agg_stats, str(data_dir / "regseason_aggregate_stats.json"))


if __name__ == "__main__":
    main()
