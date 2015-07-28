import click
from player import Player
from settings import Settings

__author__ = 'mocsar'

RED    = '\033[31m'
YELLOW = '\033[33m'
BRIGHT = '\033[1m'
WHITE  = '\033[37m'
RESET  = '\033[0m'

@click.group()
def cli():
    pass


@cli.command(name="get")
@click.argument('key', type=click.Choice(Settings.get_all_keys()), nargs=1, required=True)
def get_config(key):
    """
    Get configuration parameter.
    """
    try:
        click.echo(Settings.get(key))
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


@cli.command(name="set")
@click.argument('key', type=click.Choice(Settings.get_all_keys()), nargs=1, required=True)
@click.argument('value', type=str, nargs=1, required=True)
def set_config(key, value):
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
            click.echo('Player already exists: %s' % name)
            return 1
        else:
            Player.create_player(name)
            click.echo('Player successfully created: %s' % name)
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


@cli.command(name='list')
def lst():
    """
    Prints the leaderboard. The list contains all the registered player.
    """
    try:
        leaderboard = Player.get_leaderboard()
        if leaderboard:
            i = 1
            for player in leaderboard:
                if i == 1:
                    prefix = YELLOW + BRIGHT
                    postfix = RESET
                elif 2 <= i <= 3:
                    prefix = BRIGHT
                    postfix = RESET
                else:
                    prefix = ''
                    postfix = ''
                click.echo((prefix + '%2i  %8s (%.0f)' + postfix) % (i, player.name, player.get_score()))
                i += 1
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)


@cli.command()
@click.argument('names', type=click.Choice(Player.get_all_names()), nargs=4, required=True)
def rate(names):
    """
    Rates the specified players. The players specified in the first and the second arguments are the winners. The third and forth argument specify the losers.

    Example:
    `csocso rate axt mocsar nagysandortibor janoska`
    where 'axt' and 'mocsar' are the winners, 'nagysandortibor' and 'janoska' are the losers.
    """
    try:
        Player.rate(list(names))
    except Exception as ex:
        raise click.ClickException('Some error while setting: %s' % ex)

