# Kelley-Lab-Projects
Programs and projects created during SDSU Master's Program in Dr. Kelley's lab


## Built Environment
This file encompases the code and data used for the thesis "Effect of Site Productivity and Disturbance on Microbial Compositions in the Built Environment."

This folder consists of the QIIME code (QIIME_Analysis.ipynb) used in the analysis to demultiplex, denoise, and filter the raw data, as well as calculate diversity metrics. From this, multiple files were created and then exported:

1. 16S_repseqs.qzv: A QIIME visualization with the individual 16S seqeuence variants (SVs) and their corresponding sequences
2. ITS_repseqs.qzv: A QIIME visualization with the individual ITS SVs and their corresponding sequences
3. 16S_hash_taxa.tsv: A 16S tsv file matching the SV hash code to it's taxonomic classification
4. ITS_hash_taxa.tsv: A ITS tsv file matching the SV hash code to it's taxonomic classification
5. 16S-features.tsv: A 16S OTU table with the individual sequence variants representing the taxa
6. 16S-taxatable.tsv: A 16S OTU table with genus level taxonomic classification
7. itsfeaturetable.tsv: An ITS OTU table with SVs representing the taxa
8. itstaxatable.tsv: An ITS OTU table with genus level taxonomic classification
9. chao1_16S.tsv, evenness16S.tsv, faithspd16S.tsv, shannon16S.tsv: 16S alpha diversity metrics
10. chao1_its.tsv, evennessits.tsv, shannonits.tsv: ITS alpha diversity metrics
11. unweighted_unifrac.tsv: 16S unweighted UniFrac distance matrix

Additionally, the clean_file.py script cleans up the 16S and ITS genus OTU tables by separating taxanomic groups. 

The be_analysis.Rmd file is the file used for statistical analyses for bacterial and fungal biomass, overall activity of the system (measured by ATP), community composition, important feature selection (via randomForest), taxa abundances, and alpha diversity.

The PCR_Couponbook2.csv file is the metadata file.
