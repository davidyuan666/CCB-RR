# Have moved to Figshare website https://figshare.com/articles/online_resource/CCB_RR_zip/21434232

# CCB-RR
Code Context-Based Reviewer Recommendation

# Dependency
* Python==2.7  
* PyTorch==1.6.0  
* numpy==1.16.3  
* tqdm ==4.48.2

# Code Structure
* ```attention```: Self-attention network and submodule networks.
* ```method```: Joint Representation for file path, source files, and textual information.
* ```configs.py```: Basic configuration for the attention and method folder. Each function defines the hyper-parameters for the corresponding model.
* ```datasets.py```: Dataset loader.
* ```train.py```: Train and validate representation models.
* ```utils.py```: Utilities for models and training.
* ```revfinder_baseline_reimplement.py```: implementation of revfinder.
* ```rstrace_implement.py```: implementation of rstrace.
* ```wrc_reimplement.py```: Preprocess the contextual information of pull request.
* ```Textual.py```: Preprocess the pull request information and generate vocabulary.
* ```FilePath.py```: Preprocess the file path information.
* ```Contextual.py```: Preprocess the contextual information of pull request.
# Usage
## Data


## Configuration
Edit hyper-parameters and settings in ```config.py```  

## Train
>python train --mode train

## Eval
>python train --mode eval

## Run Baseline
>python wrc_reimplement.py

>python revfinder_baseline_reimplement.py

>python rstrace_implement.py

