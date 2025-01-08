# `aiagentsforce`

**Usage**:

```console
$ aiagentsforce [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.
* `-v, --version`: Print current CLI version.

**Commands**:

* `app`: Manage AI Agents Force apps
* `serve`: Start the aiagentsforceapi app, whether it's a...
* `template`: Develop installable templates.

## `aiagentsforce app`

Manage AI Agents Force apps

**Usage**:

```console
$ aigentsforce app [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds the specified template to the current...
* `new`: Create a new aiagentsforceapi application.
* `remove`: Removes the specified package from the...
* `serve`: Starts the aiagentsforceapi app.

### `aigentsforce app add`

Adds the specified template to the current aiagentsforceapi app.

e.g.:
aigentsforce app add extraction-openai-functions
aigentsforce app add git+ssh://git@github.com/efriis/simple-pirate.git

**Usage**:

```console
$ aigentsforce app add [OPTIONS] [DEPENDENCIES]...
```

**Arguments**:

* `[DEPENDENCIES]...`: The dependency to add

**Options**:

* `--api-path TEXT`: API paths to add
* `--project-dir PATH`: The project directory
* `--repo TEXT`: Install templates from a specific github repo instead
* `--branch TEXT`: Install templates from a specific branch
* `--help`: Show this message and exit.

### `aiagentsforce app new`

Create a new aiagentsforceapi application.

**Usage**:

```console
$ aigentsforce app new [OPTIONS] NAME
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--package TEXT`: Packages to seed the project with
* `--help`: Show this message and exit.

### `aigentsforce app remove`

Removes the specified package from the current aiagentsforceapi app.

**Usage**:

```console
$ aigentsforce app remove [OPTIONS] API_PATHS...
```

**Arguments**:

* `API_PATHS...`: The API paths to remove  [required]

**Options**:

* `--help`: Show this message and exit.

### `aigentsforce app serve`

Starts the aiagentsforceapi app.

**Usage**:

```console
$ aigentsforce app serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--app TEXT`: The app to run, e.g. `app.server:app`
* `--help`: Show this message and exit.

## `aiagentsforce serve`

Start the aiagentsforceapi app, whether it's a template or an app.

**Usage**:

```console
$ aiagentsforce serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.

## `aiagentsforce template`

Develop installable templates.

**Usage**:

```console
$ aiagentsforce template [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `new`: Creates a new template package.
* `serve`: Starts a demo app for this template.

### `aiagentsforce template new`

Creates a new template package.

**Usage**:

```console
$ aiagentsforce template new [OPTIONS] NAME
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--with-poetry / --no-poetry`: Don't run poetry install  [default: no-poetry]
* `--help`: Show this message and exit.

### `aiagentsforce template serve`

Starts a demo app for this template.

**Usage**:

```console
$ aiagentsforce template serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.
