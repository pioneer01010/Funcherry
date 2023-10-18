# Funcherry

<p align="center">
</br>
    <img width="150" src="https://github.com/pioneer01010/Funcherry/blob/main/assets/funcherry.png">
</p>

Funcherry is a library to generate python function blocks.
The main purpose of this library is to augment datasets for training or fine-tuning Language Model.

The basic motivations behind this project are:
- **A suitable datasets can be obtained based on metrics related to code maintainability**
  - It is difficult to obtain in-batch samples based on metrics. Many known datasets are unrelated to code metrics.
  - Quality code with high maintainability is not being generated in LLM.
- **Even without specifying the target function, it will be selected from your project**
  - Finding and interfacing function blocks with weak metrics is cumbersome.
  - There is a lack of tools to increase the amount of code data samples to large numbers.
