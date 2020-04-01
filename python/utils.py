import math as m
import numpy as np
from scipy.spatial import cKDTree


def match_etaphi(ref_etaphi, trigger_etaphi, trigger_pt, deltaR=0.2):
    '''Match objects within a given DeltaR. Returns the panda index of the best match (highest-pt)
       and of all the matches'''
    # print "INPUT ref_etaphi"
    # print ref_etaphi
    # print "INPUT trigger_etaphi"
    # print trigger_etaphi
    # print "INPUT trigger_pt"
    # print trigger_pt
    #print "deltaR: ", deltaR
    kdtree = cKDTree(trigger_etaphi)
    best_match_indices = {}
    all_matches_indices = {}
    # for iref,(eta,phi) in enumerate(ref_etaphi):
    for index, row in ref_etaphi.iterrows():
        matched = kdtree.query_ball_point([row.eta, row.phi], deltaR)
        # not this in an integer of the index of the array not the index in the pandas meaning: hence to beused with iloc
        # Handle the -pi pi transition
        matched_sym = kdtree.query_ball_point([row.eta, row.phi-np.sign(row.phi)*2.*m.pi], deltaR)
        matched = np.unique(np.concatenate((matched, matched_sym))).astype(int)
        # print matched
        # print type(matched)
        # print trigger_pt[matched]
        # print trigger_etaphi.iloc[matched]
        # Choose the match with highest pT
        if (len(matched) != 0):
            best_match = np.argmax(trigger_pt.iloc[matched])
            best_match_indices[index] = best_match
            all_matches_indices[index] = trigger_pt.iloc[matched].index.values
    # print best_match_indices
    # print all_matches_indices
    return best_match_indices, all_matches_indices


def debugPrintOut(level, name, toCount, toPrint):
    if level == 0:
        return
    if level >= 3:
        print('# {}: {}'.format(name, len(toCount)))
    if level >= 4 and not toPrint.empty:
        print(toPrint)
