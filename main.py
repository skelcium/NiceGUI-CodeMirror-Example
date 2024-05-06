from nicegui import ui
import sys
from io import StringIO

ui.query('.nicegui-content').classes('p-0')


def run_code():
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(cm.value)
        sys.stdout = old_stdout
        output = redirected_output.getvalue()

        if output:
            ui.notify(redirected_output.getvalue(), color='primary')

    except Exception as e:
        ui.notify(e, color='negative')


with ui.splitter(value=12).classes('h-screen w-screen') as splitter:
    with splitter.before:
        with ui.column().classes('items-center w-full'):
            ui.icon('code', color='primary').classes('my-3 text-5xl')
            ui.button(icon='play_arrow').props('round').on('click', run_code)
    with splitter.after:
        cm = ui.codemirror(language='Python').classes('h-full')


ui.run(native=True)
