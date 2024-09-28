from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import ModelTrainerConfig
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        
        # Check if the model already exists
        model_path = os.path.join(self.config.root_dir, "pegasus-samsum-model")
        if os.path.exists(model_path):
            print(f"Loading existing model from {model_path}")
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)
        else:
            print(f"Training new model and saving to {model_path}")
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
            
            seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
            
            #loading data 
            dataset_samsum_pt = {}
            for split in ['train', 'test', 'validation']:
                dataset_samsum_pt[split] = load_from_disk(os.path.join(self.config.data_path, split))

            trainer_args = TrainingArguments(
                output_dir=self.config.root_dir, num_train_epochs=self.config.num_train_epochs, warmup_steps=self.config.warmup_steps,
                per_device_train_batch_size=self.config.per_device_train_batch_size, per_device_eval_batch_size=self.config.per_device_train_batch_size,
                weight_decay=self.config.weight_decay, logging_steps=self.config.logging_steps,
                eval_strategy=self.config.eval_strategy, eval_steps=self.config.eval_steps, save_steps=1e6,
                gradient_accumulation_steps=self.config.gradient_accumulation_steps
            ) 

            trainer = Trainer(model=model_pegasus, args=trainer_args,
                      tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                      train_dataset=dataset_samsum_pt["train"], 
                      eval_dataset=dataset_samsum_pt["validation"])
            
            trainer.train()

            ## Save model
            model_pegasus.save_pretrained(model_path)
            ## Save tokenizer
            tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))

        return model_pegasus, tokenizer