"""Load and call the bundled scoring model."""

from pathlib import Path
from typing import Any

import joblib

DEFAULT_MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.joblib"


class Model:
    """Thin, lazy-loading wrapper around the serialized estimator."""

    def __init__(self, model_path: str | Path = DEFAULT_MODEL_PATH) -> None:
        self.model_path = Path(model_path)
        self._estimator: Any | None = None

    @property
    def estimator(self) -> Any:
        """Load the model on first use, not when the API starts."""
        if self._estimator is None:
            self._estimator = joblib.load(self.model_path)
        return self._estimator

    def predict(self, features: Any) -> Any:
        """Return predictions for an input supported by the fitted estimator."""
        return self.estimator.predict(features)
