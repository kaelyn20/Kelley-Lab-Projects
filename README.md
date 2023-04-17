# Kelley-Lab-Projects
Programs and projects created during SDSU Master's Program in Dr. Kelley's lab


## Built Environment
This file encompases the code and data used for the thesis "Effect of Site Productivity and Disturbance on Microbial Compositions in the Built Environment."

This folder consists of the QIIME code (QIIME_Analysis.ipynb) used in the analysis to demultiplex, denoise, and filter the raw data, as well as calculate diversity metrics. From this, multiple files were created and then exported:

1. 16S-features.tsv: A 16S OTU table with the individual sequence variants (SVs) representing the taxa
2. 16S-taxatable.tsv: A 16S OTU table with genus level taxonomic classification
3. itsfeaturetable.tsv: An ITS OTU table with SVs representing the taxa
4. itstaxatable.tsv: An ITS OTU table with genus level taxonomic classification
5. chao1_16S.tsv, evenness16S.tsv, faithspd16S.tsv, shannon16S.tsv: 16S alpha diversity metrics
6. chao1_its.tsv, evennessits.tsv, shannonits.tsv: ITS alpha diversity metrics
7. unweighted_unifrac.tsv: 16S unweighted UniFrac distance matrix

Additionally, the clean_file.py script cleans up the 16S and ITS genus OTU tables by separating taxanomic groups. 

The be_analysis.Rmd file is the file used for statistical analyses for bacterial and fungal biomass, overall activity of the system (measured by ATP), community composition, important feature selection (via randomForest), taxa abundances, and alpha diversity.

The PCR_Couponbook2.csv file is the metadata file.
