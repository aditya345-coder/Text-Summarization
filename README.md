# Text Summarization

This is a Flask-based web application that provides text summarization using the Pretrained model. The app takes user input, processes it using a pretrained Pegasus model, and returns a concise summary.

## Project Structure
```
├───.github
│   └───workflows
├───config
|   └───config.yaml
├───notebooks
|   └───01_data_ingestion.ipynb
|   └───02_data_validation.ipynb
|   └───03_data_transformation.ipynb
|   └───04_data_trainer.ipynb
|   └───05_data_evalution.ipynb
|   └───Text_Summarization.ipynb
|   └───trials.ipynb
├───src
│   └───textSummarizer
│       ├───components
│           └───__init__.py
│           └───data_ingestion.py
│           └───data_validation.py
│           └───data_transformation.py
│           └───model_evaluation.py
│           └───model_trainer.py
│       ├───config
│           └───__init__.py
│           └───configuration.py
│       ├───constants
│           └───__init__.py
│       ├───entity
│           └───__init__.py
│       ├───logging
│           └───__init__.py
│       ├───pipeline
│           └───__init__.py
│           └───stage_01_data_.py
│           └───stage_02_data_.py
│           └───stage_03_data_.py
│           └───stage_04_model_trainer.py
│           └───stage_05_model_evalution.py
│       ├───utils
│           └───__init__.py
│           └───common.py
│       ├───__init__.py
│
├───templates
│   └───layout.html
│   └───index.html
│   └───prediction.html
├───static
│   └───css
│   	└───css
│   ├───images
│   ├───js
│
├───.gitignore
├───app.py
├───Dockerfile
├───LICENSE
├───main.py
├───params.yaml
├───README.md
├───requirements.txt
├───setup.py
├───template.py
```


### Folder Details

- **src**: Contains Python files for the core functionalities, such as data ingestion, data validation, data transformation, model training, and evaluation.
  - `components/`: Implements various components like data ingestion, validation, and transformation.
  - `config/`: Configuration management for the app.
  - `pipeline/`: Scripts to define different stages of the data and model pipeline.
  - `utils/`: Helper functions for commonly used operations.
  
- **app.py**: Contains the Flask application code, which is the backbone of the web interface.

- **templates**: Stores HTML files for the frontend of the web application. 
  - `layout.html`, `index.html`, `prediction.html`. `train.html`, `error.html`: Define the structure and presentation of the pages.

- **static**: Contains static files like images, CSS, and JavaScript.
  - `css/`: Custom stylesheets for the application.
  - `images/`: Images used for displaying the app's features or screenshots.
  
- **requirements.txt**: Lists the Python packages and dependencies needed to run the project.

- **main.py**: Executes the end-to-end process, running all the modules from data ingestion to model evaluation.

- **params.yaml**: Contains the model training parameters, such as learning rate, batch size, and other attributes for tuning the model.

- **notebooks**: Includes Jupyter notebooks for various stages of the project:
  - Data ingestion, validation, transformation, model training, evaluation, and a dedicated notebook for text summarization (`Text_Summarization.ipynb`).

## Features

- **Text Summarization**: The app provides a simple interface to input text and generate concise summaries.
- **Pretrained Pegasus Model**: Uses Hugging Face's Pegasus model for summarization tasks.
- **Web Interface**: Built using Flask, with Bootstrap for styling and responsive design.
- **Modular Codebase**: The project follows a clean, modular structure with separate components for data ingestion, validation, transformation, and model training.

## Demo


https://github.com/user-attachments/assets/c46806c9-e4fb-4a54-a8f1-5659b9e7c9bc


### Try it out

To run the project locally, follow these steps:

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-summarization-app.git
    ```
    
2. Create Virtual environment
   ```bash
   python -m virtualenv venv
   ```
   
3. Activate Virtual environment
   ```bash
   venv/Scripts/activate
   ```
   
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Start the Flask app:
    ```bash
    python app.py
    ```

6. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

## Usage

- Input a block of text in the provided text box.
- Click the "Submit" button.
- The app will generate a concise summary of the input text.

