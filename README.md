# htmap_gt_loops

This repo provides corrected Ground Truth loop closure files for the following datasets:
- [St Lucia](loops_sl.csv)
- [CityCentre combined](loops_cc.csv)
- KITTI 
  -  [00](loops_k00.csv)
  -  [05](loops_k05.csv)
  -  [06](loops_k06.csv)

Corrected a number of erroneous entries in the loop closure matrices of CC and KITTI provided by Arroyo et al 2014. 

Python utility functions are provided in [utils.py](utils.py) to 
- read the provided csv files into pandas dataframes
- convert delimited range string to text and vice-versa.
