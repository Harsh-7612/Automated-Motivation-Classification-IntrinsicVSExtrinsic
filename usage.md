## 💻 Usage

### 1. Zero-Shot Labeling
Extract mentor-specific statements and run the initial BART zero-shot classification:

```bash
python src/model_pipeline/zero_shot_inference.py \
    --input data/raw/conversations.csv \
    --output data/interim/labelled.csv
```

