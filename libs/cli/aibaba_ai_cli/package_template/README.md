# __package_name__

TODO: What does this package do

## Environment Setup

TODO: What environment variables need to be set (if any)

## Usage

To use this package, you should first have the Aibaba AI CLI installed:

```shell
pip install -U aibaba_ai_   cli
```

To create a new Aibaba AI project and install this as the only package, you can do:

```shell
aibaba_ai app new my-app --package __package_name__
```

If you want to add this to an existing project, you can just run:

```shell
aibaba_ai app add __package_name__
```

And add the following code to your `server.py` file:
```python
__app_route_code__
```

(Optional) Let's now configure LangSmith. 
LangSmith will help us trace, monitor and debug Aibaba AI applications. 
You can sign up for LangSmith [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are inside this directory, then you can spin up a aibaba_ai instance directly by:

```shell
aibaba_ai serve
```

This will start the FastAPI app with a server is running locally at 
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/__package_name__/playground](http://127.0.0.1:8000/__package_name__/playground)  

We can access the template from code with:

```python
from aibaba_ai.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/__package_name__")
```