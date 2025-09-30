#!/usr/bin/env python3

import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.llm.openrouter_client import MODEL_MAPPING

def get_models():
    """Return JSON array of model keys"""
    model_keys = sorted(MODEL_MAPPING.keys())
    print(json.dumps(model_keys))

if __name__ == "__main__":
    get_models()