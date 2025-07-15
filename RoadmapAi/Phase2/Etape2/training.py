

if __name__ == '__main__':

    from fastai.vision.all import *
    import matplotlib.pyplot as plt

    path= Path(r"C:\Users\Superuser\PycharmProjects\RoadmapAi\Phase2\Etape2\ours")
    images= get_image_files(path)


    bears= DataBlock(
        blocks= (ImageBlock, CategoryBlock),
        get_items= get_image_files,
        splitter= RandomSplitter(valid_pct= 0.2, seed= 42),
        get_y= parent_label,
        item_tfms= RandomResizedCrop(224, min_scale= 0.5),
        batch_tfms= aug_transforms()

    )


    #bears= bears.new(item_tfms= Resize(128, ResizeMethod.Squish, pad_mode= 'Zeros'))

    dls= bears.dataloaders(path, bs= 5, num_workers=0)
    dls.train.show_batch(max_n= 8, nrows= 1, unique= True)

    learn= vision_learner(dls, resnet18, metrics= error_rate)
    learn.fine_tune(4)
    interp = ClassificationInterpretation.from_learner(learn)


    interp.plot_confusion_matrix()
    interp.plot_top_losses(5, nrows= 1)
    learn.export()
    
    plt.show()






