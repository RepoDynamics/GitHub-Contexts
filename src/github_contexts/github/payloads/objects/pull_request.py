
class PullRequestObject:

    def __init__(self, pull_request: dict):
        self._pull_request = pull_request
        return

    @property
    def diff_url(self) -> str | None:
        return self._pull_request.get("diff_url")

    @property
    def html_url(self) -> str | None:
        return self._pull_request.get("html_url")

    @property
    def merged_at(self) -> str | None:
        return self._pull_request.get("merged_at")

    @property
    def patch_url(self) -> str | None:
        return self._pull_request.get("patch_url")

    @property
    def url(self) -> str | None:
        return self._pull_request.get("url")
