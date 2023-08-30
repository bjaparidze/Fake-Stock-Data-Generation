import numpy as np
import pandas as pd


def classify_as_str(mis_class_prob, df: pd.DataFrame):
    """
    Classifies a random set of columns as string data type given a probability value.
    Operation is performed inplace
    (exhibits similar behavior as pandas' functions when inplace=True)
    """
    length = len(df.columns)

    # Generate misclassified indices based on misclassified probability
    misclassified_indices = np.random.choice(
        length, size=int(mis_class_prob * length), replace=False
    )

    # Introduce misclassification by converting selected columns to strings
    for idx in misclassified_indices:
        df[df.columns[idx]] = df[df.columns[idx]].astype(str)
