"""
Downloads Kobe Bryant's career stats to a json file.    
"""
from pathlib import Path
import requests
from utils.write_and_read_files import write_json_from_dict


def parse_kobe_career_stats() -> dict:
    """
    Parse NBA api, get the career stats for Kobe Bryant (PlayerID = 977).
    """

    url = "https://stats.nba.com/stats/playercareerstats"
    params = {
        "LeagueID": "00",
        "PerMode": "PerGame",
        "PlayerID": "977",
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "stats.nba.com",
        "Origin": "https://www.nba.com",
        "Referer": "https://www.nba.com/",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    }

    response = requests.get(url, headers=headers, params=params, timeout=3)
    return response.json()


def main():
    """
    Parse NBA api, get the per-game career stats for Kobe Bryant, and store them in a json file.
    """
    # define data directory
    data_dir = Path(__file__).parent.parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)  # mkdir will be ignored if dir exists

    # get kobe career stats
    kobe_stats = parse_kobe_career_stats()

    # write stats to json
    write_json_from_dict(kobe_stats, path=str(data_dir / "kobe_stats.json"))


if __name__ == "__main__":
    main()
