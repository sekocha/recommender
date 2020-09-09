# Recommender system database for finding unknown inorganic compounds

The present tensor-based recommender system database provides currently unknown chemically relevant compositions from database entries (ICSD, ICDD, and Springer Materials). 
If you use the recommender system database for academic purposes, please cite the following article [1].

[1] [A. Seko, H. Hayashi, H. Kashima and I. Tanaka, "Matrix- and tensor-based recommender systems for the discovery of currently unknown inorganic compounds", Phys. Rev. Materials 2, 013805 (2018)](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013805) 


## Examples
```
$(recommender)/recommender.py -e N -n 4 --type ionic -d recommender-2020-09-09.sqlite
$(recommender)/recommender.py -e Al Ga O -n 5 --type ionic -d recommender-2020-09-09.sqlite
$(recommender)/recommender.py -e Mg Zn -n 2 3 --type alloy -d recommender-2020-09-09.sqlite
$(recommender)/recommender.py -e Mg Zn -n 2 3 --type alloy --nmax 100 --threshold 0.05 -d recommender-2020-09-09.sqlite
$(recommender)/recommender.py -e Mg Sn -n 4 5 --type ionic --nmax 10 --threshold 0.2 -d recommender-2020-09-09.sqlite
```
## Default parameters
- elements: None
- n (number of atomic species): 3
- type: ionic
- threshold: 0.01
- nmax: None

```
usage: recommender.py [-h] [-d DATABASE] [-n [NARY [NARY ...]]]
                      [-e [ELEMENTS [ELEMENTS ...]]] [-t {ionic,alloy}]
                      [--threshold THRESHOLD] [--nmax NMAX]

optional arguments:
  -h, --help            show this help message and exit
  -d DATABASE, --database DATABASE
                        Database name
  -n [NARY [NARY ...]], --nary [NARY [NARY ...]]
                        Number of atomic species in recommended compositions
  -e [ELEMENTS [ELEMENTS ...]], --elements [ELEMENTS [ELEMENTS ...]]
                        Elements in recommended compositions
  -t {ionic,alloy}, --type {ionic,alloy}
                        Database type for recommendation
  --threshold THRESHOLD
                        Score threshold for recommendation
  --nmax NMAX           Maximum number of recommended compositions
```
