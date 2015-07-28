import click
from player import Player
from settings import Settings

__author__ = 'mocsar'


@click.group()
def cli():
    pass


@cli.command()
@click.argument('key', type=click.Choice(Settings.get_all_keys()), nargs=1, required=True)
def get(key):
    """
    Get configuration parameter.
    """
    try:
        click.echo(Settings.get(key))
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


# noinspection PyShadowingBuiltins
@cli.command()
@click.argument('key', type=click.Choice(Settings.get_all_keys()), nargs=1, required=True)
@click.argument('value', type=str, nargs=1, required=True)
def set(key, value):
    """
    Set configuration parameter.
    """
    try:
        Settings.set(key, value)
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


@cli.command()
@click.argument('name', type=str, nargs=1, required=True)
def add(name):
    """
    Registers a new player.

    Example: `csocso add times`
    """
    try:
        if Player.get_player(name):
            click.echo('Player already exists:%s' % name)
            return 1
        else:
            Player.create_player(name)
            click.echo('Player successfully created:%s' % name)
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


# noinspection PyShadowingBuiltins,PyShadowingNames
@cli.command()
def list():
    """
    Prints the leaderboard. The list contains all the registered player.
    """
    try:
        leaderboard = Player.get_leaderboard()
        if leaderboard:
            i = 1
            for player in leaderboard:
                click.echo('%s %s %s' % (i, player.name, player.get_score()))
                i += 1
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


# noinspection PyShadowingBuiltins,PyShadowingNames
@cli.command()
@click.argument('names', type=click.Choice(Player.get_all_names()), nargs=4, required=True, )
def rate(names):
    """
    Rates the specified players. The players specified in the first and the second arguments are the winners. The third and forth argument specify the losers.

    Example:
    `csocso rate axt mocsar nagysandortibor janoska`
    where 'axt' and 'mocsar' are the winners, 'nagysandortibor' and 'janoska' are the losers.
    """
    try:
        Player.rate(names)
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


# @cli.command()
# def test():
#     store = Mongo()
#     store.set_score('muki', 5.1)
#     print 'miki', store.get_score('miki')
#     print 'tomi', store.get_score('tomi')
#     print 'muki', store.get_score('muki')
#
#     print store.get_all_player()
#
#     store.close()

# def list_choices():
#     lines = None
#     with open('test.txt', 'r') as f:
#         lines = f.readlines()
#     if lines:
#         return [s.strip() for s in lines]
#     return []
#
#
# @click.command()
# @click.option('--count', '-c', default=1, help='number of greetings')
# @click.option('--choice', '-C', type=click.Choice(list_choices()), help='you can choice')
# @click.argument('word', type=click.Choice(['chronos', 'marathon', 'chronos-unscheduled', 'all']), nargs=-1, required=True)
# def cli(count, word, choice):
#     """Example script."""
#     click.echo(choice)
#     for i in xrange(count):
#         click.echo('Hello {}!'.format(word))