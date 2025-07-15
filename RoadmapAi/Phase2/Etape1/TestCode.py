if __name__ == "__main__":
    from fastai.tabular.all import *

    path= untar_data(URLs.ADULT_SAMPLE)

    dls= TabularDataLoaders.from_csv(path/'adult.csv', y_names= "salary", cat_name= ['workclass', 'education', 'marital-status',
                                                                                     'occupation', 'relationship', 'race'],
                                     cont_names= ['age', 'fnlwgt', 'education-num'], procs=
                                     [Categorify, FillMissing, Normalize])

    learn= tabular_learner(dls, metrics= accuracy)
    learn.fit_one_cycle(3)