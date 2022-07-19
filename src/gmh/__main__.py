'''
------------------------------------------------------------------------------
Copyright 2022 Violin Yanev
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
------------------------------------------------------------------------------
'''

import click

# TODO Switch import style to "from ghm import xxx
import config


@click.group()
def cli():
    """Tool for working with multiple Github hosts simultaneously

    Filter only relevant PRs. Automation of trivial tasks. And more!
    """
    pass


@cli.command('configure', short_help='Creates user config')
def configure():
    """Creates two configuration files in $HOME/.useful path. One to store interesting
    repositories, connection settings, and custom option. And one to hold a set of
    currently ignored (snoozed) PRs. Both files can be also modified manually.
    """
    config.create()


if __name__ == '__main__':
    cli(auto_envvar_prefix='GMH')
