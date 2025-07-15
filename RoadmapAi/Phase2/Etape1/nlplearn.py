
if __name__ == '__main__':
    from fastai.text.all import *


    dls= TextDataLoaders.from_folder(untar_data(URLs.IMDB),valid= 'test', num_workers=0)
    learn= text_classifier_learner(dls, AWD_LSTM, drop_mult= 0.5, metrics= accuracy)
    learn.fine_tune(4, 1e-2)
    learn.predict(("what the fuck"))
