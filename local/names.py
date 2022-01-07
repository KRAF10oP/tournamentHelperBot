from local.lang.eng import EnglishStrs
from local.lang.es import SpanishStrs

languages = {
    "SPANISH": SpanishStrs,
    "ENGLISH": EnglishStrs,
}

class StringsNames:
    DB_UPLOAD_ERROR = "DB_UPLOAD_ERROR"
    DB_DROP_ERROR = "DB_DROP_ERROR"
    ERROR = "ERROR"
    NOT_FOR_DM = "NOT_FOR_DM"
    ADMIN_ONLY = "ADMIN_ONLY"
    VALUE_SHOULD_BE_DEC = "VALUE_SHOULD_BE_DEC"
    VALUE_SHOULD_BE_TEXT_CHANNEL = "VALUE_SHOULD_BE_TEXT_CHANNEL"
    MESSAGE_NOT_FOUND = "MESSAGE_NOT_FOUND"
    MEMBER_NOT_FOUND_BY_ID = "MEMBER_NOT_FOUND_BY_ID"
    REACTION_TIMEOUT = "REACTION_TIMEOUT"
    MAY_TAKE_LONG = "MAY_TAKE_LONG"

    #Server
    CANT_REGISTER_DM = "CANT_REGISTER_DM"
    SERVER_ALREADY_IN = "SERVER_ALREADY_IN"
    SERVER_REGISTERED = "SERVER_REGISTERED"
    ADDED_OPERATOR_ROLE = "ADDED_OPERATOR_ROLE"
    REMOVED_OPERATOR_ROLE = "REMOVED_OPERATOR_ROLE"
    OPERATOR_ROLE_ALREADY_EXISTS = "OPERATOR_ROLE_ALREADY_EXISTS"
    NO_OPERATOR_ROLES = "NO_OPERATOR_ROLES"
    MANY_PEOPLE_WITH_ROLE = "MANY_PEOPLE_WITH_ROLE"
    NOT_AN_OPERATOR_ROLE = "NOT_AN_OPERATOR_ROLE"
    NEED_MANAGE_ROLES = "NEED_MANAGE_ROLES"
    LANGUAGE_CHANGED = "LANGUAGE_CHANGED"

    #Tournament
    TOURNAMENT_UNEXISTING = "TOURNAMENT_UNEXISTING"
    TOURNAMENT_ADDED = "TOURNAMENT_ADDED"
    TOURNAMENT_DELETED = "TOURNAMENT_DELETED"
    TOURNAMENT_EXISTS_ALREADY = "TOURNAMENT_EXISTS_ALREADY"
    INPUT_CHECK_IN_REACTION = "INPUT_CHECK_IN_REACTION"
    NO_REACTION_IN_MSG = "NO_REACTION_IN_MSG"

    #Registration
    PLAYER_REGISTERED = "PLAYER_REGISTERED"
    PARTICIPANT_UNEXISTING = "PARTICIPANT_UNEXISTING"
    PARTICIPANT_DELETED = "PARTICIPANT_DELETED"
    PARTICIPANTS_DELETED = "PARTICIPANTS_DELETED"
    REGISTRATION_OPEN_CHAT = "REGISTRATION_OPEN_CHAT"
    REGISTRATION_OPEN_ALREADY = "REGISTRATION_OPEN_ALREADY"
    REGISTRATION_CLOSED = "REGISTRATION_CLOSED"
    REGISTRATION_CLOSED_ALREADY = "REGISTRATION_CLOSED_ALREADY"
    PARTICIPANTS_ROLE_REMOVED = "PARTICIPANTS_ROLE_REMOVED"

    #Tetr.io
    UNEXISTING_TETRIORANK = "UNEXISTING_TETRIORANK"
    TETRIORANKCAP_LOWERTHAN_RANKFLOOR = "TETRIORANKCAP_LOWERTHAN_RANKFLOOR"
    TETRIOTRCAP_LOWERTHAN_TRFLOOR = "TETRIOTRCAP_LOWERTHAN_TRFLOOR"
