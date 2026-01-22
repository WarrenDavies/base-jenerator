"""
Implements a simple decorator-based model registry for dynamically managing
different artifact types.

This system allows concrete BaseArtifact subclasses to register themselves
using a specific string key (e.g., 'pil-artifact'), enabling the
application to instantiate the correct class based on a configuration setting
without explicit imports.
"""

ARTIFACT_REGISTRY = {}

def register_model(name):
    """
    A decorator factory used to register an Artifact subclass.

    The decorated class is stored in the global ARTIFACT_REGISTRY dictionary
    under the provided `name`.

    Args:
        name (str): The string key used to reference the artifact format
                    in the configuration (e.g., 'pil-artifact').

    Returns:
        Callable: A decorator function that takes a class and registers it.
    """
    def decorator(cls):
        ARTIFACT_REGISTRY[name] = cls
        return cls
    return decorator


def get_artifact_object(name, data, item_extras):
    """
    Retrieves and instantiates the correct artifact class based on the
    configuration dictionary.

    It looks up the class in ARTIFACT_REGISTRY using the key found in
    `name`.

    Args:
        config (dict): The configuration dictionary, which must contain a
                       'model' key corresponding to a registered model name.

    Returns:
        Artifact: An instantiated object of the registered generator class.

    Raises:
        KeyError: If the value of `name` is not found in the
                  ARTIFACT_REGISTRY.
    """
    ArtifactClass = ARTIFACT_REGISTRY[name]
    artifact = ArtifactClass(data, item_extras)

    return artifact