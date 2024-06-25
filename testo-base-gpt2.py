from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Nome del modello
MODEL_NAME = "gpt2"

# Caricamento del tokenizer e del modello pre-addestrato
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)

# Prompt di input
PROMPT = "How cute is a cat? "

# Tokenizzazione del prompt
input_ids = tokenizer.encode(PROMPT, return_tensors='pt')

# Generazione del testo
output = model.generate(
    input_ids, 
    max_length=50,  # Lunghezza massima del testo generato
    num_beams=5,    # Numero di fasci per la ricerca del beam
    no_repeat_ngram_size=2,  # Evita la ripetizione di n-grammi
    early_stopping=True  # Arresto anticipato quando tutte le sequenze sono complete
)

# Decodifica del testo generato
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)
