"""Connection module for LibreOffice UNO bridge."""

from .uno_bridge import UnoBridge, get_bridge
from .document_pool import DocumentPool, DocumentInfo, get_pool

__all__ = [
    "UnoBridge",
    "get_bridge",
    "DocumentPool",
    "DocumentInfo",
    "get_pool",
]
