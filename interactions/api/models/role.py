from .misc import DictSerializerMixin


class RoleTags(DictSerializerMixin):
    """
    :ivar typing.Optional[int] bot_id: The id of the bot this role belongs to
    :ivar typing.Optional[int] integration_id: The id of the integration this role belongs to
    :ivar typing.Optional[Any] premium_subscriber: Whether if this is the guild's premium subscriber role
    """

    # TODO: Figure out what actual type it returns, all it says is null.

    __slots__ = ("_json", "bot_id", "integration_id", "premium_subscriber")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Role(DictSerializerMixin):
    """
    The role object.

    :ivar int id: Role ID
    :ivar str name: Role name
    :ivar int color: Role color in integer representation
    :ivar bool hoist: A status denoting if this role is hoisted
    :ivar typing.Optional[str] icon: Role icon hash, if any.
    :ivar typing.Optional[str] unicode_emoji: Role unicode emoji
    :ivar int position: Role position
    :ivar str permissions: Role permissions as a bit set
    :ivar bool managed: A status denoting if this role is managed by an integration
    :ivar bool mentionable: A status denoting if this role is mentionable
    :ivar typing.Optional[RoleTags] tags: The tags this role has
    """

    __slots__ = (
        "_json",
        "id",
        "name",
        "color",
        "hoist",
        "icon",
        "unicode_emoji",
        "position",
        "managed",
        "mentionable",
        "tags",
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
