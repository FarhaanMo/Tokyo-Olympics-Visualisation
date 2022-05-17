# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from tkinter import font
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__,  suppress_callback_exceptions=True)


# Importing data from excel files.
entries_gender_df = pd.read_excel("./EntriesGender.xlsx")
medals_df = pd.read_excel("./Medals.xlsx")


# Scatter Plot for the medals won by the country with their respective ranks.
fig = px.scatter(medals_df, x="Total", y="Rank",size="Total", color="Team/NOC",hover_name="Team/NOC", log_x=True, size_max=60, title="Rank of the Country vs The Medals Won by the Country : ")

# Bar plot for the number of participants in each discipline.
fig2 = px.bar(entries_gender_df, x="Discipline", y="Total", color="Discipline", title="Total participants in each Discipline : ")



# Including tabs for Medals of a Country and the Participants in a Discipline of sport
app.layout = html.Div( children=[
    html.Div(children=[

        html.H1(className='heading', 
            children='TOKYO OLYMPIC AWARDS',
        ),

        html.Div(className='subheading', 
            children='Visualizing Awards won  and the Number of Participants at The Tokyo Olympics.'
        ),

       
        dcc.Tabs(id='tabs-example-1', value='tab-1',  parent_className='custom-tabs', className='custom-tabs-container', children=[
            dcc.Tab(label='Medals and Ranks of a Country', value='tab-1',className='custom-tab', selected_className='custom-tab--selected'),
            dcc.Tab(label='Participants in a Discipline of sport ', value='tab-2',className='custom-tab', selected_className='custom-tab--selected'),
        ]),

        html.Div(id='tabs-example-content-1'),
        
    ]),

])


# Callback for tabs
@app.callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs-example-1', 'value')
)

# Setting dropdowns which include gold, silver, bronze and all medals won by countries for tab1 
# Setting dropdowns which include male, female and all participants who participated in a discipline of sport for tab2.
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([

            html.Div(className='subheading1', 
               children='Visualizing the Medals won by the Country and their respective Rank:'
            ),

            html.Label('Select  Medal : ', className='label1' 
            ),

            dcc.Dropdown(['All Medals', 'Gold', 'Silver', 'Bronze'], 
                'All Medals', id='dropdownone'
            ),

            dcc.Graph(
                id='rvt_graph',
                figure=fig
            ),
            
            html.Div(className='plot1', 
                children='* This plot shows that USA has Biggest Circle Size and has Rank One with Maximum Total Medals.'
            ),

            html.Div(className='plot2', 
                children='* Where as Syria, Turkmenistan, Puerto Rico have the Least Rank with the Least Total Medals and the Smallest Circle Size.'
            ),
                
        ])
    elif tab == 'tab-2':
        return html.Div([

            html.Div(className='subheading1', 
                children='Visualizing the Number of Participants in each Discipline of Sport:'
            ),
            html.Label('Select  Gender : ' , className='label2'
            ),

            dcc.Dropdown(['All Genders', 'Male', 'Female'],    
                'All Genders', id='dropdowntwo'
            ),  

            dcc.Graph(
                id='p_graph',
                figure=fig2
            ),

            html.Div(className='plot1', 
                children='* This plot shows that the ATHELETICS Discipline has the Maximum Number of Participants in both Male and Female Categories.  '
            ),

            html.Div(className='plot2', 
                children='* Where as the CYCLING Discipline has the Minimum Number of Participants in both Male and Female Categories.'
            ),

        ])

# callback for medals
@app.callback(
    Output('rvt_graph', 'figure'),
    Input('dropdownone', 'value'))
def update_figure(selected_medal):
    if selected_medal == 'All Medals':
        fig = px.scatter(medals_df, x="Total", y="Rank",size="Total", color="Team/NOC",hover_name="Team/NOC", log_x=True, size_max=60, title="Rank of the Country vs The Medals Won by the Country : ")
    elif selected_medal == 'Gold':
        fig = px.scatter(medals_df, x="Gold", y="Rank",size="Total", color="Team/NOC",hover_name="Team/NOC", log_x=True, size_max=60, title="Rank of the Country vs The Medals Won by the Country : ")
    elif selected_medal == 'Silver':
        fig = px.scatter(medals_df, x="Silver", y="Rank",size="Total", color="Team/NOC",hover_name="Team/NOC", log_x=True, size_max=60, title="Rank of the Country vs The Medals Won by the Country : ")     
    else :
        fig = px.scatter(medals_df, x="Bronze", y="Rank",size="Total", color="Team/NOC",hover_name="Team/NOC", log_x=True, size_max=60, title="Rank of the Country vs The Medals Won by the Country : ") 
    return fig


# callback for number of participants
@app.callback(
    Output('p_graph', 'figure'),
    Input('dropdowntwo', 'value'))
def update_figure(selected_medal):
    if selected_medal == 'All Genders':
        fig2 = px.bar(entries_gender_df, x="Discipline", y="Total", color="Discipline", title="Number of participants in each Discipline : ")
    elif selected_medal == 'Male':
        fig2 = px.bar(entries_gender_df, x="Discipline", y="Male", color="Discipline", title="Number of participants in each Discipline : ")
    else :
        fig2 = px.bar(entries_gender_df, x="Discipline", y="Female", color="Discipline", title=" Number of participants in each Discipline : ")
    return fig2


if __name__ == '__main__':
    app.run_server(debug=False)