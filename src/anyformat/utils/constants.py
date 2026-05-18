"""Shared constants for anyformat converters."""

# Image quality presets
IMAGE_QUALITY_PRESETS = {
    "low": {"quality": 60, "optimize": True},
    "medium": {"quality": 80, "optimize": True},
    "high": {"quality": 95, "optimize": False},
}

# Video quality presets
VIDEO_QUALITY_PRESETS = {
    "low": {"crf": 28, "preset": "faster"},
    "medium": {"crf": 23, "preset": "medium"},
    "high": {"crf": 18, "preset": "slow"},
}

# Audio quality presets
AUDIO_QUALITY_PRESETS = {
    "low": {"bitrate": "128k"},
    "medium": {"bitrate": "192k"},
    "high": {"bitrate": "320k"},
}


