from dataclasses import dataclass
from models.registrationModels import RegistrationTemplate
from models.tournamentModels import Tournament

from utils import OptionTypes

from baseModel import BaseModel
from local.names import StringsNames
from games.default import BasePlayer

from contextExtentions.customContext import CustomContext, customContext
from controllers.tournamentController import tournamentController
from controllers.adminContoller import adminCommand

from bot import botGuilds, slash
from discord_slash.utils.manage_commands import create_option

@dataclass
class BasePlayer:
    game:str = None

    @staticmethod
    def fromDict(d):
        return BaseModel.fromDict(d, BasePlayer)

@slash.subcommand(
    base="tournaments",
    name="add_plain",
    guild_ids= botGuilds,
    description="Run registration for any tournament, really.",
    options=[
        create_option(  name="name", description="The tournament's name.",
                        option_type=OptionTypes.STRING, required=True),
        create_option(  name="game", description="The game's name.",
                        option_type=OptionTypes.STRING, required=False),
    ])
@adminCommand
@customContext
async def addTournamentPlain(ctx:CustomContext, name:str, game:str=""):
    if ctx.guild_id is None:
        await ctx.sendLocalized(StringsNames.NOT_FOR_DM)
        return
    if tournamentController.getTournamentFromName(ctx.guild_id, name):
        await ctx.sendLocalized(StringsNames.TOURNAMENT_EXISTS_ALREADY, name=name)
        return
    # uncomment on completing template implementation
    # customTemplate = templatesController.getTemplate(ctx.guild_id, template) # returns [] if doesnt exist
    # customTemplate.participantFields += controller.PLAYER_FIELDS
    tournament = Tournament(
        name=name,
        hostServerId=ctx.guild_id,
        game= game if game else "any",
        registrationTemplate= RegistrationTemplate(name, ctx.guild_id)
    )
    if tournamentController.addTournament(tournament):
        await ctx.sendLocalized(StringsNames.TOURNAMENT_ADDED, name=name, game=game)
    else:
        await ctx.sendLocalized(StringsNames.DB_UPLOAD_ERROR)
