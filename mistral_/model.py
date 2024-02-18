import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import prepare_model_for_kbit_training
from peft import LoraConfig, get_peft_model
#declaring the constant configurations and model ids

#configuration of the mistral  model
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
#configuration of peft lora
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj","o_proj","gate_proj",
        "up_proj",
        "down_proj",
        "lm_head",],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model_id = "mistralai/Mistral-7B-v0.1"

#load the model to set-up the backend model to classify dark patterns effectively
#also load the Tokenizer and make the parameter add_eos_token=False since only then the model generates the completion

def model_load(model_id=model_id, bnb_config=bnb_config,lora_config=lora_config):
    model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})
    tokenizer = AutoTokenizer.from_pretrained(model_id, add_eos_token=False)
    model.gradient_checkpointing_enable()
    model = prepare_model_for_kbit_training(model)
    peft_model = get_peft_model(model, lora_config) 
    #model.add_adapter(lora_config, adapter_name="adapter")
    model.load_state_dict(torch.load("/content/mistralclass.pt"))
    return model,tokenizer
    
#define the alpaca format for the prompt for training and testing purposes
def generate_prompt(data_point, return_out=True):
    text = 'Given Input that represents text from a webpage, write the correct option for the multiple choice question.\n\n'
    text += f'### Input:\n{data_point["input"]}\nChoose which of the following dark patterns it falls under:\n' \
             '(A) Urgency\n(B) Scarcity\n(C) Misdirection\n(D) Social Proof\n(E) Obstruction\n(F) Sneaking\n(G) Forced Action\n(H) Not a Dark Pattern\n\n'
    text += f'### Answer:\n{data_point["output"] if return_out else ""}'

    return text

#define function to generate output completions by the model
def get_completion_2(query: str, model, tokenizer) -> str:
   device = "cuda:0"

   prompt = generate_prompt(query, return_out=False)
  
   encodeds = tokenizer(prompt, return_tensors="pt", )

   model_inputs = encodeds.to(device)

   generated_ids = model.generate(**model_inputs, max_new_tokens=10, do_sample=True)
   decoded = tokenizer.batch_decode(generated_ids)
   return (decoded[0][327+len(query["input"])])

#result = get_completion_2(query=d, model=model, tokenizer=tokenizer)
#print(result)

#include batch size and in colab add parameter for evaluation
