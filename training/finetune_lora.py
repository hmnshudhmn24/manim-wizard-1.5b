
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

MODEL_ID = "Qwen/Qwen2.5-Coder-1.5B"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True
)

lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, task_type="CAUSAL_LM")
model = get_peft_model(model, lora)

dataset = load_dataset("json", data_files="data/manim_instructions.jsonl")

args = TrainingArguments(
    output_dir="./manim-wizard-lora",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset["train"],
    tokenizer=tokenizer,
    formatting_func=lambda x: f"<|user|>{x['instruction']}<|assistant|>{x['response']}",
    args=args
)

trainer.train()
model.save_pretrained("manim-wizard-1.5b")
