import config

import typer
from rich import print
from canvasapi import Canvas
from todoist_api_python.api import TodoistAPI as Todoist


def main(
    ids: list[int] = typer.Argument(..., help="A list of Canvas course IDs"),
    dry_run: bool = typer.Option(False, help="Do not add anything to Todoist",
                                 show_default=False),
):
    """
    Add Canvas assignments as Todoist tasks
    """
    canvas = Canvas(config.CANVAS_API_URL, config.CANVAS_API_KEY)
    todoist = Todoist(config.TODOIST_API_KEY)

    for course in map(canvas.get_course, ids):
        print(f"[blue]{course.name}[/]")
        if not dry_run:
            project = todoist.add_project(name=course.name)
        for assignment in course.get_assignments():
            if not dry_run:
                todoist.add_task(
                    content=assignment.name,
                    due_datetime=assignment.due_at,
                    project_id=project.id,
                    description=assignment.html_url
                )

            print(f"- [green]{assignment.name}[/]")
        print()


if __name__ == "__main__":
    typer.run(main)
