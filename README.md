# Medical_LLM

This model is built upon the LLaVA framework - Large Language and Vision Assistant. You can find the repo here: https://github.com/haotian-liu/LLaVA/tree/main

The objective of this model is to streamline the evaluation process of radiology reports, which is currently performed manually by professional radiologists. Our goal is to develop a model capable of interpreting X-ray images and autonomously generating detailed radiology reports, thereby enhancing efficiency and accuracy in medical diagnostics. 

To finetune the model on custom data, follow the instructions on this page: https://github.com/haotian-liu/LLaVA/blob/main/docs/Finetune_Custom_Data.md

### Evaluation
#### 1. Generate responses

Run inference on a single X-ray image
`python3 -m llava.serve.cli —model-path path_to_model —model-base path_to_llava-v1.5-13b —image-file path_to_img_folder/*.jpg`

Run inference on a set of data
```python3 LLaVA/llava/eval/model_vqa.py \
    --model-path path_to_trained_model \
    --model-base llava-v1.5-13b \
    --question-file question_prompt.jsonl \
    --image-folder path_to_image_data \
    --answers-file validation_responses.jsonl```

#### 2. Evaluate the generated responses

Evaluate diagnostic accuracy using an LLM: wip
