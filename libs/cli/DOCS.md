# `aibaba_ai`

**Usage**:

```console
$ aibaba_ai [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.
* `-v, --version`: Print current CLI version.

**Commands**:

* `app`: Manage Aibaba AI apps
* `serve`: Start the aibaba_ai app, whether it's a...
* `template`: Develop installable templates.

## `aibaba_ai app`

Manage Aibaba AI apps

**Usage**:

```console
$ aibaba_ai app [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds the specified template to the current...
* `new`: Create a new aibaba_ai application.
* `remove`: Removes the specified package from the...
* `serve`: Starts the aibaba_ai app.

### `aibaba_ai app add`

Adds the specified template to the current aibaba_ai app.

e.g.:
aibaba_ai app add extraction-openai-functions
aibaba_ai app add git+ssh://git@github.com/efriis/simple-pirate.git

**Usage**:

```console
$ aibaba_ai app add [OPTIONS] [DEPENDENCIES]...
```

**Arguments**:

* `[DEPENDENCIES]...`: The dependency to add

**Options**:

* `--api-path TEXT`: API paths to add
* `--project-dir PATH`: The project directory
* `--repo TEXT`: Install templates from a specific github repo instead
* `--branch TEXT`: Install templates from a specific branch
* `--help`: Show this message and exit.

### `aibaba_ai app new`

Create a new aibaba_ai application.

**Usage**:

```console
$ aibaba_ai app new [OPTIONS] NAME
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--package TEXT`: Packages to seed the project with
* `--help`: Show this message and exit.

### `aibaba_ai app remove`

Removes the specified package from the current aibaba_ai app.

**Usage**:

```console
$ aibaba_ai app remove [OPTIONS] API_PATHS...
```

**Arguments**:

* `API_PATHS...`: The API paths to remove  [required]

**Options**:

* `--help`: Show this message and exit.

### `aibaba_ai app serve`

Starts the aibaba_ai app.

**Usage**:

```console
$ aibaba_ai app serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--app TEXT`: The app to run, e.g. `app.server:app`
* `--help`: Show this message and exit.

## `aibaba_ai serve`

Start the aibaba_ai app, whether it's a template or an app.

**Usage**:

```console
$ aibaba_ai serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.

## `aibaba_ai template`

Develop installable templates.

**Usage**:

```console
$ aibaba_ai template [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `new`: Creates a new template package.
* `serve`: Starts a demo app for this template.
* `image`: Builds a Docker image for the Python application with REST API exposed.

### `aibaba_ai template new`

Creates a new template package.

**Usage**:

```console
$ aibaba_ai template new [OPTIONS] NAME
```

**Arguments**:

* `NAME`: The name of the folder to create  [required]

**Options**:

* `--with-poetry / --no-poetry`: Don't run poetry install  [default: no-poetry]
* `--help`: Show this message and exit.

### `aibaba_ai template serve`

Starts a demo app for this template.

**Usage**:

```console
$ aibaba_ai template serve [OPTIONS]
```

**Options**:

* `--port INTEGER`: The port to run the server on
* `--host TEXT`: The host to run the server on
* `--help`: Show this message and exit.

### `aibaba_ai template image`

Builds a Docker image for the Python application with REST API exposed.

**Usage**:

```console
$ aibaba_ai template image [OPTIONS]
```

**Options**:

* `--tag TEXT`: The tag for the Docker image
* `--port INTEGER`: The port to expose the REST API on

**Example**:

```console
$ aibaba_ai_cli image --tag myapp-v1 --port 8080
```
