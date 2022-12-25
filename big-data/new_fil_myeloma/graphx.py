#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


def main():

    # Exctract dictionary from dataframe of nodes
    nodes_elab_file = pd.read_csv("./nodes_elab.csv", sep=";")
    nodes_elab_filtered = nodes_elab_file[["new_id","names"]]

    dictionary_index = {}

    for index, row in nodes_elab_filtered.iterrows():
        dictionary_index[ row['names'] ] = row['new_id']
    

    # Create new column id into edges_elab.csv
    edges_elab_file = pd.read_csv("./edges_elab.csv", sep=";")
    edges_elab_filtered = edges_elab_file[["src:START_ID","dst:END_ID"]]

    list_src_id = []
    list_dst_id = []

    for index, row in edges_elab_filtered.iterrows():
        # Create id for src:START_ID
        if row['src:START_ID'] in dictionary_index:
            list_src_id.append(dictionary_index[ row['src:START_ID'] ])
        else:
            id_ = len(dictionary_index)+1
            dictionary_index[ row['src:START_ID'] ] = id_
            list_src_id.append(dictionary_index[ row['src:START_ID'] ])

        # Create id for dst:END_ID
        if row['dst:END_ID'] in dictionary_index:
            list_dst_id.append(dictionary_index[ row['dst:END_ID'] ])
        else:
            id_ = len(dictionary_index)+1
            dictionary_index[ row['dst:END_ID'] ] = id_
            list_dst_id.append(dictionary_index[ row['dst:END_ID'] ])

    
    edges_elab_file["src:START_ID_int"] = list_src_id
    edges_elab_file["dst:END_ID_int"] = list_dst_id
    
    print(edges_elab_file.head())

    edges_elab_file.to_csv("./new/edges_elab.csv", sep=";")

    return 0



if __name__ == "__main__":
    main()