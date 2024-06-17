# ABCD-normalization


## Overview

Data from multisite magnetic resonance imaging (MRI) studies contain variance attributable to the scanner that can reduce statistical power and potentially bias results if not appropriately managed. ABCD Study is a prospective longitudinal study starting at the ages of 9-10 and following participants for 10 years. ` The ABCD study is a collection of neuroimaging, neurocognitive, genetic, physiological, psychosocial, and other behavioral data from ~12,000 sociodemographically diverse youth recruited from 9-10 years of age, from across the USA, to investigate the host of factors that may affect adolescent health. Enrollment to the ABCD Study occurred between 2018 and 2018, with annual visits of participants for up to 10 years. As a commitment to open and reproducible science, data from the ABCD Study is publicly available for users to access, further highlighting the importance of addressing the responsible use of these data, as well as the perpetuation and reproduction of narratives and practices that impact historically minoritized populations as a result of their misuse. 


## 


$${\color{blue}These scans are acquired on 29 different scanners of di}$$
 The Adolescent Cognitive Brain Development (ABCD) study is an ongoing, longitudinal neuroimaging study acquiring data from over 11,000 children starting at 9-10 years of age. These scans are acquired on 29 different scanners of 5 different model types manufactured by 3 different vendors. Publicly available data from the ABCD study include structural MRI (sMRI) measures such as cortical thickness and diffusion MRI (dMRI) measures such as fractional anisotropy. In this work, we 1) quantify the variance attributable to scanner effects in the sMRI and dMRI datasets, 2) demonstrate the effectiveness of the data harmonization approach called ComBat to address scanner effects, and 3) present a simple, open-source tool for investigators to harmonize image features from the ABCD study. Scanner-induced variance was present in every image feature and varied in magnitude by feature type and brain location. For almost all features, scanner variance exceeded variability attributable to age and sex. ComBat harmonization was shown to effectively remove scanner induced variance from all image features while preserving the biological variability in the data. Moreover, we show that for studies examining relatively small subsamples of the ABCD dataset, the use of ComBat harmonized data provides more accurate estimates of effect sizes compared to controlling for scanner effects using ordinary least squares regression.

