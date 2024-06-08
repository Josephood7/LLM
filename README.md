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
  The outcome might always be "Claim". Only a few "Premise". The accuracy is 47% correct for 50% probability in this 2-answer problem.  
* **After fine-tuning:**  
  The outcome has both "Claim" and "Premise". The accuracy is raised to 76% correct.
    
ps. The outcome of the result might not be exactly the "Premise" or "Claim". We might see "Prem", "premise" or "claim" as the result of prediction. Thus, we can resolve this problem beforehand.

