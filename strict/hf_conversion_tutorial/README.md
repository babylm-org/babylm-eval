# HuggingFace Converter Tutorial

## Introduction

This folder contains a python script to convert your model and tokenizer into a HuggingFace repository using the `dummy_model` found here. The arguments of the file are as follows:

- `model_weights_path`: The path to your model weights (required)
- `tokenizer_path`: The path to your tokenizer.json file (required)
- `save_directory`: Where you want to save your HuggingFace Repository (required)
- `dummy_directory`: The path to the dummy directory. By default it is `dummy_model` but you can choose another one. For example, if you already have a HF repository (with the right modeling file, etc.), you could use it as a dummy file to avoid having to re-create the files in your HF repository.

> [!Warning]
> The created repository will not be usable as is, a TODO.md file will be created with all the modifications needed to be done to make sure your repository works. It is also very important to check that the names of the parameters in your model weights match those in your modeling, otherwise the model will ignore them and randomly initialize them.

## Adding more AutoModel classes.

Say you want to add a AutoModelForSequenceClassification (for example the one you use in the finetune pipeline). You can do this by adding the following class (it is an example the exact names and internals of the function can be different):

```python
class MyModelForSequenceClassification(MyModel):
    _keys_to_ignore_on_load_unexpected = ["lm_head"]  # Or whatever the name of your Language Modeling head is
    _keys_to_ignore_on_load_missing = ["head"]  # Or whatever the name of your classification head will be

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)

        self.num_labels = config.num_labels
        self.head = Classifier(config, self.num_labels)  # Do not forget to specify the classifier class.

    def forward(...):
        ...
```
