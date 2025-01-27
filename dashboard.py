import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import os
from extractingMetadata import extract_metadata, process_photos
from checkPaths import process_photos_and_check_paths


# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("SnapSync Metadata Comparison Tool"),
    dcc.Input(id='input-folder', type='text', placeholder='Enter folder path...'),
    html.Button('Load and Compare Metadata', id='load-button'),
    html.Div(id='output-container')])

# Define callback to update the output container
@app.callback(
    Output('output-container', 'children'),
    [Input('load-button', 'n_clicks')],
    [dash.dependencies.State('input-folder', 'value')])
def update_output(n_clicks, value):
    if n_clicks and value:
        directory = value
        if os.path.exists(directory):
            results = process_photos_and_check_paths(directory)
            return html.Ul([html.Li(f"{result}") for result in results])
        else:
            return "The provided folder path does not exist. Please enter a valid path."
    return "Enter a folder path and click the button to load and compare metadata."


if __name__ == '__main__':
    app.run_server(debug=True)
