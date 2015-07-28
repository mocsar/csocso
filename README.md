# csocso
Simple rating system from cmd line based on [TrueSkill](http://trueskill.org/).


## Installation

```bash
virtualenv venv
. venv/bin/activate
pip install git+https://github.com/mocsar/csocso#egg=csocso
csocso config set db-uri URI
```

URI should be given in the standard URI format: `mongodb://[dbuser:dbpassword@]host:port/dbname`

## Usage

Run `csocso --help` for detailed usage.

