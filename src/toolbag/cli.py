import os
import click
# Ordering of command
class NaturalOrderGroup(click.Group):
    def list_commands(self, ctx):
        return self.commands.keys()

# This is used to share config between click commands
class Config(object):
    def __init__(self):
        self.verbose=0
        self.database=None

pass_config=click.make_pass_decorator(Config,ensure=True)

@click.group(cls=NaturalOrderGroup)
@pass_config
def cli(config):
    '''Toolbag'''

@click.command()
@click.option('-u','--url',required=True,help='Url of youtube videos')
@pass_config
def ytdl(config,url):
    '''Download Youtube Videos'''
    from pytubefix import YouTube
    from pytubefix.cli import on_progress    
    yt = YouTube(url, on_progress_callback = on_progress)
    print(f'Downloading {yt.title}')
    ys = yt.streams.get_highest_resolution()
    ys.download()

def get_cli():
    commands=[ytdl]
    for command in commands:
        cli.add_command(command)
    return cli

def main():
    cli=get_cli()
    cli()

if __name__=='__main__':
    main()