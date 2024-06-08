# LLM
### Goal:  
>Classify whether an argument belongs to a "Premise" or "Claim".  
### Model:  
* **LLaMA3-8B**  
* **LLaMA2-7B**  
>Authorized directly from Kaggle. No need to download to the local device  
### Method:  
  Fine-tune LLaMA3 using PEFT(a Python library by HuggingFace for Parameter-Efficient Fine-Tuning)
### Result:  
* **Before fine-tuning:**  
  The outcome might always be "Claim". Only a few "Premise". The accuracy is 47% correct for a 2-answer problem has a 50% probability.  
* **After fine-tuning:**  
  The outcome has both "Claim" and "Premise". The accuracy is raised to 76% correct.
### Prompt:  
>The correct answer in the training script should be "text" not "label with numbers".  
>We should use the sentence "either...or..." to distinct the 2 classes.
```Python
def generate_prompt(data_point):
    return f"""
            This sentense is either premise or claim, which category does it belong to? Be determine and concise about the output. The answer is either premise or claim.

            [{data_point["text"]}] = {data_point["pc"]}
            """.strip()
```
```Python
def generate_test_prompt(data_point):
    return f"""
            This sentense is either premise or claim, which category does it belong to? Be determine and concise about the output. The answer is either premise or claim.
            
            [{data_point["text"]}] = """.strip()
```
Get the string after "=" to elicit the answer
```Python
        prompt = X_test.iloc[i]["text"]
        pipe = pipeline(task="text-generation", 
                        model=model, 
                        tokenizer=tokenizer, 
                        max_new_tokens = 1, 
                        temperature = 1.0,
                       )
        result = pipe(prompt)
        answer = result[0]['generated_text'].split("=")[-1].strip()
```
### Fine-tuning:  
>The way we fine-tune LLM. We do not separate input sentences with labels. Instead, we combine them into a corpus. Then we use the Supervised Fine-tuning Step (SFT) in the Transformer Reinforcement Learning library (trl) by HuggingFace.
  
ps. The outcome of the result might not be exactly the "Premise" or "Claim". We might see "Prem", "premise" or "claim" as the result of prediction. Thus, we can resolve this problem beforehand.

