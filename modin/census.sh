#!/bin/bash

conda deactivate
conda create --name intel-aikit-modin -c intel/label/oneapibeta -c intel -c conda-forge 

#runipy intel-aikit-modin=2021.1b10

conda activate intel-aikit-modin

python -m pip install runipy
python -m pip install modin
python -m pip install ipykernel
python -m ipykernel install --name intel-aikit-modin --display-name "intel-aikit-modin"
conda run -n intel-aikit-modin python3 -m ipykernel install --name intel-aikit-modin --display-name imodin   
#jupyter kernelspec uninstall intel-aikit-modin