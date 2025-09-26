# Random Processes & Probability

## 1. Illustration of Concepts

During normalization procedure, subtracting the mean brings the datapoints to be centered around zero and reduces the mean to zero. In the context of deep learning, most activation functions have their strongest gradients around x = 0 and hence centering the datapoints in a dataset around zero would speed-up the learning.

### 1.1. Mean Normalization

Mean normalization of N-dimensional dataset is implemented in the source code with insightful comments included as necessary. For simplicity, first two features (i.e. first two dimensions of the dataset) are scatter plotted to illustrate mean normalization.

![Mean Normalization](random_process_results/mean_normalization.png)

### 1.2. Standardization

Standardization of N-dimensional dataset is implemented in the source code with insightful comments included as necessary. For simplicity, first two features (i.e. first two dimensions of the dataset) are scatter plotted to illustrate standardization. Then, all the features containing 'N' datapoints (also known as training examples) in both original and standardized datasets are plotted for illustration. Lastly, the distribution of all features in both original and standardized datasets is illustrated.

![Standardization](random_process_results/standardization.png)

![Standardization](random_process_results/standardization_features.png)

![Standardization](random_process_results/standardization_feature_distribution_original_data.png)

![Standardization](random_process_results/standardization_feature_distribution_standardized_data.png)

## Citation

Please note that the code and technical details made available are for educational purposes only. The repo is not open for collaboration.

If you happen to use the code from this repo, please use the below citation to cite. Thank you!

balarcode (2025). *GitHub - balarcode/subjects: Practical implementation of algorithms, concepts and techniques from subjects such as Linear Algebra, Random Processes & Probability and PyTorch.* GitHub. https://github.com/balarcode/subjects

## Copyright

<a href="https://github.com/balarcode/subjects">Subjects</a> © 2025 by <a href="https://github.com/balarcode">balarcode</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/">CC BY-NC-ND 4.0</a>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nd.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
