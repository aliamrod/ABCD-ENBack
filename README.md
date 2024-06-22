# ABCD-normalization


## Overview

Data from multisite magnetic resonance imaging (MRI) studies contain variance attributable to the scanner that can reduce statistical power and potentially bias results if not appropriately managed. ABCD Study is a prospective longitudinal study starting at the ages of 9-10 and following participants for 10 years. These scans are acquired on 29 different scanners of 5 different model types manufactured by 3 different vendors (request access at: https://nda.nih.gov/abcd/).

The ABCD study is a collection of neuroimaging, neurocognitive, genetic, physiological, psychosocial, and other behavioral data from ~12,000 sociodemographically diverse youth recruited from 9-10 years of age, from across the USA, to investigate the host of factors that may affect adolescent health. The provision of these data alongside comprehensive demographic and behavioral measures make for a low “cost of entry” for any researcher to conduct statistical analyses on the ABCD cohort or any sub-population therein. However, such investigators must be cognizant of the potentially confounding effects of different scanners on the neuroimaging measures. As a commitment to open and reproducible science, data from the ABCD Study is publicly available for users to access, further highlighting the importance of addressing the responsible use of these data, as well as the perpetuation and reproduction of narratives and practices that impact historically minoritized populations as a result of their misuse. 



To that end, we have created this simple-to-use tool to enable investigators to "harmonize" the data - that is: to remove scanner induced variance present in the data while preserving the biological variability in the sample.






## Methods

* Emotional n-back task consisted of **160 trials divided into 2 runs. The task was performed in the scanner while collecting functional magnetic resonance imaging data.

* Each run consisted of 8 blocks, each with 10 trials. For each trial, the objective was to decide whether the current stimulus matched a target stimulus (Figure 01).

* In the 0-back condition, the target stimulus is presented before the first trial in each block and participants are asked to decidde whether the current stimulus matches the target stimulus.

* In the 2-back condition, participants respond whether the stimulus on the current trial match the stimulus presented 2 trials back.

* The stimulus and target matched in 20% of the trials. For the remaining trials, the stimulus did not match the target, and the stimulus on the current trial either had (lure, 25% of trials) or had not (nonlure, 55%) been presented earlier in the block.





![image](https://github.com/aliamrod/ABCD-ENBack/assets/62684338/09a63ecd-2085-474d-b4d5-55e74857e6a9)


Figure 01. 




### References

[1] "Computational Modeling of the n-Back Task in the ABCD Study: Association of Drift Diffusion Model Parameters to Polygenic Scores of Mental Disorders and Cardiometabolic Diseases". 




[1] "_ABCD_Harmonizer: An Open-source Tool for Mapping and Controlling for Scanner Induced Variance in the Adolescent Brain Cognitive Development Study_". Date of Access: 17 June, 2024. 

[2] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6981278/

[3]

[4] https://www.sciencedirect.com/science/article/pii/S2451902222000787#sec1.5.5 

[5]

