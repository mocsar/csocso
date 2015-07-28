# csocso
Simple rating system from cmd line based on [TrueSkill](http://trueskill.org/).


## Installation

```
sudo pip install git+https://github.com/mocsar/csocso#egg=csocso
csocso config set db-uri URI
```

or

```
git clone https://github.com/mocsar/csocso
sudo pip install csocso/
csocso config set db-uri URI
```

The only supported db is mongoDB.
URI should be given in the standard URI format: `mongodb://[dbuser:dbpassword@]host:port/dbname`

## Usage

Run `csocso --help` for detailed usage.

