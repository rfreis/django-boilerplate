# Django 4.1 Boilerplate

This repository has a default application using `Django 4.1` running on `Docker`, `docker-compose` and `postgresql`.

## Requirements

To make this run you must have installed:

* docker
* docker-compose

## Formatting

To run black before commiting, install `pre-commit`:

```bash
make pre-commit-install
```

## Running application

```bash
make start-local
```

## Stopping application

```bash
make stop
```

## Local bash

```bash
make local-bash
```

## Logs

```bash
make logs
```

## Tests

```bash
make test
```