import ROOT
import pandas as pd
import python.selections as selections

version = 'v76t'


def get_label_dict(selections):
    dictionary = {}
    for sel in selections:
        dictionary[sel.name] = sel.label
    return dictionary


# -------------------------------------------------------------------------

samples_ele = [
    Sample('ele_flat2to100_PU0', 'PU0', version, 'ele'),
    Sample('ele_flat2to100_PU200', 'PU200', version, 'ele')
    ]

samples_ele_V8 = [
    Sample('ele_flat2to100_PU0', 'PU0', version, 'V8'),
    Sample('ele_flat2to100_PU200', 'PU200', version, 'V8')
    ]


samples_ele_V9 = [
    Sample('all_flat5to80_PU0', 'PU0', 'v75t', 'V9'),
    Sample('all_flat5to80_PU200', 'PU200', 'v75t', 'V9')
    ]

samples_photons = [
    Sample('photon_flat8to150_PU0', 'PU0', version, 'photon'),
    Sample('photon_flat8to150_PU200', 'PU200', version, 'photon')
    ]

samples_pions = [
    Sample('pion_flat2to100_PU0', 'PU0', version, 'pions'),
    ]

samples_nugus = [
    Sample('nugun_alleta_pu0', 'PU0', version, 'mb'),
    Sample('nugun_alleta_pu200', 'PU200', version, 'mb')
    ]

samples_nugunrates = [
    Sample('nugun_alleta_pu200', 'PU200', version, 'mb')
    ]

samples_nugunrates_V8 = [
    Sample('nugun_alleta_pu200', 'PU200', version, 'V8')
    ]

samples_nugunrates_V9 = [
    Sample('nugun_alleta_pu200', 'PU200', version, 'V9')
    ]

all_tpsets = {'DEF': 'dRC3d',
              'DEFCalib': 'NNDR Calib v1',
              'DEFNC': 'dRC3d + new Th',
              'HMvDR': 'HistoMaxC3d + dR(layer)',
              'HMvDRNC0': 'HMC3d+dR(layer)+NC0',
              'HMvDRNC1': 'HMC3d+dR(layer)+NC1',
              'EG': 'EG',
              'TkEG': 'TkEG',
              'TkEle': 'TkEle',
              'TkIsoEle': 'TkIsoEle',
              'L1Trk': 'L1Track'}
