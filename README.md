# Canvas + Todoist

A short and simple script to grab [Canvas](https://community.canvaslms.com/t5/Canvas-Basics-Guide/What-is-Canvas/ta-p/45) assignments and add them as [Todoist](https://todoist.com) tasks. A new Todoist project is created for each Canvas course.

# Usage

This project uses [Poetry](https://python-poetry.org/) to manage dependencies. To install the dependencies, run `poetry install`.

Then, to spawn a shell within the virtual environment, run `poetry shell`.

Finally, run `python main.py`!

# API Keys

This project makes use of the Canvas and Todoist APIs, both of which require API keys. Once you have both, add them in [`config.py`](./config.py), along with the base URL of your Canvas instance.
