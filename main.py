import Pack as p
import Player as pl
import Bot as bt
import Game as g


def main():
    game = g.Game(pl.Player(), bt.Bot(), p.Pack())
    game.get_cards()
    game.find_min_rank_of_players()
    print(game.winner())


if __name__ == '__main__':
    main()
