import streamlit as st

import plotly.express as px

import pandas as pd

from minicodingcompetition.parse_data import *

st.write(
    """
# CS Compass

Select Two University Programs to Compare
"""
)

school_publications, school_cit_score, school_placements, name = parse_data()


def createRadarPlot(data):
    # Create a radar chart using Plotly Express
    fig = px.line_polar(data, r='Value', theta='Category', line_close=True)

    # Display the radar chart
    st.plotly_chart(fig)

schools = name

chosen_schools = st.multiselect(
    'Select 2 universities',
    schools,
    [name[0], name[1]],
    max_selections=2)

if len(chosen_schools) != 2:
    st.write("Please select 2 universities.")
else:
    # Papers Published	Citation Score	Placements
    data_categories = ["Publications", "Citation Score", "Placements"]

    scalars = [150, 100, 100]

    # show the radar for the first school
    st.write("## " + chosen_schools[0] + ": Radar Chart")
    values0 = [school_publications[chosen_schools[0]] / scalars[0],
                school_cit_score[chosen_schools[0]] / scalars[1],
                school_placements[chosen_schools[0]] / scalars[2]]
    createRadarPlot({"Category": data_categories, "Value": values0})

    # show radar for second school
    st.write("## " + chosen_schools[1] + ": Radar Chart")
    values1 = [school_publications[chosen_schools[1]] / scalars[0],
                school_cit_score[chosen_schools[1]] / scalars[1],
                school_placements[chosen_schools[1]] / scalars[2]]
    createRadarPlot({"Category": data_categories, "Value": values1})

    selected_school_publications = pd.Series({key: school_publications[key] for key in chosen_schools})
    selected_school_cit_score =  pd.Series({key: school_cit_score[key] for key in chosen_schools})
    selected_school_placements =  pd.Series({key: school_placements[key] for key in chosen_schools})

    st.write("### Number of Publications Per School")
    st.bar_chart(selected_school_publications)

    st.write("### Citation Score")
    st.bar_chart(selected_school_cit_score)

    st.write("### PhD Student Placements")
    st.bar_chart(selected_school_placements)