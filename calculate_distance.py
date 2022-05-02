#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:43:52 2022

@author: james
"""

import json
import numpy as np
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='Calculates forward association strength')

parser.add_argument('--cue', type=str, default = None,
                    help='cue word to test')
parser.add_argument('--response', type=str, default = None,
                    help='response word to test')
parser.add_argument('--cue_response_input_file', '-i', type=str,
                    help='path to file containing ues and responses to test')
parser.add_argument('--norms', type=str, default = "all",
                    help='which norms to use. Current options are "usffan","eat", or "all".')

args = parser.parse_args()
    

def get_fas(dict_list,cue,response):
    cue = cue.upper()
    response = response.upper()
    
    if cue==response:
        fas = 1
    
    else:
        total_respones = 0
        responses = 0
        for dictionary in dict_list:
            if cue in dictionary:
                total_respones += float(dictionary[cue]["_count"])
                if response in dictionary[cue]:
                    responses += float(dictionary[cue][response]["_count"])
        
        if total_respones ==0:
            fas = None
        else:
            fas = responses/total_respones
        
        
    return fas

def get_fas_file(dict_list,cue_response_input_file):
    input_csv = pd.read_csv(cue_response_input_file)
    input_name_split = cue_response_input_file.split(".")
    output_name = ".".join(input_name_split[:-1]+["output"]+input_name_split[-1:])
    
    csv_length = input_csv.shape[0]
    fas_dataframe = pd.DataFrame(columns = ["Cue","Response","FAS"])
    for i in range(csv_length):
        cue = input_csv.loc[i,"Cue"]
        response = input_csv.loc[i,"Response"]
        fas = get_fas([usffan_dict],cue,response)
        current_df_row = pd.DataFrame({
            "Cue":[cue],
            "Response":[response],
            "FAS":[fas]})
        fas_dataframe = pd.concat([fas_dataframe,current_df_row],ignore_index=True)
    fas_dataframe.reset_index().to_csv(output_name,index=False)
    print("Successfully produced output file: {}".format(output_name))
        

if __name__ == "__main__":
    
    
    with open('usffan_dict.json', 'r') as f:
        usffan_dict = json.load(f)
    
    with open('eat_dict.json', 'r') as f:
        eat_dict = json.load(f)
        
    if args.norms=="all":
        norms_list = [usffan_dict,eat_dict]
    elif args.norms=="usffan":
        norms_list = [usffan_dict]        
    elif args.norms=="eat":
        norms_list = [eat_dict]   

    if len(norms_list)>0:
        if not args.cue_response_input_file==None:
            get_fas_file(norms_list,args.cue_response_input_file)
        else:
            fas = get_fas(norms_list,args.cue,args.response)
            print("Cue: {0}\tResponse: {1}\tFAS: {2}".format(args.cue,args.response,fas))
    else:
        print("Invalid norms")