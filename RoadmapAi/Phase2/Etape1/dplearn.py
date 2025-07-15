
if __name__ == '__main__':
    from fastai.vision.all import *

    path = untar_data(URLs.CAMVID_TINY)

    # 👇 Crée une fonction normale au lieu de lambda
    def label_fn(o):
        return path/'labels'/f'{o.stem}_P{o.suffix}'

    dls = SegmentationDataLoaders.from_label_func(
        path,
        bs=8,
        fnames=get_image_files(path/"images"),
        label_func=label_fn,
        codes=np.loadtxt(path/'codes.txt', dtype=str),
        num_workers=0
    )

    learn = unet_learner(dls, resnet34)
    learn.fine_tune(8)
    learn.show_results(max_n= 6, figsize= (7,8))