def detect_stress(ndvi_value, threshold=0.35):
    if ndvi_value < threshold:
        return "⚠ Crop Stress Detected"
    return "✅ Crop Healthy"
