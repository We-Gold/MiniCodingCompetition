import pandas as pd

def parse_data():
    dataframe = pd.read_csv("data.csv")

    school_publications = dataframe.set_index("name")["numPublished"].to_dict()
    school_cit_score = dataframe.set_index("name")["citScore"].to_dict()
    school_placements = dataframe.set_index("name")["placement"].to_dict()

    names = dataframe["name"].tolist()

    return school_publications, school_cit_score, school_placements, names