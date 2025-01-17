import importlib
from typing import TYPE_CHECKING, Any

from aibaba_ai_core.document_loaders import Blob, BlobLoader

if TYPE_CHECKING:
    from aibaba_ai_community.document_loaders.blob_loaders.cloud_blob_loader import (
        CloudBlobLoader,
    )
    from aibaba_ai_community.document_loaders.blob_loaders.file_system import (
        FileSystemBlobLoader,
    )
    from aibaba_ai_community.document_loaders.blob_loaders.youtube_audio import (
        YoutubeAudioLoader,
    )


_module_lookup = {
    "CloudBlobLoader": (
        "aibaba_ai_community.document_loaders.blob_loaders.cloud_blob_loader"
    ),
    "FileSystemBlobLoader": (
        "aibaba_ai_community.document_loaders.blob_loaders.file_system"
    ),
    "YoutubeAudioLoader": (
        "aibaba_ai_community.document_loaders.blob_loaders.youtube_audio"
    ),
}


def __getattr__(name: str) -> Any:
    if name in _module_lookup:
        module = importlib.import_module(_module_lookup[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__} has no attribute {name}")


__all__ = [
    "BlobLoader",
    "Blob",
    "CloudBlobLoader",
    "FileSystemBlobLoader",
    "YoutubeAudioLoader",
]
