from enum import Enum


class ActiveLockReason(Enum):
    RESOLVED = "resolved"
    OFF_TOPIC = "off-topic"
    TOO_HEATED = "too heated"
    SPAM = "spam"
    OTHER = None


class AuthorAssociation(Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"
    CONTRIBUTOR = "CONTRIBUTOR"
    COLLABORATOR = "COLLABORATOR"
    FIRST_TIME_CONTRIBUTOR = "FIRST_TIME_CONTRIBUTOR"
    FIRST_TIMER = "FIRST_TIMER"
    MANNEQUIN = "MANNEQUIN"
    NONE = "NONE"


class State(Enum):
    OPEN = "open"
    CLOSED = "closed"


class RefType(Enum):
    BRANCH = "branch"
    TAG = "tag"


class UserType(Enum):
    USER = "User"
    ORGANIZATION = "Organization"
    BOT = "Bot"


class EventType(Enum):
    BRANCH_PROTECTION_CONFIGURATION = "branch_protection_configuration"
    BRANCH_PROTECTION_RULE = "branch_protection_rule"
    CHECK_RUN = "check_run"
    CHECK_SUITE = "check_suite"
    CODE_SCANNING_ALERT = "code_scanning_alert"
    COMMIT_COMMENT = "commit_comment"
    CREATE = "create"
    CONTENT_REFERENCE = "content_reference"
    CUSTOM_PROPERTY = "custom_property"
    CUSTOM_PROPERTY_VALUES = "custom_property_values"
    DELETE = "delete"
    DEPENDABOT_ALERT = "dependabot_alert"
    DEPLOY_KEY = "deploy_key"
    DEPLOYMENT = "deployment"
    DEPLOYMENT_PROTECTION_RULE = "deployment_protection_rule"
    DEPLOYMENT_REVIEW = "deployment_review"
    DEPLOYMENT_STATUS = "deployment_status"
    DISCUSSION = "discussion"
    DISCUSSION_COMMENT = "discussion_comment"
    FORK = "fork"
    GITHUB_APP_AUTHORIZATION = "github_app_authorization"
    GOLLUM = "gollum"
    INSTALLATION = "installation"
    INSTALLATION_REPOSITORIES = "installation_repositories"
    INSTALLATION_TARGET = "installation_target"
    ISSUE_COMMENT = "issue_comment"
    ISSUES = "issues"
    LABEL = "label"
    MARKETPLACE_PURCHASE = "marketplace_purchase"
    MEMBER = "member"
    MEMBERSHIP = "membership"
    MERGE_GROUP = "merge_group"
    META = "meta"
    MILESTONE = "milestone"
    ORG_BLOCK = "org_block"
    ORGANIZATION = "organization"
    PACKAGE = "package"
    PAGE_BUILD = "page_build"
    PERSONAL_ACCESS_TOKEN_REQUEST = "personal_access_token_request"
    PING = "ping"
    PROJECT_CARD = "project_card"
    PROJECT = "project"
    PROJECT_COLUMN = "project_column"
    PROJECTS_V2 = "projects_v2"
    PROJECTS_V2_ITEM = "projects_v2_item"
    PUBLIC = "public"
    PULL_REQUEST = "pull_request"
    PULL_REQUEST_REVIEW_COMMENT = "pull_request_review_comment"
    PULL_REQUEST_REVIEW = "pull_request_review"
    PULL_REQUEST_REVIEW_THREAD = "pull_request_review_thread"
    PUSH = "push"
    REGISTRY_PACKAGE = "registry_package"
    RELEASE = "release"
    REMINDER = "reminder"
    REPOSITORY_ADVISORY = "repository_advisory"
    REPOSITORY = "repository"
    REPOSITORY_DISPATCH = "repository_dispatch"
    REPOSITORY_IMPORT = "repository_import"
    REPOSITORY_RULESET = "repository_ruleset"
    REPOSITORY_VULNERABILITY_ALERT = "repository_vulnerability_alert"
    SECRET_SCANNING_ALERT = "secret_scanning_alert"
    SECRET_SCANNING_ALERT_LOCATION = "secret_scanning_alert_location"
    SECURITY_ADVISORY = "security_advisory"
    SECURITY_AND_ANALYSIS = "security_and_analysis"
    SPONSORSHIP = "sponsorship"
    STAR = "star"
    STATUS = "status"
    TEAM_ADD = "team_add"
    TEAM = "team"
    WATCH = "watch"
    WORKFLOW_DISPATCH = "workflow_dispatch"
    WORKFLOW_JOB = "workflow_job"
    WORKFLOW_RUN = "workflow_run"


class ActionType(Enum):
    """
    Triggering actions of events that can trigger a workflow.
    Each action is only valid for certain events. For example:

    Attributes
    ----------
    ASSIGNED : str
        Available for `issues`.
    AUTO_MERGE_DISABLED : str
        Available for `pull_request`.
    AUTO_MERGE_ENABLED : str
        Available for `pull_request`.
    CLOSED : str
        Available for `issues`, `pull_request`.
    CONVERTED_TO_DRAFT : str
        Available for `pull_request`.
    CREATED : str
        Available for `issue_comment`.
    DELETED : str
        Available for `issue_comment`, `issues`, `pull_request`.
    DEMILESTONED : str
        Available for `issues`, `pull_request`.
    DEQUEUED : str
        Available for `pull_request`.
    EDITED : str
        Available for `issue_comment`, `issues`, `pull_request`.
    ENQUEUED : str
        Available for `pull_request`.
    LABELED : str
        Available for `issues`, `pull_request`.
    LOCKED : str
        Available for `issues`, `pull_request`.
    MILESTONED : str
        Available for `issues`, `pull_request`.
    OPENED : str
        Available for `issues`, `pull_request`.
    PINNED : str
        Available for `issues`.
    READY_FOR_REVIEW : str
        Available for `pull_request`.
    REOPENED : str
        Available for `issues`, `pull_request`.
    REVIEW_REQUEST_REMOVED : str
        Available for `pull_request`.
    REVIE_REQUESTED : str
        Available for `pull_request`.
    SYNCHRONIZE : str
        Available for `pull_request`.
    TRANSFERRED : str
        Available for `issues`.
    UNASSIGNED : str
        Available for `issues`, `pull_request`.
    UNLABELED : str
        Available for `issues`, `pull_request`.
    UNLOCKED : str
        Available for `issues`, `pull_request`.
    UNPINNED : str
        Available for `issues`.
    """

    ASSIGNED = "assigned"
    AUTO_MERGE_DISABLED = "auto_merge_disabled"
    AUTO_MERGE_ENABLED = "auto_merge_enabled"
    CLOSED = "closed"
    CONVERTED_TO_DRAFT = "converted_to_draft"
    CREATED = "created"
    DELETED = "deleted"
    DEMILESTONED = "demilestoned"
    DEQUEUED = "dequeued"
    EDITED = "edited"
    ENQUEUED = "enqueued"
    LABELED = "labeled"
    LOCKED = "locked"
    MILESTONED = "milestoned"
    OPENED = "opened"
    PINNED = "pinned"
    READY_FOR_REVIEW = "ready_for_review"
    REOPENED = "reopened"
    REVIEW_REQUEST_REMOVED = "review_request_removed"
    REVIE_REQUESTED = "review_requested"
    SYNCHRONIZE = "synchronize"
    TRANSFERRED = "transferred"
    UNASSIGNED = "unassigned"
    UNLABELED = "unlabeled"
    UNLOCKED = "unlocked"
    UNPINNED = "unpinned"


