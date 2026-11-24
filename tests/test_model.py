from pathlib import Path

import pandas as pd
import pytest
from lightgbm.basic import LightGBMError

from model import DEFAULT_MODEL_PATH, Model


@pytest.fixture(scope="module")
def loaded_model() -> Model:
    """Load the actual bundled model once for model tests."""
    return Model(DEFAULT_MODEL_PATH)


@pytest.fixture(scope="module")
def valid_features(loaded_model: Model) -> pd.DataFrame:
    """Build an all-zero row using the feature names stored by LightGBM."""
    estimator = loaded_model.estimator
    classifier = estimator.named_steps["model"]
    feature_names = classifier.feature_name_
    return pd.DataFrame([[0.0] * len(feature_names)], columns=feature_names)


def test_model_predicts_with_bundled_model(
    loaded_model: Model, valid_features: pd.DataFrame
) -> None:
    prediction = loaded_model.predict(valid_features)

    assert len(prediction) == 1


def test_model_accepts_missing_numeric_values(
    loaded_model: Model, valid_features: pd.DataFrame
) -> None:
    features_with_missing_value = valid_features.copy()
    features_with_missing_value.iloc[0, 0] = float("nan")

    prediction = loaded_model.predict(features_with_missing_value)

    assert len(prediction) == 1


def test_model_rejects_missing_required_feature(
    loaded_model: Model, valid_features: pd.DataFrame
) -> None:
    incomplete_features = valid_features.drop(columns=[valid_features.columns[0]])

    with pytest.raises(LightGBMError, match="number of features"):
        loaded_model.predict(incomplete_features)


def test_model_rejects_text_in_numeric_feature(
    loaded_model: Model, valid_features: pd.DataFrame
) -> None:
    invalid_features = valid_features.astype(object)
    invalid_features.iloc[0, 0] = "not-a-number"

    with pytest.raises((TypeError, ValueError)):
        loaded_model.predict(invalid_features)


def test_model_raises_for_invalid_path(tmp_path: Path) -> None:
    model = Model(tmp_path / "missing-model.joblib")

    with pytest.raises(FileNotFoundError):
        model.predict([[0.0]])
