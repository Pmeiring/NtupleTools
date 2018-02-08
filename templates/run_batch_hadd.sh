#!/bin/bash

CLUSTERID=$1
PROCID=$2

echo "Runnin Cluster ${CLUSTERID} Job ${PROCID}"
BATCH_DIR=${PWD}
echo "Current dir: ${BATCH_DIR}"
cd TEMPL_WORKDIR
echo "Now in dir: ${PWD}"

hostname

source ./setup_lxplus.sh
source ~/scripts/setVirtualEnvWrapper.sh
workon HGCTPGPerformance-1

cd ${BATCH_DIR}
date
hadd TEMPL_OUTFILE TEMPL_INFILES
#mv TEMPL_OUTFILE TEMPL_OUTDIR