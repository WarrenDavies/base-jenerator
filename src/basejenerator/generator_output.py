from dataclasses import dataclass

from basejenerator.artifact import Artifact

@dataclass
class GeneratorOutput:
    """
    Standardized return type for all GenAI pipelines within the Jenerator ecosystem
    """
    batch: List[Artifact]
    extras: dict = field(default_factory=dict)
