import numpy as np
import torch

def make_json_safe(obj):
    """
    Recursively convert non-JSON-serializable objects
    into JSON-safe Python types.
    """

    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    elif isinstance(obj, tuple):
        return tuple(make_json_safe(v) for v in obj)

    elif isinstance(obj, np.ndarray):
        return obj.tolist()

    elif isinstance(obj, np.generic):
        return obj.item()

    elif isinstance(obj, torch.Tensor):
        return obj.detach().cpu().tolist()

    else:
        return obj
