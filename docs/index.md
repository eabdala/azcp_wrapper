<div>
<p align="center">
   <h1 align="center"> azcp_wrapper</h1>
   <p align="center"> A simple AzCopy wrapper to transfer data
</p>

</div>

<div class="termy">
```sh
$ python -m pip install azcp_wrapper

$ python -m azcp_init

```
</div>

* <a href="https://www.google.com" class="external-link" target="_blank">Google</a> for the web parts.

<div class="termy">

```console
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>uvicorn main:app --reload</code>...</summary>

The command `uvicorn main:app` refers to:

* `main`: the file `main.py` (the Python "module").
* `app`: the object created inside of `main.py` with the line `app = FastAPI()`.
* `--reload`: make the server restart after code changes. Only do this for development.

</details>

```JSON
{"item_id": 5, "q": "somequery"}
```
