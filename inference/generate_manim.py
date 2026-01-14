
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "hmnshudhmn24/manim-wizard-1.5b"

tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)

prompt = "Create a Manim animation showing a parabola."

out = model.generate(**tok(prompt, return_tensors="pt").to(model.device), max_new_tokens=400)
print(tok.decode(out[0], skip_special_tokens=True))
