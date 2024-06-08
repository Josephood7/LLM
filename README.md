# LLM
### Goal:  
>Classify whether an argument belongs to a "Premise" or "Claim".  
### Model:  
* **LLaMA3-8B**  
* **LLaMA2-7B**  
>Authorized directly from Kaggle. No need to download to the local device  
### Method:  
  Fine-tune LLaMA3 using PEFT(a Python library by HuggingFace for efficient fine-tuning)
### Result:  
* **Before fine-tuning:**  
  The outcome might always be "Claim". Only a few "Premise". The accuracy is 47% correct for a 2-answer problem has a 50% probability.  
* **After fine-tuning:**  
  The outcome has both "Claim" and "Premise". The accuracy is raised to 76% correct.
### Prompt:  
>The correct answer in the training script should be "text" not "label with numbers".  
>We should use the sentence "either...or..." to distinct the 2 classes.
### Fine-tuning:  
>The way we fine-tune LLM. We do not separate input sentences with labels for supervised learning. Instead, we combine them into a corpus. The LLM then use self-supervised learning to mask and learn through the transformer mechanism.
  
ps. The outcome of the result might not be exactly the "Premise" or "Claim". We might see "Prem", "premise" or "claim" as the result of prediction. Thus, we can resolve this problem beforehand.

