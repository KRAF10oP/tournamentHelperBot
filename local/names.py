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
    GAME = "GAME"
    CREATED_AT = "CREATED_AT"
    REGISTRATION = "REGISTRATION"
    OPEN = "OPEN"
    CLOSED = "CLOSED"

    #Server
    CANT_REGISTER_DM = "CANT_REGISTER_DM"
    SERVER_ALREADY_IN = "SERVER_ALREADY_IN"
    SERVER_REGISTERED = "SERVER_REGISTERED"
    SERVER_UPDATED = "SERVER_UPDATED"
    ADDED_OPERATOR_ROLE = "ADDED_OPERATOR_ROLE"
    REMOVED_OPERATOR_ROLE = "REMOVED_OPERATOR_ROLE"
    OPERATOR_ROLE_ALREADY_EXISTS = "OPERATOR_ROLE_ALREADY_EXISTS"
    NO_OPERATOR_ROLES = "NO_OPERATOR_ROLES"
    MANY_PEOPLE_WITH_ROLE = "MANY_PEOPLE_WITH_ROLE"
    NOT_AN_OPERATOR_ROLE = "NOT_AN_OPERATOR_ROLE"
    NEED_MANAGE_ROLES = "NEED_MANAGE_ROLES"
    LANGUAGE_CHANGED = "LANGUAGE_CHANGED"
    CANT_ASSIGN_ROLE_TO_USER = "CANT_ASSIGN_ROLE_TO_USER"

    #Tournament
    TOURNAMENT_UNEXISTING = "TOURNAMENT_UNEXISTING"
    TOURNAMENT_ADDED = "TOURNAMENT_ADDED"
    TOURNAMENT_DELETED = "TOURNAMENT_DELETED"
    TOURNAMENT_GAME_WRONG = "TOURNAMENT_GAME_WRONG"
    TOURNAMENT_EXISTS_ALREADY = "TOURNAMENT_EXISTS_ALREADY"
    INPUT_CHECK_IN_REACTION = "INPUT_CHECK_IN_REACTION"
    NO_REACTION_IN_MSG = "NO_REACTION_IN_MSG"

    #Registration
    PLAYER_REGISTERED = "PLAYER_REGISTERED"
    PARTICIPANT_UNEXISTING = "PARTICIPANT_UNEXISTING"
    PARTICIPANT_DELETED = "PARTICIPANT_DELETED"
    PARTICIPANTS_DELETED = "PARTICIPANTS_DELETED"
    PARTICIPANT_REGISTRATION_FAILED = "PARTICIPANT_REGISTRATION_FAILED"
    REGISTRATION_OPEN_CHAT = "REGISTRATION_OPEN_CHAT"
    REGISTRATION_OPEN_ALREADY = "REGISTRATION_OPEN_ALREADY"
    REGISTRATION_CLOSED_MSG = "REGISTRATION_CLOSED_MSG"
    REGISTRATION_CLOSED_ALREADY = "REGISTRATION_CLOSED_ALREADY"
    REG_CHANNEL_NOT_FOUND = "REG_CHANNEL_NOT_FOUND"
    PARTICIPANT_COUNT = "PARTICIPANT_COUNT"
    PARTICIPANT_HAS_WARNINGS = "PARTICIPANT_HAS_WARNINGS"
    PARTICIPANTS_ROLE_REMOVED = "PARTICIPANTS_ROLE_REMOVED"
    NO_PARTICIPANTS_IN_TOURNAMENT = "NO_PARTICIPANTS_IN_TOURNAMENT" 

    #Tetr.io
    UNEXISTING_TETRIORANK = "UNEXISTING_TETRIORANK"
    TETRIORANKCAP_LOWERTHAN_RANKFLOOR = "TETRIORANKCAP_LOWERTHAN_RANKFLOOR"
    TETRIOTRCAP_LOWERTHAN_TRFLOOR = "TETRIOTRCAP_LOWERTHAN_TRFLOOR"
    #Tetr.io warnings
    TETRIO_INACTIVE_FOR_A_WEEK = "TETRIO_INACTIVE_FOR_A_WEEK" 
    TETRIO_PROMOTION_INMINENT = "TETRIO_PROMOTION_INMINENT" 
    TETRIO_NEAR_PROMOTION = "TETRIO_NEAR_PROMOTION" 
    TETRIO_PLAYER_DECAYING = "TETRIO_PLAYER_DECAYING" 
    TETRIO_HIGH_RD = "TETRIO_HIGH_RD" 

    #JStris+
    JSTRIS_PREDICTED_GLICKO = "JSTRIS_PREDICTED_GLICKO"
    