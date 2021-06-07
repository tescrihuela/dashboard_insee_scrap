# coding: utf8
#!/usr/bin/python3

import flask
import dash
import dash_table
import dash_html_components as html
import requests
import pandas as pd


data_insee = 'https://gitlab.com/jdlom/data_insee/-/jobs/artifacts/master/raw/data_insee.csv?job=insee_scrap'
df = pd.read_csv(data_insee, sep = ';')


#########
# Serveur
server = flask.Flask(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, server = server, title = 'Insee Data', external_stylesheets = external_stylesheets)
app.config.suppress_callback_exceptions = True


##########
### Layout
app.layout = html.Div(
    id = 'page',
    children = [
        html.H1('Données de l\'INSEE'),
        html.Div([
            dash_table.DataTable(
                id = 'datatable-interactivity',
                columns = [
                    {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
                ],
                style_header = {
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                style_data_conditional = [
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
    		style_cell={'textAlign': 'left'},
                data = df.to_dict('records'),
                # editable = True,
                filter_action = "native",
                sort_action = "native",
                sort_mode = "multi",
                # column_selectable = "single",
                # row_selectable = "multi",
                # row_deletable = True,
                selected_columns = [],
                selected_rows = [],
                page_action = "native",
                # page_current= 0,
                # page_size= 10,
            )
        ]),
        html.Div(id = 'page-content', className = 'content', children = [
            "Source : ",
            html.Br(),
            html.A("Script de listing des données Insee", href = "https://gitlab.com/jdlom/data_insee", target='_blank'),
            html.Br(),
            html.A("Code pour cette interface", href = "https://github.com/tescrihuela/dashboard_insee_scrap", target='_blank'),
        ])
    ]
)


######
# Main
if __name__ == '__main__':
    app.run_server(debug = True)

