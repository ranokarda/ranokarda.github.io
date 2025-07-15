import gradio as gr
from fastai.vision.all import *

path = Path(r"C:\Users\Superuser\PycharmProjects\RoadmapAi\Phase2\Etape2")
learn_inf = load_learner(path / 'export.pkl')

def classify(img):
    pred_class, pred_idx, outputs = learn_inf.predict(img)
    scores = {c: float(s)*100 for c, s in zip(learn_inf.dls.vocab, outputs)}
    result = f"{pred_class} ({scores[pred_class]:.2f}%)"
    return result, scores

iface = gr.Interface(
    fn=classify,
    inputs=gr.Image(type="pil", label="Choisis une image d'ours"),
    outputs=[
        gr.Label(label="Classe prédite et score"),
        gr.Label(label="Probabilité (%) par classe")
    ],
    title="Classificateur d'Ours IA 🐻",
    description="Charge une image et découvre la race d'ours prédite par ton modèle IA.",
    theme='soft',
    allow_flagging="never"
)

iface.launch()
