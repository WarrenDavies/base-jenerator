from dataclasses import dataclass, field
from typing import List

from basejenerator.artifacts.base_artifact import BaseArtifact

@dataclass
class GeneratorOutput:
    """
    Standardized return type for all GenAI pipelines within the Jenerator ecosystem
    """
    batch: List[BaseArtifact]
    extras: dict = field(default_factory=dict)
