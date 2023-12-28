"""
Read json file with the career stats of Kobe Bryant,
write a 2 csv files with the yearly stats: 
one containing the regular season stats and the other the postseason stats.
"""
from pathlib import Path
from utils.write_and_read_files import read_json, write_csv_from_matrix
from utils.matrix_filtering import filter_matrix_by_column_names


def parse_yearly_stats(stats: dict, stage: str) -> list[list]:
    """
    Parse player stats,
    return a matrix with the yearly regular season or postseason stats
    """
    # Find the yearly stats inside the stats dict
    if stage == "postseason":
        yearly_stats = stats["resultSets"][2]
    elif stage == "regseason":
        yearly_stats = stats["resultSets"][0]
    else:
        raise ValueError("stage must be a value in ['postseason', 'regseason']")

    # Find the headers and data inside the reg_season dict
    headers = yearly_stats["headers"]
    data = yearly_stats["rowSet"]

    # Construct a matrix where the first row is the header and the rest of the rows are the data
    yearly_stats_matrix = [headers, *data]

    return yearly_stats_matrix


def main():
    """
    Read Kobe stats from json file,
    filter them to get the yearly regular season and postseason stats.
    Store the yearly regular season and postseason stats in 2 csv files.
    """
    # define data directory
    data_dir = Path(__file__).parent.parent.parent / "data"

    # read Kobe career stats from json file
    kobe_stats = read_json(str(data_dir / "kobe_stats.json"))

    # Set the columns of interest. We'll use them later to filter the data.
    columns_of_interest = [
        "SEASON_ID",
        "PLAYER_AGE",
        "GP",
        "PTS",
        "AST",
        "REB",
    ]

    for stage in ["regseason", "postseason"]:
        # get matrix with yearly stats
        yearly_stats = parse_yearly_stats(kobe_stats, stage=stage)

        # Filter the matrix, only keep the columns of interest
        filtered_yearly_stats = filter_matrix_by_column_names(
            yearly_stats, columns_of_interest
        )

        # Write filtered matrix to csv
        write_csv_from_matrix(
            filtered_yearly_stats, path=str(data_dir / f"{stage}_yearly_stats.csv")
        )


if __name__ == "__main__":
    main()
