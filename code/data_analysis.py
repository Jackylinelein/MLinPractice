#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:01:20 2021

@author: Hendrik Timm
"""

# plotting with matplotlib
import pickle
from matplotlib import pyplot as plt
import numpy as np


# create graphs for every extracted feature
def plot():
    
    plot_str = "No"
    plot_str = input("Do you want to plot the given features in different plots? Answer with 'Yes' or 'No'")
    if(plot_str !="Yes"):
        print("Not plotting graphs")
    else:
        
        print("Plotting graphs")
        with open("data/feature_extraction/training.pickle", "rb") as f_in:
            data = pickle.load(f_in)
            labels = data["labels"]
      
            for i in range(len(data["feature_names"])):
                
                # get feature names for x-axis
                x_axis = data["feature_names"][i]
                # get one feature after another by slicing whole data
                feature = data["features"][:, i:i+1]
                
                
                # only tweets with positive labels
                pos = feature[labels]
                neg_index = np.array([not x for x in labels])
                # only tweets with negative labels
                neg = feature[neg_index]
           
                
                # get min and max value in order to create an array of the correct size
                max_value = (int)(max(feature)[0])
                min_value = (int)(min(feature)[0])
               
                
                # set baseline (0.0918 of all tweets are viral)
                baseline =  pos.size/feature.size
                baseline_array = np.full((max_value-min_value+1),baseline)
                
                # store amount of viral tweets for a certain x value
                viral_tweets = np.zeros((max_value-min_value+1))
                
                # store x value here
                only_x = np.zeros((max_value-min_value+1))
                
                # go through all possible values within min and max
                for i in range(max_value-min_value+1):
                    
                    # count how many viral and not viral tweets there are for this value i+min_value
                    viral = np.count_nonzero(pos == min_value + i)
                    lame = np.count_nonzero(neg == min_value + i)
                    
                    if(viral+lame>0):
                        viral_tweets[i] = viral/(lame+viral)
                    
                    only_x[i] = min_value+i
                    
                # plot three graphs:
                    
                # percentage of viral tweets within a certain feature number
                y_axis = "Percentage of viral tweets"    
                plt.plot(only_x, viral_tweets, color='green', label = 'viral tweets')
                plt.plot(only_x, baseline_array, color = 'red', label='baseline')
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                plt.legend()
                plt.savefig("plots/viral_percent_" + x_axis + ".png")
                plt.show()
                
     
                
                # percentage of tweets (viral, not viral, all) w.r.t. feature 
                y_axis = "Percentage of all tweets"
                plt.hist(feature,  weights =np.zeros_like(feature)+1. /feature.size, label="all tweets", color='blue')
                plt.hist(neg, weights =np.zeros_like(neg)+1. /feature.size, color = 'red', label = "not viral tweets")
                plt.hist(pos, weights =np.zeros_like(pos)+1. /feature.size ,color = 'green', label="viral tweets")
                
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                plt.legend()
                plt.savefig("plots/tweets_percent_" + x_axis + ".png")
                plt.show()
                
                # total amount of tweets (viral, not viral, all) w.r.t. feature
                y_axis = "Number of Tweets"
                plt.hist(feature, color='blue',label="all tweets")
                plt.hist(neg, color='red', label="not viral tweets")
                plt.hist(pos, color='green', label= "viral tweets")
                plt.legend()
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                plt.savefig("plots/tweets_total_" + x_axis + ".png")
                plt.show()
                
    
    
    
    
