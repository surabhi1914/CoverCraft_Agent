# src/pipeline/candidate_profile_cache.py

"""
Purpose of this file: Cache utilities for candidate profile generation.

The candidate profile is expensive to create and does not change often.
This module stores the generated CandidateProfile based on a hash of the
candidate source text.
"""
# ---------------------------------------------
# Importing libraries
# ---------------------------------------------
from hashlib import sha256
from pathlib import Path
from typing import Optional, Tuple

from src.config import PROCESSED_DATA_DIR
from src.schemas.candidate_schema import CandidateProfile
from src.agents.candidate_builder import build_candidate_profile
from src.utils.file_utils import load_json, save_json, ensure_directory_exists


CACHE_DIR = PROCESSED_DATA_DIR / "cache"
CANDIDATE_PROFILE_CACHE_PATH = CACHE_DIR / "candidate_profile_cache.json"

# ---------------------------------------------
# Functions
# ---------------------------------------------
def get_text_hash(text: str) -> str:
    """
    Create a stable hash for a text block.
    """
    if not text:
        return ""

    return sha256(text.encode("utf-8")).hexdigest()


def load_cached_candidate_profile(
    candidate_source_text: str,
    cache_path: str | Path = CANDIDATE_PROFILE_CACHE_PATH,
) -> Optional[CandidateProfile]:
    """
    Load cached CandidateProfile if the source text has not changed.
    """
    cache_path = Path(cache_path)

    if not cache_path.exists():
        return None

    source_hash = get_text_hash(candidate_source_text)

    try:
        cache_data = load_json(cache_path)
    except Exception:
        return None

    cached_hash = cache_data.get("source_hash")
    cached_profile = cache_data.get("candidate_profile")

    if cached_hash != source_hash:
        return None

    if not cached_profile:
        return None

    return CandidateProfile(**cached_profile)


def save_candidate_profile_cache(
    candidate_source_text: str,
    candidate_profile: CandidateProfile,
    cache_path: str | Path = CANDIDATE_PROFILE_CACHE_PATH,
) -> None:
    """
    Save CandidateProfile cache with source text hash.
    """
    cache_path = Path(cache_path)
    ensure_directory_exists(cache_path.parent)

    cache_data = {
        "source_hash": get_text_hash(candidate_source_text),
        "candidate_profile": candidate_profile.model_dump(),
    }

    save_json(cache_data, cache_path)


def get_or_build_candidate_profile(
    candidate_source_text: str,
    use_cache: bool = True,
) -> Tuple[CandidateProfile, bool]:
    """
    Load candidate profile from cache if possible.
    Otherwise build it using the LLM and save it.

    Returns:
        candidate_profile, used_cache
    """
    if not candidate_source_text or not candidate_source_text.strip():
        raise ValueError("Candidate source text cannot be empty.")

    if use_cache:
        cached_profile = load_cached_candidate_profile(candidate_source_text)

        if cached_profile:
            return cached_profile, True

    candidate_profile = build_candidate_profile(candidate_source_text)

    if use_cache:
        save_candidate_profile_cache(
            candidate_source_text=candidate_source_text,
            candidate_profile=candidate_profile,
        )

    return candidate_profile, False