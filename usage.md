💻 Usage
1. Zero-Shot Labeling
Extract mentor-specific statements and run the initial BART zero-shot classification:

Bash
python src/model_pipeline/zero_shot_inference.py \
    --input data/raw/conversations.csv \
    --output data/interim/labelled.csv
2. High-Confidence Filtering
Filter out low-confidence predictions to establish a clean ground-truth approximation:

Bash
python src/data_pipeline/confidence_filter.py \
    --input data/interim/labelled.csv \
    --output data/interim/pseudo_lbd.csv \
    --threshold 0.88
3. Model Fine-Tuning
Execute the Jupyter Notebook to augment pseudo_lbd.csv into aug.csv and fine-tune the DistilBERT model.

Bash
jupyter notebook notebooks/01_finetune_distilbert.ipynb
4. Interactive Streamlit App
Launch the web interface to test real-time motivational text classification:

Bash
streamlit run app/main.py
