import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
            
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        try:
            logger.info(f"Loading dataset from: {self.config.data_path}")
            dataset_samsum = load_from_disk(self.config.data_path)
            logger.info(f"Dataset loaded successfully. Splits: {dataset_samsum.keys()}")

            for split in dataset_samsum.keys():
                logger.info(f"Processing {split} split")
                processed_split = dataset_samsum[split].map(
                    self.convert_examples_to_features,
                    batched=True,
                    remove_columns=dataset_samsum[split].column_names,
                    desc=f"Processing {split} split"
                )
                
                output_dir = os.path.join(self.config.root_dir, "samsum_dataset", split)
                output_dir = output_dir.replace('\\', '/')  # Ensure forward slashes
                logger.info(f"Saving {split} split to: {output_dir}")
                os.makedirs(output_dir, exist_ok=True)
                
                try:
                    processed_split.save_to_disk(output_dir)
                    logger.info(f"{split} split saved successfully to {output_dir}")
                except Exception as save_error:
                    logger.error(f"Error saving {split} split: {str(save_error)}")
                    # Try alternative save method
                    try:
                        logger.info(f"Attempting alternative save method for {split} split")
                        processed_split.to_json(os.path.join(output_dir, f"{split}.json"))
                        logger.info(f"{split} split saved as JSON successfully")
                    except Exception as json_error:
                        logger.error(f"Error saving {split} split as JSON: {str(json_error)}")
                        raise

            logger.info(f"All splits of transformed dataset saved to {os.path.join(self.config.root_dir, 'samsum_dataset')}")
        except Exception as e:
            logger.error(f"Error in convert method: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            logger.error(f"Error args: {e.args}")
            raise