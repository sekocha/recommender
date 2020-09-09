# Recommender system database for finding unknown inorganic compounds

The present tensor-based recommender system database provides currently unknown chemically relevant compositions from database entries (ICSD, ICDD, and Springer Materials). 
If you use the recommender system database for academic purposes, please cite the following article [1].

[1] [A. Seko, H. Hayashi, H. Kashima and I. Tanaka, "Matrix- and tensor-based recommender systems for the discovery of currently unknown inorganic compounds", Phys. Rev. Materials 2, 013805 (2018)](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.013805) 


## Examples
```
> $(recommender)/recommender.py -e Al Si O -n 4 -t ionic --nmax 20 -d recommender-2020-09-09.sqlite
 # composition, score
  Al2Ba2O7Si1   0.74232
  Al2O12Si3Zn3   0.4814
  Al1Li1O12Si5   0.41613
  Al2Ba3O14Si4   0.39355
  Al2O14Si4Sr3   0.34611
  Al2La2O7Si2   0.29978
  Al1O10Rb1Si4   0.29434
  Al1Li17O20Si5   0.28859
  Al3O16Rb3Si5   0.27276
  Al2O12Pb3Si3   0.2638
  Al1O4Si1Sr1   0.24765
  Al1La1O7Si2   0.24091
  Al2Ni3O12Si3   0.23918
  Al1Ba1O4Si1   0.23488
  Al2Ca3O14Si4   0.23044
  Al4Cd2O18Si5   0.22631
  Al1K1O12Si5   0.21797
  Al2Mn3O8Si1   0.21206
  Al1O13Si2Y5   0.2119
  Al4Ni2O18Si5   0.20939
```

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

![image](ps3nitrides-map1.png)
