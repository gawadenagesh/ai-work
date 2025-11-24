# splitters/strategies for different chunking methods

class ChunkingStrategy:
    def chunk(self, text):
        raise NotImplementedError("Chunking strategy must implement the chunk method.")