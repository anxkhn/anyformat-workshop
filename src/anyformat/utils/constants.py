"""Shared constants for anyformat converters.

This module contains constants that are used across multiple converters
to ensure consistency and avoid duplication.
"""

# Quality presets for audio conversion
AUDIO_QUALITY_PRESETS = {
    "low": {"bitrate": "128k"},
    "medium": {"bitrate": "192k"},
    "high": {"bitrate": "320k"},
}

# Quality presets for image conversion
IMAGE_QUALITY_PRESETS = {
    "low": {"quality": 60, "optimize": True},
    "medium": {"quality": 85, "optimize": True},
    "high": {"quality": 95, "optimize": True},
}

# Quality presets for video conversion
VIDEO_QUALITY_PRESETS = {
    "low": {"crf": "28", "preset": "veryfast"},
    "medium": {"crf": "23", "preset": "medium"},
    "high": {"crf": "18", "preset": "slow"},
}

# Default quality setting
DEFAULT_QUALITY = "medium"

# Supported audio formats
SUPPORTED_AUDIO_FORMATS = ["mp3", "wav", "flac", "aac", "ogg", "m4a"]

# Supported image formats
SUPPORTED_IMAGE_FORMATS = ["jpeg", "jpg", "png", "webp", "gif", "bmp", "tiff"]

# Supported video formats
SUPPORTED_VIDEO_FORMATS = ["mp4", "avi", "mov", "mkv", "webm", "flv"]
