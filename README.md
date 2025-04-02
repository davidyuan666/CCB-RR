# CCB-RR: Code Context-Based Reviewer Recommendation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://img.shields.io/badge/DOI-10.1007%2Fs11704--023--3256--9-9cf)](https://doi.org/10.1007/s11704-023-3256-9)
[![Paper PDF](https://img.shields.io/badge/📄_Paper-PDF-red)](https://journal.hep.com.cn/fcs/EN/10.1007/s11704-023-3256-9)
[![Dataset](https://img.shields.io/badge/📁_Dataset-Figshare-important)](https://figshare.com/articles/online_resource/CCB_RR_zip/21434232)

## 📑 Publication 
📌 ​**Title**: Code context-based reviewer recommendation  
🏛 ​**Journal**: [Frontiers of Computer Science](https://journal.hep.com.cn/fcs/) (SCI-indexed)  
📅 ​**Year**: 2025  
🔗 ​**DOI**: [10.1007/s11704-023-3256-9](https://doi.org/10.1007/s11704-023-3256-9)  

## 🗃️ Dataset Access
The benchmark dataset is available on Figshare:  
📂 [CCB-RR Dataset](https://figshare.com/articles/online_resource/CCB_RR_zip/21434232)  
(DOI: [10.6084/m9.figshare.21434232](https://doi.org/10.6084/m9.figshare.21434232))

## Features
- Context-aware reviewer recommendation for code changes
- Integration with version control systems
- Support for multiple programming languages


## Abstract
Code review is a critical process in software development. We introduce CCB-RR, a model that leverages information from changesets to recommend the most suitable reviewers. The model achieved Top-1 accuracy of 60%, 55%, 51%, and 45% on Android, OpenStack, QT, and LibreOffice projects respectively.

## Requirements
* Python==3.7  
* PyTorch==1.6.0  
* numpy==1.16.3  
* tqdm==4.48.2

## Project Structure
* ```attention/```: Self-attention network and submodule networks
* ```method/```: Joint representation for file path, source files, and textual information
* ```configs.py```: Basic configuration for the attention and method folder
* ```datasets.py```: Dataset loader
* ```train.py```: Train and validate representation models
* ```utils.py```: Utilities for models and training
* ```revfinder_baseline_reimplement.py```: Implementation of RevFinder
* ```rstrace_implement.py```: Implementation of RSTrace
* ```wrc_reimplement.py```: Preprocess contextual information of pull request
* ```Textual.py```: Preprocess pull request information and generate vocabulary
* ```FilePath.py```: Preprocess file path information
* ```Contextual.py```: Preprocess contextual information of pull request

## Usage

### Configuration
Edit hyper-parameters and settings in ```config.py```

### Training

```
python train.py --mode train
```


### Evaluation 

```
python train.py --mode eval
```


### Run Baselines
```
python wrc_reimplement.py
python revfinder_baseline_reimplement.py
python rstrace_implement.py
```


## Citation
If you use this code in your research, please cite our paper:

```bibtex
@article{yuan2025code,
title={Code context-based reviewer recommendation},
author={Yuan, Dawei and Peng, Xiao and Chen, Zijie and Zhang, Tao and Lei, Ruijia},
journal={Frontiers of Computer Science},
volume={19},
number={1},
pages={191202},
year={2025},
publisher={Higher Education Press}
}
```


## License
This project is licensed under the MIT License - see the LICENSE file for details.

