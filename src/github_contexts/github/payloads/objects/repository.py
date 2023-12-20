
class RepositoryObject:

    def __init__(self, repository: dict):
        self._repository = repository
        return

    @property
    def default_branch(self) -> str:
        return self._repository["default_branch"]
