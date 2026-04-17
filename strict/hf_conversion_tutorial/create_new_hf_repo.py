import argparse
import pathlib
import shutil


TODO_TEXT = """# TODO
 - In the modeling file, edit the code between the two comments saying YOUR CODE...
 - In the modeling file, edit/add the model architectures, i.e. ForCausalLM to ForMaskedLM, adding ForSequenceModeling, etc.
 - In the config file, reflect the pervious changes, i.e. change the AutoModel, architecture, add AutoModelForSequenceModeling, etc.
 - In the config file, edit the model configurations to reflect your configurations (so changing hidden size, adding a parameter, etc.)
 - In the model_configuration file, reflect the changes made in the config file.
 - Make sure that the model keys in the bin file the same as the ones in the modeling.py file.
 - In the special_tokens_map file, change the values of the special tokens, remove those not used, add new ones.
 - In the tokenizer_config file, change the value of the tokenizer class, special tokens, remove unused special tokens.
 - Add the behaviours you want when tokenizing sentences. For example if you want a sperator between a pair of sentences, add:
    ```json
    "pair": [
      {
        "SpecialToken": {
          "id": "<s>",
          "type_id": 0
        }
      },
      {
        "Sequence": {
          "id": "A",
          "type_id": 0
        }
      },
      {
        "SpecialToken": {
          "id": "</s>",
          "type_id": 0
        }
      },
      {
        "Sequence": {
          "id": "B",
          "type_id": 0
        }
      }
    ],
    "special_tokens": {
      "<s>": {
        "id": "<s>",
        "ids": [
          1
        ],
        "tokens": [
          "<s>"
        ]
      },
      "</s>": {
        "id": "</s>",
        "ids": [
          2
        ],
        "tokens": [
          "</s>"
        ]
      }
      ```
      to the post_processor field in the tokenizer.json (if you do not have one, create one.)
"""


def _parse_arguments():
    parser = argparse.ArgumentParser("This parser takes the location of the model weights, the tokenizer, and the location to save the new HF repository.")

    # Required Parameters
    parser.add_argument("--model_weights_path", required=True, type=pathlib.Path, help="Path to the model weights.")
    parser.add_argument("--tokenizer_path", required=True, type=pathlib.Path, help="Path to the tokenizer file.")
    parser.add_argument("--save_directory", required=True, type=pathlib.Path, help="Directory in which to create the HF repository.")
    parser.add_argument("--dummy_directory", default="dummy_model", required=True, type=pathlib.Path, help="Path to the dummy repository.")

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = _parse_arguments()

    shutil.copytree(args.dummy_directory, args.save_directory)
    shutil.copy(args.model_weights_path, args.save_directory / "pytorch_model.bin")
    shutil.copy(args.tokenizer_path, args.save_directory / "tokenizer.json")

    with (args.save_directory / "TODO.md").open("w") as todo_file:
        print(TODO_TEXT, file=todo_file)
