import os
from pathlib import Path


def generate_reports(data, folder):
    """
    Generates reports for the data.
    :param data: DataFrame
    """

    Path(folder).mkdir(parents=True, exist_ok=True)

    # Generate report The top 10 best games for each console/company.
    top_10_games = data.groupby(["console", "company"], as_index=False).apply(
        lambda x: x.nlargest(10, columns="metascore")
    )
    top_10_games.to_csv(os.path.join(folder, "top_10_games.csv"), index=False)

    # Generate report The worst 10 games for each console/company.
    worst_10_games = data.groupby(["console", "company"], as_index=False).apply(
        lambda x: x.nsmallest(10, columns="metascore")
    )
    worst_10_games.to_csv(os.path.join(folder, "worst_10_games.csv"), index=False)

    # Generate report The top 10 best games for all consoles.
    top_10_games_all = data.nlargest(10, columns="metascore")
    top_10_games_all.to_csv(os.path.join(folder, "top_10_games_all.csv"), index=False)

    # Generate report The worst 10 games for all consoles.
    worst_10_games_all = data.nsmallest(10, columns="metascore")
    worst_10_games_all.to_csv(
        os.path.join(folder, "worst_10_games_all.csv"), index=False
    )
