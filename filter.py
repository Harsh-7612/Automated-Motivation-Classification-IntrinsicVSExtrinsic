"""Confidence-threshold filter for zero-shot pseudo-labels."""
import argparse, logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

def filter_by_confidence(input_path: str, output_path: str, threshold: float = 0.88) -> None:
    df = pd.read_csv(input_path)
    logger.info(f"Loaded {len(df)} rows from {input_path}")
    filtered = df[df["confidence"] > threshold].reset_index(drop=True)
    logger.info(f"Kept {len(filtered)}/{len(df)} rows above threshold={threshold}")
    filtered.to_csv(output_path, index=False)
    logger.info(f"Saved to {output_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="labelled.csv")
    p.add_argument("--output", default="pseudo_lbd.csv")
    p.add_argument("--threshold", type=float, default=0.88)
    args = p.parse_args()
    filter_by_confidence(args.input, args.output, args.threshold)
