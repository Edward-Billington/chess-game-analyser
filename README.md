# chess-game-analyser
A small application that will analyse games from Lichess' open database: https://database.lichess.org/, the resulting output will be used to train an "ELO guessing" ML model.

### Setup
- First clone the repository and download a `.pgn.zst` file from https://database.lichess.org/ into the root directory.
- Run `docker compose up --build -d`
- Run `docker compose exec python-chess analyse`
- Wait for output.
