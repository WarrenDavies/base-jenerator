# Base Jenerator

Abstract base class and return formats for AI Generator classes within the Jeneratorverse, providing a unified API across different media formats. 

The idea is, whether you're running Stable Diffusion 1.5 with imagejenerator, or Llama 3.2 with textjenerator, you'll always call the same methods, and get outputs returned to you in the same format.

## BaseGenerator class

Contract for generator classes that run model inference.

Abstract methods that must be implmented by subclasses are:

* `load`: load the model into memory, and assign the pipeline/model/engine to `self.model`.
* `prepare`: Reset lifecycle without tearing down the model - e.g., reset torch generators, clear cache, etc.
* `generate`: The public method that is called to run inference.
* `generate_impl`: Subclasses must implement this to run inference. Called by `.generate()`.
* `_quick_wrap`: Helper for subclasses to wrap artifacts into the Artfact class.
* `teardown`: Purge the model from memory, empty cache, run garbage collector, etc. 

## GeneratorOutput

Wrapper for artifacts generated. Will always return artifacts in a list in  the `.artifacts` attribute, even for pipelines that return a single artifact (e.g., LLMs, non-batch image generation, etc.). Generation level metadata can be returned in `.extras`, however you should reserve this for things really cannot be captured anywhere else. The generator classes are meant to be stateless, besides the model/pipline. 

They are like toasters - prompt in, artifact out.

## Artifact

Represents a single artifact created by the generator. One image, text response, wav file, or whatever.

As with GeneratorOutput you can bundle metadata into `.item_extras` but again, I recommend leaving that responsibility to the calling app.

