# **SUIR-Model**

SUIR model for COVID-19 transmission projection in KDD 2020 paper "A knowledge transfer model for COVID-19 predicting and non-pharmaceutical intervention simulation".

## Requirements

All required packages are list in `environment.yml` which is available from [Anaconda](https://anaconda.org/). Install with command on CMD or terminal:

```
conda env create -f environment.yml
```

## Projecting COVID-19

- `SUIR_simplex.ipynb` Train an SUIR model by simplex algorithm (Nelder-Mead) and run projection for future days (Recommended)

- `./data` Contains COVID-19 data, including confirmed, cure and death, which are data for training model. Sample data in this repository are from "COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University" https://github.com/CSSEGISandData/COVID-19.

## License

This repository is licensed under the GNU General Public License (GPL).

If you find this code useful, please consider kindly cite our paper as
```
@inproceedings{wang2020SUIR,
  title={A knowledge transfer model for COVID-19 predicting and non-pharmaceutical intervention simulation},
  author={Wang, Jingyuan and Lin, Xin and Liu, Yuxi and Qilegeri and Feng, Kai and Lin, Hui},
  booktitle={Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  year={2020}
}
```

For more questions about code, issue or contact sweeneylin at buaa dot edu dot cn.
